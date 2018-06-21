#ASSIGNMENT-11

#Q.1- Create a class Animal as a base class and define method animal_attribute.
#Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
 def __init__(self,characteristics):
    self.characteristics=characteristics
 def animal_attribute(self):
   print("characteristic of tiger=",self.characteristics)
class Tiger(Animal):
 def display(self):
   print("Tiger is King of forest and being distinct from our earth soon ")
   print("So,save the tiger")   
ch=input("Enter Characteristic of Tiger:-")
t=Tiger(ch)
t.display()
t.animal_attribute()	
 
#Q.2- What will be the output of following code.

#class A:
#   def f(self):
#        return self.g()

#    def g(self):
#        return 'A'

#class B(A):
#    def g(self):
#        return 'B'

#a = A()
#b = B()
#print a.f(), b.f()
#print a.g(), b.g()

#Solution:-
#output:-       A B
#               A B
class A:
 def f(self):
  return self.g()

 def g(self):
  return 'A'

class B(A):
 def g(self):
  return 'B'

a = A()
b = B()
# In the previous program required brackets print() are missing.
print (a.f(), b.f())
print (a.g(), b.g())

#Q.3- Create a class Cop. Initialize its name, age , work experience and designation.
# Define methods to add, display and update the following details.
# Create another class Mission which extends the class Cop. Define method add_mission _details.
# Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.

class Cop:
 def __init__(self,name,age,work_exp,designation):
  self.name=name
  self.age=age
  self.work_exp=work_exp
  self.designation=designation
 def display(self):
  print("cop Name=",self.name)
  print("cop Age=",self.age)
  print("cop Work experience=",self.work_exp)
  print("cop Designation=",self.designation)
 def update(self,name,age,work_exp,designation):
  self.name=name
  self.age=age
  self.work_exp=work_exp
  self.designation=designation 
class Mission(Cop):
   t="To caught a Boss of Drug Mafia"
   g="To caught jewellery Theif" 
   def mission_details(self):
    print("Mission Details=",self.t,"\n",self.g)
n=input("Enter cop name:-")
a=int(input(" Enter cop age:-"))
w=input("Enter cop work experience:-")
d=input("Enter cop designation:-")
c=Mission(n,a,w,d)
c.display()
c.mission_details()
c.update(input("Enter cop name:-"),int(input(" Enter cop age:-")),input("Enter cop work experience:-"),input("Enter cop designation:-"))
c.display()
c.mission_details()	

#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area.
# Create class rectangle and square which inherits shape and access the method Area.

class Shape:
 def __init__(self,length,breadth):
  self.length=length
  self.breadth=breadth
 def area(self):
    print("area=",self.length*self.breadth)
class Rectangle(Shape):
  def area(self):
    print("Area of rectangle=",self.length*self.breadth)
class Square(Shape):	
  def area(self):
    print("Area of square=",self.length*self.breadth)
l=int(input("Enter length:-"))
b=int(input("Enter Breadth:-"))
if l!=b:
  r=Rectangle(l,b)
  r.area()
else:
  s=Square(l,b)
  s.area()  
 