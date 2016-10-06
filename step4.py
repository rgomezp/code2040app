import requests
import json

#get data
r = requests.post('http://challenge.code2040.org/api/prefix', data = {'token':'06da63edb778ccce75da5f89aaffc09e'})

data = r.json()

prefix = data['prefix']
array = data['array']

array = [x.encode('UTF8') for x in array]	#convert to ascii

newArray = [] 	#array to which copy items with given prefix

for item in array:
	if item[0:3]!=prefix[0:3]:
		newArray.append(item)

print "prefix:", prefix
print "array:", array
print "new array:", newArray

r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = {'token':'06da63edb778ccce75da5f89aaffc09e','array':newArray})

print r.text
