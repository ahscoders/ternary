'''
Created on Apr 14, 2015

@author: robotics
'''
def basextodec(base,number):
   bstr = str(number)
   power = len(bstr)
   decimal = 0
   for i in bstr:
      i = int(i)
      decimal += i*(base**power)
      power -= 1
   print (decimal)
def dectobasex(base,dec):
   number = ""
   while (dec != 0):
      dec1 = dec%base
      dec2 = dec/base
      dec = int(dec2)
      app = str(dec1)
      number = app +" "+ number
   print (number)
#######################################
basextodec(2,6666666666666)
dectobasex(3,50)
dectobasex(2.718,154000)