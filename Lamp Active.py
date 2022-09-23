import serial
import time


print('type H to turn the lamp on')
print('type L to turn the lamp off')
print('type Q to exit the program')

ser = serial.Serial('COM4', 9800, timeout=1)
time.sleep(1)
SoftwareSerial bluetooth(rxpin, txpin)
time.sleep(1)
bluetooth.begin(9600)

user_input = 'L'
while user_input != 'Q':
    user_input = input('H = on, L = off, Q = quit' : )
    byte_command = encode(user_input)
    ser.writelines(byte_command)   
    time.sleep(0.1) 

ser.close()