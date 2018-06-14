#Q1-Create a list with defined inputs.

# program for user defined inputs.
list=[]
a=int(input("enter first elemet of list:-"))
b=int(input("enter second element of list:-"))
list.append(a)
list.append(b)
print (list)

# program for defined inputs.
name=["Bhuvnesh","Geetika","Pratham"]
print(name)
roll_no=[12,21,30]
print(roll_no)

#Q2-Add the following list to above created list:['"google","apple","facebook","microsoft","tesla"'].

application=['"google","apple","facebook","microsoft","tesla"']
print(name.extend(application))
print(name)


#Q3-Count the number of time an object occurs in a list.

list=[1,2,1,4,1,7,6]
print(list.count(1))
list=["b","h","b","e","r","b"]
print(list.count("b"))



#Q4-Create a list with number and sort it in ascending order.

z=[3,6,10,45,12,56,71,23,13,76]
print(z.sort())
print(z)
#Q5-Given are two one-dimensional array A and B which are sorted in ascending order.write program to merge them into a single sorted array C that contain every item from arrays A and B in ascending order list.

A=[2,56,73,13]
A.sort()
print(A)
B=[5,65,72,12]
B.sort()
print(B)
C=[]
C.extend(A)
C.extend(B)
print(C)
C.sort()
print(C)



#Q6-Implement a stack and queue using lists.

#Implement stack using list.
stack=[]
stack.append(123)
stack.append(258)
print("insertion in list ")
print(stack)
stack.pop()
print("after poping from list")
print(stack)
print("hence stack using list is study")

#Implement queue using list.
queue=[]
queue.append(344)
queue.append(355)
queue.append(233)
print("insertion from one end")
print(queue)
del queue[0]
print("poping from another end")
print(queue)


#Q7-Count even and odd number in that list.

list=[1,2,3,4,5,6,7,8,9,10,11,12,34,35,67,22,90]
even_count=0
odd_count=0
for x in list:
 if x%2==0:
  even_count=even_count+1
 else:
  odd_count=odd_count+1
print("count even in list:",even_count)
print("count odd in list:",odd_count)

	  
	  
	  
