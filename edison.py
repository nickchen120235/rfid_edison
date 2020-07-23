import serial
import requests

ser = serial.Serial('/dev/ttyACM0')

try:
  while 1:
    while ser.inWaiting():
      data = ser.readline().decode().replace('\r\n', '')
      print(data)
      if data == 'Ready': continue
      r = requests.post('http://192.168.137.1:4000/api/sendCard', json={'cardID': data})
      print(r.status_code)

except KeyboardInterrupt:
  exit()
