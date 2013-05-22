import sys
sys.path.append("/afs/cats.ucsc.edu/users/f/jrowley/classs/beautifulsoup4-4.2.0")
import urllib
import urllib2
import string
import time
from bs4 import BeautifulSoup
from datetime import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import smtplib

fromaddr = 'email@ucsc.edu'
toaddrs  = 'email@ucsc.edu'
toaddrs2  = 'email@ucsc.edu'
toaddrs3  = '1234567810@txt.att.net'
msg = 'PHYSICS!!!!!!!'
msg2 = 'DUDE Physics Opened! Enroll in it!!!'  
msg3 = 'Michaela! Joes Physics Opened! Get him to enroll in it!!! Like call him if you have a second and dont mind. Thank you!!!!'  

# Credentials (if needed)  
username = 'youremail@address.here'
password = 'yourpasswordhere' #plain text passwords are highly secure. well not at all but yeah, okay I have no defense besides I'm lazy

# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')
response = urllib2.urlopen('https://pisa.ucsc.edu/class_search/index.php?action=detail&class_data=YTozMDp7czo0OiJTVFJNIjtzOjQ6IjIxMzIiO3M6OToiQ0xBU1NfTkJSIjtzOjU6IjYxNTE2IjtzOjEzOiJDTEFTU19TRUNUSU9OIjtzOjI6IjAxIjtzOjEzOiJDTEFTU19NVEdfTkJSIjtzOjE6IjEiO3M6MTI6IlNFU1NJT05fQ09ERSI7czoxOiIxIjtzOjEwOiJDTEFTU19TVEFUIjtzOjE6IkEiO3M6NzoiU1VCSkVDVCI7czo0OiJQSFlTIjtzOjExOiJDQVRBTE9HX05CUiI7czo1OiIgICA2QyI7czo1OiJERVNDUiI7czoxNDoiSW50cm8gUGh5cyBJSUkiO3M6MTM6IlNTUl9DT01QT05FTlQiO3M6MzoiTEVDIjtzOjEwOiJTVEFSVF9USU1FIjtzOjc6IjAyOjAwUE0iO3M6ODoiRU5EX1RJTUUiO3M6NzoiMDM6MTBQTSI7czo5OiJGQUNfREVTQ1IiO3M6MTY6IlRoaW0gTGVjdHVyZSAwMDMiO3M6MzoiTU9OIjtzOjE6IlkiO3M6NDoiVFVFUyI7czoxOiJOIjtzOjM6IldFRCI7czoxOiJZIjtzOjU6IlRIVVJTIjtzOjE6Ik4iO3M6MzoiRlJJIjtzOjE6IlkiO3M6MzoiU0FUIjtzOjE6Ik4iO3M6MzoiU1VOIjtzOjE6Ik4iO3M6OToiRU5STF9TVEFUIjtzOjE6IkMiO3M6ODoiV0FJVF9UT1QiO3M6MToiMCI7czo4OiJFTlJMX0NBUCI7czozOiIyNDAiO3M6ODoiRU5STF9UT1QiO3M6MzoiMjQ0IjtzOjk6IkxBU1RfTkFNRSI7czoxMDoiU3RlaW5hY2tlciI7czoxMDoiRklSU1RfTkFNRSI7czo3OiJBZHJpYW5lIjtzOjExOiJNSURETEVfTkFNRSI7TjtzOjE2OiJDT01CSU5FRF9TRUNUSU9OIjtzOjE6IiAiO3M6NToiVE9QSUMiO047czoxMjoiRElTUExBWV9OQU1FIjtzOjEzOiJTdGVpbmFja2VyLEEuIjt9')
html = response.read()
soup = BeautifulSoup(html)
bar = []
bar = soup.find("div", {"id": "detail_table"})
closed = []
closed = bar.find(alt="Closed")
dattt = str(datetime.time(datetime.now())).replace(":", "").replace(".", "")
dataFile = open("/afs/cats.ucsc.edu/users/f/jrowley/public_html/physics.html", "w")
dataFile.write("Still Closed as of %s\n" % str(datetime.now()))
dataFile.close()

if closed is None:
    server.starttls()
    server.login(username,password)
    print "WOAH"
    server.sendmail(fromaddr, toaddrs, msg)
    server.sendmail(fromaddr, toaddrs, msg)
    server.sendmail(fromaddr, toaddrs2, msg2)
    server.sendmail(fromaddr, toaddrs3, msg2)
    server.sendmail(fromaddr, toaddrs4, msg3)
    server.sendmail(fromaddr, toaddrs3, msg2)
    dataFile = open("/afs/cats.ucsc.edu/users/f/jrowley/public_html/physics.html", "w")
    dataFile.write("ITS OPEN %s \n" % str(datetime.time(datetime.now())))
# dataFile.write()
    dataFile.close()
    print closed

server.quit()      
#if (soup.find_all(alt='Closed') == '<img alt="Closed" src="https://pisa.ucsc.edu/cs9/prd/images/PS_CS_STATUS_CLOSED_ICN_1.gif" title="Closed"> Closed</img>'):
#    print 'happy'
#print "\n"
#print soup.find_all(text='Open')
# print len(bar)
