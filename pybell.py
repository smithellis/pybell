#import sys, os, socket
#ipdefine contains the list of IP addresses we want to check
import subprocess
import ipdefine

#Let's see if the device is on the network right now
#for device, ipadd in ipdefine.ip_address.iteritems():
#	try:
#	    socket.gethostbyaddr(ipadd)
#	    # If previous line doesn't throw exception, IP address is being used; let's perform some action
#	    print device+" on network"
#	except socket.herror:
#	    # socket.gethostbyaddr() throws error, so IP is not being used at present; device not on network
#	    print device+" not on network"

for device, ipadd in ipdefine.ip_address.iteritems():
	res = subprocess.call(['ping','-n','1',ipadd],stdout=False)
	if res == 0:
		print device+" is on network."
	elif res == 2:
		print device+" is not responding."
	else: 
		print "Ping of "+device+" failed."