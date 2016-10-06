import requests

r = requests.post('http://challenge.code2040.org/api/dating', data = {'token':'06da63edb778ccce75da5f89aaffc09e'})

data = r.json()

datestamp = data['datestamp']
interval = data['interval']

datestamp = datestamp.encode('UTF8') 	#convert to ascii

print datestamp

#datestamp time info - convert to seconds
hours = int(datestamp[11:13])
minutes = int(datestamp[14:16])
seconds = int(datestamp[17:19])
days = int(datestamp[8:10]) 
month = int(datestamp[5:7])

minutes = minutes + 60*hours
seconds = seconds + 60*minutes

#add datestamp seconds to interval
interval = interval + seconds	#now, total interval is offset from date + 00:00:00

#convert combined (datestamp + interval) seconds to days, hours, minutes, seconds
m, s = divmod(interval, 60) 	#convert to minutes with remainder in seconds
h, m = divmod(m, 60)		#convert to hours with remainder in minutes
d, h = divmod(h, 24)		#convert to days with remainder in hours

monthMap = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} 	#days per month

maxDays = monthMap[month]

d = days + d

#check if adding days spills over into next month
if(d>maxDays):
	month+=1
	d = d - maxDays


datestamp = list(datestamp)

#change to correct format (i.e. '9' -> '09')
vals = [month,d,h,m,s]
formattedVals = []

for i in vals:
	if i < 10:
		i = "0"+ str(i)
	else:
		i = str(i)
	formattedVals.append(i)

#insert values
datestamp = list(datestamp)

datestamp[5:7] = formattedVals[0]
datestamp[8:10] = formattedVals[1]
datestamp[11:13] = formattedVals[2]
datestamp[14:16] = formattedVals[3]
datestamp[17:19] = formattedVals[4]

datestamp = "".join(datestamp)

print datestamp


r = requests.post('http://challenge.code2040.org/api/dating/validate', json = {'token':'06da63edb778ccce75da5f89aaffc09e', 'datestamp':datestamp})

print r.text
