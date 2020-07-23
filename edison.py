import serial
import requests
import flask
from flask_cors import CORS
import atexit

app = flask.Flask(__name__)
app.config['DEBUG'] = True
CORS(app)

@app.route('/api/flask', methods=['GET'])
def test():
  return 'Hello Flask'

@app.route('/api/getCard', methods=['GET'])
def getCard():
  ser = serial.Serial('COM7')
  while 1:
    while ser.inWaiting():
      cardID = ser.readline().decode().replace('\r\n', '')
      print(cardID)
      if cardID != '' and cardID != 'Ready':
        transfer = {'cardID': cardID}
        ser.close()
        return transfer

if __name__ == '__main__': 
  app.run()