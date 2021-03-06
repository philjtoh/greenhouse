import MySQLdb
from PIL import Image
import io
import datetime
import sys
import base64
from config import readerpwd

limit = None
year=2019
starthour=9
endhour=14

if len(sys.argv) > 1:
	limit = int(sys.argv[1])
	print ("doing %d photos..." % (limit,))
else:
	print ("doing all photos...")

db = MySQLdb.connect(host='localhost',user='Greenhouse.Reader',passwd=readerpwd, db='Greenhouse')
dbc = db.cursor()

filter = 'AND YEAR(ReadingTimestamp) = %d AND HOUR(ReadingTimestamp) >= %d AND HOUR(ReadingTimestamp) < %d' % (year, starthour, endhour)

#start with the oldest photo

sql = "SELECT ReadingPhoto, ReadingTimestamp FROM Greenhouse.Readings WHERE ReadingPhoto IS NOT NULL %s ORDER BY ReadingTimestamp ASC LIMIT 1;" % (filter,)
#print (sql)
dbc.execute(sql)
rows = dbc.fetchall()

photo = rows[0][0]
timestamp = rows[0][1]
hasrow = True
index = 1

while (hasrow and (limit is None or index <= limit)):

	#save it to disk as image****.png

	photoimage = Image.open(io.BytesIO(base64.b64decode(photo)))
	filename = "frames/image%04d.png" % (index,)
	photoimage.save(filename, "png")
	print ("wrote %s to disk." % (filename,))

	#continue with next oldest photo

	sql = "SELECT ReadingPhoto, ReadingTimestamp FROM Greenhouse.Readings WHERE ReadingPhoto IS NOT NULL AND ReadingTimestamp > '%s' %s ORDER BY ReadingTimestamp ASC LIMIT 1;" % (timestamp,filter)
	#print (sql)
	dbc.execute(sql)
	rows = dbc.fetchall()

	if len(rows) is 0:
		hasrow = False
	else:
		photo = rows[0][0]
		timestamp = rows[0][1]
		index = index + 1

db.close()
print ("done!")
