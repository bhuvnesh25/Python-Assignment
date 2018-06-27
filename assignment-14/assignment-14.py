#ASSIGNMENT-14

#(FILE HANDLING)

#Q.1- Write a Python program to read last n lines of a file.

file = open("Bhuvnesh.txt",'r',encoding="utf8")
l= file.readlines()
file.close()
n = int(input("Enter number of last lines to be read: "))
print ("The last lines are: ")
while n > 0:
    print (l[-n])
    n=n-1


# # #Q.2- Write a Python program to count the frequency of words in a file.

from collections import Counter
def count(fname):
      with open(fname) as f:
          return Counter (f.read().split())

print("number of words in the file :",count("demo.txt"))


#
# # #Q.3- Write a Python program to copy the contents of a file to another file.
#
with open("geetika.txt","r",encoding="utf8") as f1:
   with open("test.txt", "w") as f2:
        for line in f1:
           f2.write(line)
#
#
# #Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
#
#
with open("demo1.txt") as fh1, open("demo2.txt",encoding="utf8") as fh2:
      for line1, line2 in zip(fh1, fh2):
           print(line1+line2)
#
#
# #Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
#
#
import random
with open("Acadview.txt", "w") as f:
    for i in range(10):
        line = str(random.randint(1, 100))
        f.writelines(line + '\n')
        print(line)

with open("Acadview.txt") as f1, open("Acad.txt", "w") as f2:
    lines = f1.read().splitlines()
    lines.sort()
    print(lines)
    for l in lines:
        f2.write(l)
        f2.write('\n')

