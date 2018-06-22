#ASSIGNMENT-9
#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.

import threading
from threading import Thread
import time

def display():
 
 time.sleep(5)
 print(threading.current_thread().getName(),":I am Bhuvnesh")
 
t=Thread(target=display)
t.setName("MyThread")
t.start()
print(threading.current_thread().getName()) 
#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between.

 
def number():
 
 for x in range(1,11):
  time.sleep(1)
  print(threading.current_thread().getName(),":",x)
 
t=Thread(target=number)
t.setName("Number")
t.start()


#Q3. Make a list that has 5 elements.
#    Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#    Delay goes like 2sec-4sec-6sec-8sec-10sec.


l=[1,2,3,4,5]
def delay():
  
  n=0
  for x in l:
   if n%2==0:
    time.sleep(n)
    print(threading.current_thread().getName(),":",x)
    n=n+2
  
t=Thread(target=delay)
t.setName("List")
t.start()
     

#Q4. Call factorial function using thread.

def fact():
 
 n=int(input("Enter the number to get factorial:-"))
 f=1
 while n>=1:
   f=f*n
   n=n-1
 print(threading.current_thread().getName(),":",f)
 
t=Thread(target=fact)
t.setName("Factorial")
t.start() 
  
 