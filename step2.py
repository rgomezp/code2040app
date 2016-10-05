import requests

#get string
r = requests.post('http://challenge.code2040.org/api/reverse', data = {'token':'06da63edb778ccce75da5f89aaffc09e'})

inString = r.text	#decode
outString = inString[::-1] 	#reverse

#return string
r = requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token':'06da63edb778ccce75da5f89aaffc09e', 'string':outString})
