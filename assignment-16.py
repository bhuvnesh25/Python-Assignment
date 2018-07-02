
# ASSIGNMENT-16

# DATABASES IN PYTHON

import pymysql


# Q.1- Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors


db=pymysql.connect("localhost",'root','root','Library')
point=db.cursor()
for i in range(0,6):
 try:

   cmd=input("enter SQL Querry to create table:-")
   point.execute(cmd)
   db.commit()
 except:
    db.rollback()
db.close()

#output:-mysql> show tables;
#       +-------------------+
#       | Tables_in_library |
#       +-------------------+
#       | authors           |
#       | authorstitles     |
#       | book              |
#       | publishers        |
#       | titles            |
#       | zipcodes          |
#       +-------------------+
#       6 rows in set (0.00 sec)


# Q.2- Insert values in the tables.

db=pymysql.connect("localhost",'root','root','Library')
point=db.cursor()
for i in range(0,6):
 try:
   cmd=input("enter SQL Querry to insert values in created table:-")
   point.execute(cmd)
   db.commit()
 except:
    db.rollback()
db.close()

#output:-

# mysql> select * from book;
# +------+
# | name |
# +------+
# | java |
# | C++  |
# +------+
# 2 rows in set (0.00 sec)
#
# mysql> select * from titles;
# +--------------+
# | names        |
# +--------------+
# | play java    |
# | play classes |
# +--------------+
# 2 rows in set (0.00 sec)
#
# mysql> select * from publishers;
# +------------------+
# | name             |
# +------------------+
# | jai ma pulishers |
# | bharat publish   |
# +------------------+
# 2 rows in set (0.00 sec)
#
# mysql> select * from zipcodes;
# +----------+
# | name     |
# +----------+
# | abdtjg   |
# | bhdrysoo |
# +----------+
# 2 rows in set (0.00 sec)
#
# mysql> select * from authorstitles;
# +-----------+
# | name      |
# +-----------+
# | play java |
# | play oops |
# +-----------+
# 2 rows in set (0.00 sec)
#
# mysql> select * from authors;
# +--------------+
# | name         |
# +--------------+
# | hary         |
# | bala goswami |
# +--------------+
# 2 rows in set (0.00 sec)



# Q.3- Update any values in any of the tables. Print the original and updated values.

db=pymysql.connect("localhost",'root','root','Library')
point=db.cursor()
for i in range(0,6):
 try:
   cmd=input("enter SQL Querry to update values in created table:-")
   point.execute(cmd)
   db.commit()
 except:
    db.rollback()
db.close()

#output:-
# mysql> select * from book;
# +------+
# | name |
# +------+
# | java |
# | C++  |
# +------+
# 2 rows in set (0.00 sec)

#  updated:-
# mysql> select * from book;
# +----------+
# | name     |
# +----------+
# | database |
# | C++      |
# +----------+
# 2 rows in set (0.00 sec)