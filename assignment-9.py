# Class and Modules -1

# QUESTION: 1  
# Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

class circle:
 def __init__(self,r):
  self.r=r
 def radius(self):
  print("Radius=",self.r) 
 def area(self):
  print("Area of circle=",self.r**2 * 3.14 )
 def circumference(self):
  print("Circumference of circle=",self.r*2*3.14)
r=int(input("Enter radius:-"))  
radius=circle(r)
radius.radius()
radius.area()
radius.circumference() 

# QUESTION: 2  
# Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all informations of the student.

class student:
 def __init__(self,name,roll_no):
  self.name=name
  self.roll_no=roll_no
 def display(self):
  print("Name=",self.name)
  print("Roll_No=",self.roll_no)
n=input("Enter your name:-")
r=int(input("Enter your roll_no:-"))  
s=student(n,r)
s.display()

# QUESTION: 3  
# Q.3- Create a Temprature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class temperature:
 def __init__(self,tempc,tempf):
  self.tempc=tempc
  self.tempf=tempf
 def fahenheit(self):
  print("Temperature Celius to Fahrenheit=",(self.tempc*1.8)+32) 
 def celcius (self):
  print("Temperature Fahrenheit to celcius=",(self.tempf-32)*(5/9))
c=int(input("Enter temperature in celcius:-"))
f=int(input("Enter temperature in faherenheit:-"))
t=temperature(c,f)
t.fahenheit()
t.celcius()

#QUESTION: 4  
# Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to 
#1. Display-Display the details.
#2. Update- Update the movie details.

class movie:
 def __init__(self,name,artist,release,rating):
  self.name=name
  self.artist=artist
  self.release=release
  self.rating=rating
 def display(self):
  print("Movie name=",self.name)
  print("Artist name=",self.artist)
  print("Year of release=",self.release)
  print("Rating=",self.rating)
 def update(self,name,artist,release,rating):
  self.name=name
  self.artist=artist
  self.release=release
  self.rating=rating
   
   
n=input("enter movie name:-")
a=input("enter artist name:-")
y=int(input("year of release:-"))
r=int(input("rating between(1-5):-"))
m=movie(n,a,y,r)
m.display()
m.update(input("enter movie name:-"),input("enter artist name:-"),int(input("year of release:-")),int(input("rating between(1-5):-")))
m.display()

#QUESTION: 5  
#Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
#1. Display expenditure and savings 
#2. Calculate total salary
#3. Display salary

class expenditure:
 def __init__(self,exp,sav):
  self.exp=exp
  self.sav=sav
 def display(self):
  print("Expenditure=",self.exp)
  print("Savings=",self.sav)  
 def total_salary(self):
  print("Total salary=",self.exp+self.sav)
s=int(input("enter your saving:-")) 
e=int(input("enter your expenditure:-"))
x=expenditure(e,s)
x.display()
x.total_salary()
 
  
  