#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '''
  ____                _               _   _           _      
 / ___|_ __ __ _  ___| | _____ _ __  | | | | __ _ ___| |__  
| |   | '__/ _` |/ __| |/ / _ \ '__| | |_| |/ _` / __| '_ \ 
| |___| | | (_| | (__|   <  __/ |    |  _  | (_| \__ \ | | |
 \____|_|  \__,_|\___|_|\_\___|_|    |_| |_|\__,_|___/_| |_|

                                           Creative By Aink


'''
import md5
import logging


#1 debug - detailed info
#2 info - confirmation that things according to plan
#3 warning - something unexpected
#4 error - some function failed
#5 critical - something failed appliation must close.


counter = 1
#---------------------------------------------------------------------log file--------------------------------------------------------------------------
logging.basicConfig(filename='logfilecrack.log',level=logging.INFO)
def main():
    try:
        pwfile = open.read()
        #mathFail = 1/0
       
    except Exception, e:
        logging.info(str(e))

main()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
pass_in = raw_input(" Silahkan Masukan MD5 Hash: ")
print '''

'''
pwfile = raw_input(" Silahkan Masukan Lokasi File Password (wordlist): ")

try:
        pwfile = open(pwfile, "r")

except:
        print "\nFile Tidak Ditemukan."
        quit()

for password in pwfile:
        filemd5 = md5.new(password.strip()).hexdigest()
        print "Mencoba Password %d: %s " % (counter, password.strip())

        counter += 1
        if pass_in == filemd5:
                print "\nDitemukan \nPassword: %s" % password
                break
            
else: 
    print "\nMaaf Password Tidak Ditemukan."
    print ""
    print ""
    print "\nSilahkan coba lagi !! "
