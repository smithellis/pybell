import sys, os, socket

#Our Phone has a known, assigned IP address
ip_address = '192.168.0.148'

#Let's see if the Phone is on the network right now
try:
    socket.gethostbyaddr(ip_address)
    # If previous line doesn't throw exception, IP address is being used; let's perform some action
    print "Phone on network"
except socket.herror:
    # socket.gethostbyaddr() throws error, so IP is not being used at present; Phone not on network
    print "Phone not on network"
