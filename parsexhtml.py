import sys
import xml.dom.minidom
import mysql.connector



document = xml.dom.minidom.parse(sys.argv[1])
weatherElement1 = document.getElementsByTagName('a') #10
x = weatherElement1[10].childNodes[0]
cityAll = x.nodeValue

for char in cityAll:
  if char == ',':
      m = cityAll.index(',')
      city = cityAll[:m]
      break
  elif char == '/':
      q = cityAll.index('/')
      city = cityAll[:q]
      break
  elif ',' and '/' not in cityAll:
      s = cityAll.index(' ')
      city = cityAll[s+1:]


weatherElementState1 = document.getElementsByTagName('a')
k = weatherElementState1[10].childNodes[0]
stateA1 = k.nodeValue
weatherElementState2 = document.getElementsByTagName('h2')
g = weatherElementState2[1].childNodes[0]
stateA2 = g.nodeValue
for char in stateA1:
  if char == ',':
      j = stateA1.index(',')
      state = stateA1[j+1:]
  elif ',' not in stateA1:      
    h = stateA2.index('\n')
    state = stateA2[h-2:h]

weatherElement2 = document.getElementsByTagName('h4')
y = weatherElement2[2].childNodes[0]
weather = y.nodeValue

weatherElement3 = document.getElementsByTagName('h1')
z = weatherElement3[1].childNodes[0]
temp = z.nodeValue
i = temp.index(chr(176))
temperature = temp[0:i] #

weatherElement4 = document.getElementsByTagName('td')
a = weatherElement4[1].childNodes[0]
humi = a.nodeValue
n = humi.index('%')
humidity = humi[:n]

weatherElement5 = document.getElementsByTagName('td')
b = weatherElement5[5].childNodes[0]
press = b.nodeValue
pressure = 0.0
for t in press.split():
    try:
        pressure = pressure + (float(t))
    except ValueError:
        pass
print("state,city,weather,temperature,humidity,pressure")
print(state, city, weather, temperature, humidity, pressure)

def insert(cursor):
	query = 'INSERT INTO weathertable(state, city, weather, temperature, humidity, pressure) VALUES (%s, %s, %s, %s, %s, %s)'
	cursor.execute(query, (state, city, weather, temperature, humidity, pressure))

try:
	cnx = mysql.connector.connect(host='localhost', user='root', password='root', database='weather')
	cursor = cnx.cursor()

	insert(cursor)
	cnx.commit()

	cursor.close()
except mysql.connector.ERROR as err:
	print(err)
finally:
	cnx.close()

#new_csv = "new_Csv.csv"
#csv = open(new_csv, "a")

row = state + "," + city + ',' + weather + ',' + temperature + ',' + humidity + ','   + str(pressure) + '\n'
#csv.write(row)


