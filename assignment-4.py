# TUPLES
#Q1-Write program to create a tuples with different data type and do the following operations.

t1=(1,2,4,'a','b',45,6,'x')

#   1.Find the length of Tuples.

print("tuple t1=",t1)
print("lenth of tuple t1 is:-",len(t1))

#Q2-Find largest and smallest elements of a tuples.

a=(98,35,56,78,35,23,43,68)
print("tuple a=",a)
print("largest element in tuple a is:-",max(a))
print("smallest element is tuple a is:-",min(a))

#Q3-Write a program to find the product of all elements of a tuples.

t=(2,3,4)
r=1
for x in t:
 r=r*x
print("tuple t=",t) 
print("product of all element of tuple t=",r)
 

#SETS
#Q1-Create two set using user defined values.

s1=set([])
a=int(input("enter the first no.:-"))
b=int(input("enter the second no.:-"))
c=int(input("enter the third no.:-"))
s1.add(a)
s1.add(b)
s1.add(c)
print(s1)

s2=set([])
a=int(input("enter the first no.:-"))
b=int(input("enter the second no.:-"))
c=int(input("enter the third no.:-"))
s2.add(a)
s2.add(b)
s2.add(c)
print(s2)

#  1.Calculate difference between two sets.
   
print("s1=" ,s1)
print("s2=" ,s2)
print("s3=",s1 - s2)
print("s4=",s2 - s1)

#   3.Print the result of intersection of two sets.

a=set([1,7,8,4,9])
b=set([5,6,7,3,8,9])
print(a & b)

#DICTIONNARIES
#Q1-Create a dictionary to store name and marks of 10 students by user input.
	
d={}
name=input("Enter your name: ")
marks= int(input("Enter your marks: "))
d[name]=marks
name=input("Enter your name: ")
marks= int(input("Enter your marks: "))
d[name]=marks
name=input("Enter your name: ")
marks= int(input("Enter your marks: "))
d[name]=marks
#name=input("Enter your name: ")
#marks= int(input("Enter your marks: "))
#d[name]=marks
#name=input("Enter your name: ")
#marks= int(input("Enter your marks: "))
#d[name]=marks
#name=input("Enter your name: ")
#marks= int(input("Enter your marks: "))
#d[name]=marks
#name=input("Enter your name: ")
#marks= int(input("Enter your marks: "))
#d[name]=marks
#name=input("Enter your name: ")
#marks= int(input("Enter your marks: "))
#d[name]=marks
#name=input("Enter your name: ")
#marks= int(input("Enter your marks: "))
#d[name]=marks
#name=input("Enter your name: ")
#marks= int(input("Enter your marks: "))
#d[name]=marks
print(d)

#Q2-Sort the dictionary created in previous question according to marks.

print(d)
values=list(d.values())
print(values)
values.sort()
print(values)

#Q3-Count the number of occurance of each letter in word "MISSISSIPPI" .
# Store count of every letter with the letter in a dictionary.

l=list("MISSISSIPPI")
d={}
d['M']=l.count('M')
d['I']=l.count('I')
d['S']=l.count('S')
d['P']=l.count('P')
print(d) 