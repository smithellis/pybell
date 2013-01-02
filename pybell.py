import sys, os, socket
#ipdefine contains the list of IP addresses we want to check
import ipdefine

#Let's see if the Phone is on the network right now
for ipadd in ipdefine.ip_address:
	try:
	    socket.gethostbyaddr(ipadd)
	    # If previous line doesn't throw exception, IP address is being used; let's perform some action
	    print "Phone on network"
	except socket.herror:
	    # socket.gethostbyaddr() throws error, so IP is not being used at present; Phone not on network
	    print "Phone not on network"