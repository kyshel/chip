



# ping   (unix windows OK)
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os

def ping(host):
	"""
	Returns True if host (str) responds to a ping request.
	Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
	"""
	try:
	 	TIMEOUT_PING
	except NameError:
	 	TIMEOUT_PING = 2

	timeout = TIMEOUT_PING * 1000 if platform.system().lower()=='windows' else  TIMEOUT_PING
	number = '-n' if platform.system().lower() == 'windows' else '-c'
	devnull = open(os.devnull, 'w')


	# Building the command. Ex: "ping -c 1 google.com"
	command = ['ping', number, '1', '-w', str(timeout) , host]

	return subprocess.call(command,stdout=devnull, stderr=subprocess.STDOUT) == 0

a = ping('8.8.8.8')

print(a)



# date
from time import localtime, strftime
CUR_TIME = strftime("%Y%m%d_%H%M%S", localtime())
