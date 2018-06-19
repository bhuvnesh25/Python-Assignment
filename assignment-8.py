#Common Modules in Python.

#QUESTION: 1  
#What is Time Tuple?

import time
print(time.gmtime(60*60*24))

#QUESTION: 2  
#WAP To Get Formatted Time?

import time
print(time.ctime())

#QUESTION: 3  
#Extract Month from the Time.
l=[]
import time
l=list(time.localtime())
print("Month=",l[1])

#QUESTION: 4  
#Extract Day from the Time.

l=[]
import time
l=list(time.localtime())
print("Day=",l[2])

#QUESTION: 5  
#Extract date (ex : 11 in 11/01/2021) from the time.

l=[]
import time
l=list(time.localtime())
print("Date=",l[2],"/",l[1],"/",l[0])



#QUESTION: 6  
#WAP Time Using Local Time.

import time
print(time.localtime())

#QUESTION: 7  
#Find the Factorial of a Number

import math
print("Enter a number whose Factorial you want to find")
x=int(input("Enter a number="))
print("Factorial of ",x,"=",math.factorial(x))

#QUESTION: 8  
#Find the GCD of a Number 

import math
print("Give greatest common divisor of the integers a and b. is the largest positive integer that divides both a and b. gcd(0, 0) returns 0.")
a=int(input("Enter a 1st number="))
b=int(input("Enter a 2nd number="))
print("gcd=",math.gcd(a,b))

#QUESTION: 9  
#Use OS package.

import os

#1. Get current working directory.

print(os.getcwd())


#2. Get the user environment.

print(os.environ)