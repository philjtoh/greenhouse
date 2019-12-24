import Adafruit_DHT
import MySQLdb
import sched, time, datetime
from config import writerpwd

delay = 600

def take_reading(sc):
	sc.enter(delay, 1, take_reading, (sc, ))
	humidity, airtemp = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

	with open('/sys/class/thermal/thermal_zone0/temp') as cputempfile:
		cputemp = float(cputempfile.read()) / 1000

	now = datetime.datetime.now()
	db = MySQLdb.connect(host='localhost',user='Greenhouse.Writer',passwd=writerpwd, db='Greenhouse')
	dbc = db.cursor()
	sql = "INSERT INTO Greenhouse.Readings (ReadingTimestamp, ReadingAirTemp, ReadingHumidity, ReadingCPUTemp)"
	sql += "VALUES ('%s', %.2f, %.2f, %.2f);" % (now.strftime('%Y-%m-%d %H:%M:%S') ,airtemp, humidity, cputemp)
	print(sql)
	dbc.execute(sql)
	db.commit()
	db.close()


#Reader pw = e463daea5f91438a

try:
	sc = sched.scheduler(time.time, time.sleep)

	sc.enter(0, 1, take_reading, (sc, ))

	sc.run()
except Exception, e:
	print(str(e))
finally:
	db.close()






