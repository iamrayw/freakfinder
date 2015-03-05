#!/usr/bin/python
#freakfinder.py by iamrayw
#this script works only in *nix
from subprocess import Popen, PIPE
import subprocess
import os
import sys
def runModule(hostname):
	if hostname == None:
			print "Please enter a host."
			quit()
	strCmd = "openssl"
	strArgs = "s_client -connect " + hostname +":443 -cipher EXPORT"
	strFullCmd = "openssl s_client -connect " + hostname + ":443 -cipher EXPORT"
	ps = subprocess.Popen(strFullCmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	print "Script running..."
	output = ps.communicate()[0];
#   	print output
   	return output

  
def FreakFinder(output):    
    if ("alert handshake failure" in str(output)):
        return "Host not Vulnerable"
    else:
        return "Host is Vulnerable"
    

def main():
    output = runModule(sys.argv[1])
    print(FreakFinder(output))

if __name__ == "__main__":
	main()
