#ASSIGNMENT-13

#EXCEPTION HANDLING

# Q.1- Name and handle the exception occured in the following program:

# a=3
#  if a<4:
#     a=a/(a-3)
#      print(a)


#Exception Ocuured:-division by zero
#Handle The Exception
a=3
if a<4:
 try:
  a=a/(a-3)
  print(a)
 except Exception:
   print("Exception occur")



# Q.2- Name and handle the exception occurred in the following program:
# l=[1,2,3]
# print(l[3])

#Exception Occured:-Index Error
l = [1, 2, 3]
try:
   print(l[3])
except Exception:
     print("Exception occur")

# Q.3 - What will be the output of the following code:
#
# # Program to depict Raising Exception
#
# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print
#     "An exception"
#     raise  # To determine whether the exception was raised or not


#Program to depict Raising Exception

# try:
#      raise NameError("Hi there")  # Raise Error
# except NameError:
#      print("An exception")
#      raise  # To determine whether the exception was raised or not

#output:-
#An exception
#   File "C:/Users/SONY/PycharmProjects/exceptionhandling/assignment-13.py", line 51, in <module>
#     raise NameError("Hi there")  # Raise Error
# NameError: Hi there



# Q.4 - What will be the output of the following code:
#
#
# # Function which returns a/b
# def AbyB(a, b):
#     try:
#         c = ((a + b) / (a - b))
#     except ZeroDivisionError:
#         print
#         "a/b result in 0"
#     else:
#         print
#         c
#
#
##Driver program to test above function
#AbyB(2.0, 3.0)
#AbyB(3.0, 3.0)


#Function which returns a/b
def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)



#Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#output:--5.0
#         a/b result in 0


# Q.5- Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error

try:
     import xyz
     print("hello world")
except Exception :
 print("ImportError occur")

try:
    name=int(input("Enter your name"))
except Exception:
    print("ValueError Occur")

try:
    l=[1,4,6]
    print(l[6])
except Exception:
    print("IndexError Occur")

#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
# The code must keep taking input till the user enters the appropriate age number(less than 18).



class AgeSmallError(Exception):
   pass


while True:
 try:
    age=int(input("Enter your age:-"))
    if age >18:
      raise AgeSmallError
    break
 except AgeSmallError:
                 print("the entered age is larger than 18")
                 print('')

print("you enter correct age")