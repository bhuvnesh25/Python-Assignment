#CLASS 4
#ASSIGNMENT - PANDAS
#Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.

import pandas as pd
import numpy as np
data={'Name':["Bhuvnesh Kumar"],
     'Age':[19],
     'Email-id':["bhuvneshkumar2798@gmail.com"],
     'Phone-No':[8295464599]}
df=pd.DataFrame(data)
print(df)
df=df.append({'Name':"Geetika",'Age':20,'Email-id':"geetika2598@gmail.com",'Phone-No':8295689593},ignore_index=True)
print("\n",df)


#Q.2 - Download the dataset from this link ,
#      Click Here
#      Import the data and print the following :
#       a.) First 5 rows of Dataframe
#       b.) First 10 rows of the Dataframe
#       c.) find basic statistics on the particular dataset.
#       d.) Find the last 5 rows of the dataframe
#       e.) Extract the 2nd column and find basic statistics on it.

import pandas as p
df=p.read_csv("Weather.csv")

print("First 5 rows of Dataframe:-",df.head(5))
print("First 10 rows of the Dataframe:-",df[0:10])

print("find basic statistics on the particular dataset:-",df.describe())

print("Find the last 5 rows of the dataframe:-",df.tail(5))
p=df["Location"]
print("Extract the 2nd column and find basic statistics on it:-",p.describe())