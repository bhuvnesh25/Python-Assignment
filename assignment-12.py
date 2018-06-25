#ASSIGNMENT-12

#Let’s learn and practise concepts of API:
 
#Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).

#Access token is what is issued to the client once the client successfully authenticates itself 
#(using the consumer key & secret). This access token defines the privileges of the client 
#(what data the client can and cannot access). Now every time the client wants to access the end-user's data, 
#the access token secret is sent with the access token as a password (similar to the consumer secret)

#How to create your access token for any API :
#  step-1: create Twitter Account : twitter provide an API trough which we can create our application.
#  step_2: go to website app.Twitter.com
#      (a)create new application
#  step-3 requirement : 
# (a) consumer_key
# (b) consumer_secret
# (c) access_token
# (d) access_token_secret
# step -4. generate access token.
#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.

# C:\Users\SONY>nslookup youtube.com
# Server:  UnKnown
# Address:  192.168.43.1

# Non-authoritative answer:
# Name:    youtube.com
# Addresses:  2404:6800:4002:805::200e
          # 216.58.196.206


# C:\Users\SONY>nslookup google.com
# Server:  UnKnown
# Address:  192.168.43.1

# Non-authoritative answer:
# Name:    google.com
# Addresses:  2404:6800:4002:802::200e
          # 172.217.31.14


#Q.3- Using Tweepy library try to extract tweets from Twitter.

import tweepy

consumer_key='_______'#enter your specific consumer_key
consumer_secret='_______'#enter your specific consumer_secret

access_token='______'#enter your specific access_token

access_token_secret='_______'#enter your specific access_token_secret

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search('#NotWithOutMyDog',lang="en",count=10,tweet_mode="extended")

#print(tweets)
for tweet in tweets:
 print("----------------")
 print(tweet.full_text)
 print("----------------")

 #with user input................
 
 import tweepy
hastag=input("Enter your hastag:-")
n=int(input("How many top tweet you want:-"))
consumer_key='_______'#enter your specific consumer_key
consumer_secret='_______'#enter your specific consumer_secret

access_token='______'#enter your specific access_token

access_token_secret='_______'#enter your specific access_token_secret

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search(hastag,lang="en",count=n,tweet_mode="extended")

#print(tweets)
for tweet in tweets:
 print("----------------")
 print(tweet.full_text)
 print("----------------")
 
 
#Q.4- What is a difference between library and API . Figure it out with examples.

# Library
#
# As per simple English terminology – A library is a collection of sources of information and similar resources, made accessible to a defined community for reference or borrowing.
#
# Now put that definition in the Custom Software Development context – What will be the collection of information? And why will a developer use it for reference? The basic building block of any application is its “Code”, and there are certain functionalities that any programmer needs to use repeatedly – then why to code it every time for different applications? That’s where a ‘Library’ comes to a rescue – a chunk of pre-defined code (a collection) that you can call (use for reference) from your own code, to help you do things (similar functionality) more quickly/easily.
#
# example= NumPy , Scrapy-If you are involved in webscraping then this is a must have library for you. ,
#  wxPython- A gui toolkit for python
#


# API
#
# Unlike English, not everything in this ‘Library’ is accessible directly. There will be back-end code to support the front-end code which needs to be accessible to programmers for Custom Software Development. Now how do a programmer access this front-end code? Yeah, the API – the Interface to Library.
#
#
# An API (Application Programming Interface) are the functions/methods (the front-end code) in a library that you can call to ask it to do things for you – the interface to the library.
#
# In general terms, it is a set of clearly defined methods of communication between various software components. A good API makes it easier to develop a computer program by providing all the building blocks, which are then put together by the programmer.
#
# example= When used in the context of web development, an API is typically defined a set of specifications , such as Hypertext Transfer Protocol (HTTP) request messages, along with a definition of the structure of response messages, which is usually in an Extensible Markup Language (XML) or JavaScript Object Notation (JSON) format


