# ASSIGNMENT-15 (REGULAR EXPRESSIONS)

#Q.1- Extract the user id, domain name and suffix from the following email addresses.
#     emails = "zuck26@facebook.com" "page33@google.com"jeff42@amazon.com"
#     desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]


import re
emails="zuck26@facebook.com page33@google.com  jeff42@amazon.com"
p=re.compile(r"(.*)@(.*).(...) (.*)@(.*).(...) (.*)@(.*).(...)")
result=p.match(emails)
#s=(r"([a-zA-Z0-9])@([A-Za-z])\.(com|org|in|edu)")
s1=tuple([result.group(1),result.group(2),result.group(3)])
s2=tuple([result.group(4),result.group(5),result.group(6)])
s3=tuple([result.group(7),result.group(8),result.group(9)])
l=[]
l.append(s1)
l.append(s2)
l.append(s3)
print(l)

#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#     text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter,
#     To make the bitter butter better."

text="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter,To make the bitter butter better."
p=re.compile(r"\b[bB]\w+")
result=p.findall(text)
l=[]
for i in result:
    l.append(i)
print(l)


# Q.3- Split the following irregular sentence into words
#      sentence = "A, very very; irregular_sentence"
#      desired_output = "A very very irregular sentence"

sentence = "A,very very;irregular_sentence"
p=re.sub(r"(,|;|_)"," ",sentence)
print(p)



#OPTIONAL QUESTION

#Q.1- Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
#desired_output = 'Good advice What I would do differently if I was learning to code today'

tweet='''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
r=re.sub(r"https?://[a-zA-Z]\.[A-Za-z0-9]+/[a-zA-Z0-9]+","",tweet)
p=re.sub(r"!|@\w+:|#\w+|@\w+|[A-Za-z][A-Za-z]:|RT","",r)
print(p)