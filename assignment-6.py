#LOOPS

#QUESTION: 1  Take a Input From User and Print On Screen.

i=1
n=int(input("How many student name you want to enroll:-"))
while i<=n:
 c=input("Enter name:-")
 print("student",i,"name:-",c)
 i=i+1
 
#QUESTION: 2  Write an Infinite Loop

#n=int(input("enter any number "))
#i=1
#while i<=n:
# print("Hello")


#QUESTION: 3  Create a List of Integers And Make a New List Which Will Store The Square Of The Elements

l=[12,4,10,400]
y=[]
i=0
for x in l:
  a=l[i]**2
  y.append(a)
  i=i+1  
print(y)  
 
#QUESTION: 4  Form a list for Integer,Float and String

integer=[]
for x in range(5):
 x=int(input("Enter the integer no:-"))
 integer.append(x)
print("list integer=",integer)

float=[]
for x in range(5):
 x=input("Enter the float no:-")
 float.append(x)
print("list float=",float)

string=[]
for x in range(5):
 x=input("Enter your name:-")
 string.append(x)
print("list string=",string) 


#QUESTION: 5  Using range(1,101), make a list containing even and odd numbers.
odd=[]
even=[]
for x in range (1,101):
 if x%2==0:
   even.append(x)
 else:
   odd.append(x)
print("odd no=",odd)
print("even no=",even)   

#QUESTION: 6  Print Patterns


for x in range(0,10):
 for y in range(0,x+1):
  print("*",end=" ")
 print()
 
#QUESTION: 7  Create a User Defined Dictionary

d={}
for x in range(4):
 name=input("Enter your name: ")
 marks= int(input("Enter your marks: "))
 d[name]=marks
print(d)

#QUESTION: 8  Perform Inputs And Search and deletion From User in a list

list=[]
for x in range(5):
 x=int(input("Eenter a no. in list:-"))
 list.append(x)
print("list=",list)
key=int(input("Enter a no. you want to search:-"))
for y in list:
 if y==key:
   print("vaue found in list=",y)
de=int(input("Enter a no. you want to del:-"))
for y in list:
 if y==de:
    print(list.remove(de))
print(list)	
   
   
 
 
