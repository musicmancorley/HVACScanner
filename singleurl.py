import urllib2

import requests

theresponse=0
machineprefix="http://192.168.1."
securemachineprefix="https://192.168.1."
#add 1 to make it 1-254
for i in range(20,21):
    try:
        theresponse = urllib2.urlopen(securemachineprefix+str(i)+"/web/")
        print theresponse.read()
        #print urlbodycontent
     

        raw_input('Press any key to continue with the scan...')
    except:
        print "http://192.168.1."+str(i)
        print "no HVAC machines here..."
