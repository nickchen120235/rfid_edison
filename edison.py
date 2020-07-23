import serial
import requests

ser = serial.Serial('COM7')

try:
  while 1:
    while ser.inWaiting():
      data = ser.readline().decode().replace('\r\n', '')
      print(data)
      r = requests.post('http://localhost:4000/api/sendCard', json={'cardID': data})
      print(r.status_code)

except KeyboardInterrupt:
  exit()
