'''
Created on Apr 14, 2015

@author: robotics
'''
#importing libaries
import Adafruit_BBIO.GPIO as GPIO
def basextodec(base,number):
    bstr = str(number)
    power = len(bstr)
    decimal = 0
    for i in bstr:
        i = int(i)
        decimal += i*(base**power)
        power -= 1
    print (decimal)
def dectobasex(dec,base):
    number = ""
    while (dec != 0):
        dec1 = dec%base
        dec2 = dec/base
        dec = int(dec2)
        app = str(dec1)
        number = app +" "+ number
    print (number)
#defining varables 
value = ['','','']
#sets the GPIO to an input
GPIO.setup("P8_14", GPIO.IN)
GPIO.setup("P8_12", GPIO.IN)
GPIO.setup("P8_#", GPIO.IN)
GPIO.setup("P8_#", GPIO.IN)
GPIO.setup("P8_#", GPIO.IN)
GPIO.setup("P8_#", GPIO.IN)

#reads the state of all the switches
def Main():
        while True:
            #reads the state of switch 1
                if GPIO.input("P8_14") and not GPIO.input("P8_12"):
                                value[0] = '1'
                                value1 = ''.join(value)
                                basextodec(3,value1)
                                print (value1)
                if not GPIO.input("P8_14") and GPIO.input("P8_12"):
                                value[0] = '2'
                                value1 = ''.join(value)
                                basextodec(3,value1)
                                print (value1)
                if not GPIO.input("P8_14") and not GPIO.input("P8_12"):
                                value[0] = '0'
                                value1 = ''.join(value)
                                basextodec(3,value1)
                                print (value1)
                
            #reads the state of switch 2                
                if GPIO.input("P8_#") and not GPIO.input("P8_#"):
                                value[1] = '1'
                                value1 = ''.join(value)
                                basextodec(3,value1)
                                print (value1)
                if not GPIO.input("P8_#") and GPIO.input("P8_#"):
                                value[1] = '2'
                                value1 = ''.join(value)
                                basextodec(3,value1)
                                print (value1)
                if not GPIO.input("P8_#") and not GPIO.input("P8_#"):
                                value[1] = '0'
                                value1 = ''.join(value)
                                basextodec(3,value1)
                                print (value1)
                
            #reads the state of switch 3                
                if GPIO.input("P8_#") and not GPIO.input("P8_#"):
                                value[2] = '1'
                                value1 = ''.join(value)
                                basextodec(3,value1)
                                print (value1)
                if not GPIO.input("P8_#") and GPIO.input("P8_#"):
                                value[2] = '2'
                                value1 = ''.join(value)
                                basextodec(3,value1)
                                print (value1)
                if not GPIO.input("P8_#") and not GPIO.input("P8_#"):
                                value[2] = '0'
                                value1 = ''.join(value)
                                basextodec(3,value1)
                                print (value1)               

#runs the switch function
Main()
