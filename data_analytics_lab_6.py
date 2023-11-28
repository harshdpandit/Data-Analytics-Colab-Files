# -*- coding: utf-8 -*-
"""Data Analytics Lab 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Th_CZjGmeb1PRReZd8b7LVi_atldDCPu
"""

import pandas as pd
#importing all relevant libraries

data={'Name':['Harsh','Orange','Banana','Sarvesh','Chihuahua','Mumbai'],'Age':[12,13,23,34,45,67],'Gender':['M','N','N','M','F','N'],'Marks':[69,21,'NaN',52,85,21]}
df=pd.DataFrame(data)#converting the dictionary into dataframe
print(df)

df['Name']

c= avg = 0;
for ele in df['Marks']:
  if str(ele).isnumeric(): #checks whether the datatype is numeric or not
    c+=1 #for counting numeric values
    avg+=ele #for sum of numeric values
avg/=c #fpr calculating the average

df=df.replace(to_replace='NaN',value=avg)
df

df['Gender']=df['Gender'].map({'M':0,'F':1,'N':0}).astype(float)
#map helps us to replace the existing values with new values
#we use astype to change the data type
print(df)

df=df[df['Marks']>60]
df.drop('Age',axis=1)
print(df)

details=pd.DataFrame({'Id':[101,102,103,104,105,106,107,108,109,110],'Name':['Harsh','Praveen','Prakash','Sandeep','Santosh','Jagdeep','Manish','Rajesh','Pankaj','Yash']
                      ,'Branch':['CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE',]
})
print(details)

fee_status=pd.DataFrame({'Id':[101,102,103,104,105,106,107,108,109,110],'Pending':["Nil",1000,2000,3400,3200,1000,4500,3456,1232,3478]
                      ,'Branch':['CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE',]
})
print(fee_status)

fee_status=pd.DataFrame({'Id':[101,102,103,104,105,106,107,108,109,110],'Pending':["Nil",1000,2000,3400,3200,1000,4500,3456,1232,3478]
                      ,'Branch':['CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE',]
})


details=pd.DataFrame({'Id':[101,102,103,104,105,106,107,108,109,110],'Name':['Harsh','Praveen','Prakash','Sandeep','Santosh','Jagdeep','Manish','Rajesh','Pankaj','Yash']
                      ,'Branch':['CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE','CSE',]
})

new_data=pd.merge(details,fee_status, on='Id') #merging data based on Id
print(new_data)

car_selling_data={'Brand':['Maruti','Maruti','Maruti','Maruti','Hyundai','Hyundai','Toyota','Mahindra','Mahindra','Ford','Toyota','Ford'],
                  'Year':[2010,2011,2009,2013,2010,2011,2010,2013,2010,2011,2010,2011],
                  'Sold':[4,5,6,7,8,9,1,2,3,1,2,3]}
df=pd.DataFrame(car_selling_data)
grouped=df.groupby('Year') #groups the data according to year
print(grouped.get_group(2010)) #prints values in a group

print(df[df['Year']==2010])

non_duplicate=df[-df.duplicated('Year')] #df.duplicate takes all the duplicate values
# the - sign ensures that the duplicate value sare eliminated
print(non_duplicate)

#program to convert list into series
#program to convert dictionary  into dataframe



###########################################
#convert 2d list into dataframe

lst=[[123,211],[234,302],[322,411]]
df=pd.DataFrame(lst)
print(df)

#convert string into uppecase

string='Hi I am Harsh. How are you doing'
print(string.upper()) if len(string)>5 else print('Not enough length')

