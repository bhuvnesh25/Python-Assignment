#Dicision control statement.
#Q1-Take a input from user and cheack wheather it is leap year or not.

y=int(input("Enter the year you want to check weather it is leap year or not:-"))
if y%400==0 or y%4==0 and y%100!=0:
 print(y," It is a leap year")
else:
 print(y,"It is not a leap year")
 
#Q2-check the dimensions of square and rectangle.

l=[]
a=int(input("Enter the length of shape=")) 
b=int(input("Enter the width of shape=")) 
c=int(input("Enter the length of shape=")) 
d=int(input("Enter the width of shape="))
l.append(a)
l.append(b)
l.append(c)
l.append(d)
print("Required demension of shape=",l)
if l[0]==l[1]==l[2]==l[3]:
 print("It's a square")
elif l[0]==l[2] and l[1]==l[3]:
 print("It's a rectangle")
else:
 print("neither square nor rectangle")
 
#Q3-Determine the oldest and youngest people.

a=int(input("Enter your age:-"))
print("age",a)
if a>0 and a<=5:
 print("You are baby")
elif a>5 and a<=40:
 print(" You are youngest in age ")
elif a>40 and a<=100:
 print("You are oldest in age ")
else:
 print(" wrong age entered")
 
#Q4-Write an if statement to let's competitor know which of these prizes they won.

prize1="Get an apple i6"
prize2="Get an SUV"
prize3="Trip to canada"
a=int(input("Enter your postion in competetion( 1,2,3):-"))
print("Position got=",a)
if a==1:
 print("you won prize1",prize1)
elif a==2:
 print("you won prize2",prize2)
elif a==3: 
 print("you won prize3",prize3)
else:
 ("you won no prize") 


#Q5-Print the total cost after getting discount.

price=int(input("Enter the price:-"))
print("price=",price)
dis=int(input("Enter the discount"))
print("discount=",dis)
discount=price * dis // 100
total=price-discount
print("total amount after discount=",total)
