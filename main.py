import datetime

import serial
import time

ser = serial.Serial('com6', 9600)
time.sleep(2)

print("Connection established successfully ")

file = open('batteryLogs.csv', 'w+')

file.write("Time,Reading \n")

while True:
    getData = str(ser.readline())
    data = getData[2:-5]
    newData = ''
    ct = str(datetime.datetime.now().time())
    print(ct[:-7], data, '\n')
    log = ct[:-7] + ',' + data + '\n'
    file.write(log)

