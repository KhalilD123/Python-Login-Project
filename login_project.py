import sys
import os
import re
import time

print ('* ------------------------------------ *')
print ('* Please enter username and password   *')
print ('* ------------------------------------ *')

#Username field \/
while True:
	username = input('Please enter your username: ')
	if re.match(r'[a-zA-Z0-9]{3,12}', username):
		break
	else:
		print('Error: Please enter a username')




#Password field \/
while True:
	password = input('Please enter your password: ')
	if re.match(r'[a-zA-Z0-9]{3,9}', password):
		break
	else:
		print('Error: Please enter a password')
