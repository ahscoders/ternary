'''
Created on Apr 14, 2015

@author: Nick Goodman
'''
#importing libaries
import Adafruit_BBIO.GPIO as GPIO

#defining varables 
Value_0 = ''
Value_1 = ''
Value_2 = ''

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
                                Value_0 = 1
                                print (Value_0)
                if not GPIO.input("P8_14") and GPIO.input("P8_12"):
                                Value_0 = 2
                                print (Value_0)
                if not GPIO.input("P8_14") and not GPIO.input("P8_12"):
                                Value_0 = 0
                                print (Value_0)
                
            #reads the state of switch 2                
                if GPIO.input("P8_#") and not GPIO.input("P8_#"):
                                Value_1 = 1
                                print (Value_1)
                if not GPIO.input("P8_#") and GPIO.input("P8_#"):
                                Value_1 = 2
                                print (Value_1)
                if not GPIO.input("P8_#") and not GPIO.input("P8_#"):
                                Value_1 = 0
                                print (Value_1)
                
            #reads the state of switch 3                
                if GPIO.input("P8_#") and not GPIO.input("P8_#"):
                                Value_2 = 1
                                print (Value_2)
                if not GPIO.input("P8_#") and GPIO.input("P8_#"):
                                Value_2 = 2
                                print (Value_2)
                if not GPIO.input("P8_#") and not GPIO.input("P8_#"):
                                Value_2 = 0
                                print (Value_2)                

#runs the switch function
Main()

