#Functions

#QUESTION: 1
#Create a Function To Calculate Area of a circle by taking radius from user.


pie=3.14
def circle():
  c=float(input("Enter the radius of circle:-"))
  area=pie * c**2
  print("Area of circle=",area)
circle()	
	
	


#QUESTION: 2
#Write a Function Perfect And Perform Task.
# Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

l=[]
def perfect(n):
 sum=0
 for i in range(1,n):
  if n%i==0:
   sum=sum+i
 if sum==n:
    return True
 else:
    return False 
for i in range (1,1001):
 if perfect(i):
  print(i)
  l.append(i)
print("Perfect no betweeen 1 to 1000=",l)

#QUESTION: 3  
#Print multiplication table of 12 using recursion

def table(n,i):
  print(n," * ",i," = ",n*i)
  i=i+1
  if i<=10:
   table(n,i)
table(12,1)  
  
  

#QUESTION: 4  
#Using Recursion Write a function to calculate power of a number raised to other ( a^b ) using recursion.

n=int(input("Enter a number whose power you want:-"))
m=int(input("Enter a power of that number:-"))
def power(a,b):
 if b==1:
  return a
 else:
  pow=a*power(a,b-1)
  return pow  
p=power(n,m)
print("Power of given no. is:-",p)
  
#QUESTION: 5  
# Write a function to find factorial of a number but also store the factorials calculated in a dictionary.

d={}
n=int(input("Enter a number whose factorial is you want :-"))
def fact(x):
 if x==1 or x==0:
  return 1
 else:
  f=x*fact(x-1)
  return f
fact=fact(n)
print("factorial of given no.:-",fact)  
d[n]=fact
print(d)