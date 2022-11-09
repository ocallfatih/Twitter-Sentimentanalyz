import pandas as pd
import re
import csv
# To read a CSV file
# with open('sentences.csv','r') as df:
with open('sentences.csv', mode='r',encoding="utf-8") as df:
    with open('sentences.csv') as f:
    #  mylist = []
     mylist = list(f)
    #  f.close()
     print("--------------")

     
     print(mylist)
     print("--------------")
#df = pd.read_csv('sentences.csv')
# df = pd.DataFrame(mylist)
df=pd.DataFrame({
    'id':[1,2,3,4,5],
    'name':['Jeremy','Frank','Janet','Ryan','Mary'],
    'age':[20,25,15,10,30],
    'income':[4000,7000,200,0,10000]
})
df['age']=df.apply(lambda x: x['age']+3,axis=1)

from textblob import TextBlob

# The x in the lambda function is a row (because I set axis=1)
# Apply iterates the function accross the dataframe's rows

df['polarity'] = df.apply(lambda x: TextBlob(str(mylist)).sentiment.polarity, axis=1)
df['subjectivity'] = df.apply(lambda x: TextBlob(str(mylist)).sentiment.subjectivity, axis=1)
print(df['polarity'])
 

print(df)
