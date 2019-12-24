#!/usr/bin/python

# enable debugging
import cgitb
import MySQLdb
import datetime

cgitb.enable()

print "Content-Type: text/html\r\n\r\n"
print

print "<html><head><title>Greenhouse</title></head><body>"

hdg = "LAST 40 READINGS"

print ("<h1>%s</h1>" % (hdg))

db = MySQLdb.connect(host='localhost',user='Greenhouse.Reader',passwd='e463daea5f91438a', db='Greenhouse')
dbc = db.cursor()
sql = "SELECT ReadingAirTemp, ReadingCPUTemp, ReadingHumidity, ReadingTimestamp FROM Greenhouse.Readings WHERE ReadingAirTemp IS NOT NULL ORDER BY ReadingTimestamp DESC LIMIT 40;"
#sql = "SELECT ReadingAirTemp FROM Greenhouse.Readings ORDER BY ReadingTimestamp DESC LIMIT 10;"
dbc.execute(sql)
rows = dbc.fetchall()


for row in rows:

#	print("<div>%s</div>" % (str(row)))
	print ("<div>Air Temp=%.2f&deg;C, CPU Temp=%.2f&deg;C, Humidity=%.2f%%RH at %s</div>" % (row[0],row[1],row[2],row[3].strftime("%H:%M on %a %d %b")))


db.close()

print "</body></html>"





