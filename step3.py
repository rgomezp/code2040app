import requests

#get data
r = requests.post('http://challenge.code2040.org/api/haystack', data = {'token':'06da63edb778ccce75da5f89aaffc09e'})

data = r.json()

needle = data['needle']
haystack = data['haystack']

index = 0
for item in haystack:
	if item!=needle:
		index+=1
	else:
		print "Found"
		break

print "index:", index

print haystack
print needle

#return index
r = requests.post('http://challenge.code2040.org/api/haystack/validate', data = {'token':'06da63edb778ccce75da5f89aaffc09e','needle':index})
