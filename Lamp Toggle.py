import serial
import time

rxpin = 2
txpin = 3

print('type a number to turn the lamp on for that amount of time')
print('type Q to exit the program')

ser = serial.Serial('COM4', 9800, timeout=1)
time.sleep(1)
SoftwareSerial bluetooth(rxpin, txpin)
time.sleep(1)
bluetooth.begin(9600)

while user_input != 'Q':
  input=ser.readline() 
  if input:
    user_input=int(h1)
  for i in range(user_input):
    ser.writelines(b'H')   
    time.sleep(0.2)         

ser.close()