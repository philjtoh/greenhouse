#import Adafruit_DHT
import MySQLdb
import sched, time, datetime
from picamera import PiCamera
import StringIO
import base64

camera = PiCamera()

delay = 1800

def take_photo(sc):
	sc.enter(delay, 1, take_photo, (sc, ))
#	humidity, airtemp = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

#	with open('/sys/class/thermal/thermal_zone0/temp') as cputempfile:
#		cputemp = float(cputempfile.read()) / 1000
	img = StringIO.StringIO()
	camera.capture(img, format="jpeg")
	imgblob = MySQLdb.escape_string(base64.b64encode(img.getvalue()))

	now = datetime.datetime.now()
	db = MySQLdb.connect(host='localhost',user='Greenhouse.Writer',passwd='97ad48e2298fbeb9', db='Greenhouse')
	dbc = db.cursor()
	sql = "INSERT INTO Greenhouse.Readings (ReadingTimestamp, ReadingPhoto)"
	sql += "VALUES ('%s','%s');" % (now.strftime('%Y-%m-%d %H:%M:%S') ,imgblob)
#	print(sql)
	dbc.execute(sql)
	db.commit()
	db.close()
#	print("Photo at %s" % (ReadingTimestamp.strftime("%H:%M on %a %d %b")))
	print("Photo taken")

#Reader pw = e463daea5f91438a

try:
	sc = sched.scheduler(time.time, time.sleep)

	sc.enter(0, 1, take_photo, (sc, ))

	sc.run()
except Exception, e:
	print(str(e))
finally:
	db.close()






