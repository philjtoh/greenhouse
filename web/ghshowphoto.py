#!/usr/bin/python

# enable debugging
import cgitb
import MySQLdb
import datetime
from congig import readerpwd

cgitb.enable()

print "Content-Type: text/html\r\n\r\n"
print

print "<html><head><title>Greenhouse</title></head><body>"

hdg = "LATEST PHOTO"

print ("<h1>%s</h1>" % (hdg))

db = MySQLdb.connect(host='localhost',user='Greenhouse.Reader',passwd=readerpwd, db='Greenhouse')
dbc = db.cursor()
sql = "SELECT ReadingPhoto, ReadingTimestamp FROM Greenhouse.Readings WHERE ReadingPhoto IS NOT NULL ORDER BY ReadingTimestamp DESC LIMIT 1;"
#sql = "SELECT ReadingAirTemp FROM Greenhouse.Readings ORDER BY ReadingTimestamp DESC LIMIT 10;"
dbc.execute(sql)
rows = dbc.fetchall()

#	So at this point row[0] is ReadingPhoto (a string) and row[1] is ReadingTimestamp (another string)

for row in rows:

#	print("<div>%s</div>" % (str(row)))
#	print("<img src=\"data:image/jpeg;base64,%s\" />" % (row[4])) - this is Thom's rough template of what I should use
	print("<div>Photo taken at %s </div>" % (row[1].strftime("%H:%M on %a %d %b")))
	print("<img src=\"data:image/jpeg;base64,%s\" />" % (row[0]))
#	print("<div>Photo taken at%s<img src=\"data:image/jpeg;base64,%s\" /></div>" %  (strftime("%H:%M on %a %d %b")).(row[1],row[0]))

db.close()

print "</body></html>"








