# -*- coding: utf-8 -*-
"""Data Analytics Lab 5 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/196-XvkEx8Kmxas7CnuzJUHOTM0u1TATo
"""

n=int(input())
if n%2==0:
  if n%4==0:
    print('No')
  else :
    print('Yes')
else:
  s=n//4
  n-=(4*s)
  print('No. of cars:',s)
  print('No. of bikes:',n//2)

n=int(input())
m=2
f=2
while(m<n):
  if n%m==0:
    f+=1
  m+=1
if f==2:
  print('Number is prime')
else:
  print('Number is not prime')

a=int(input())
b=int(input())
m=int(input())
if a<b:
  print(abs(b-a)) if abs(b-a)<abs(a+m-b) else print(abs(a+m-b))
else:
  print(abs(a-b)) if abs(a-b)<abs(b+m-a) else print(abs(b+m-a))

import numpy as np

arr=np.array([[1,2,3],[2,3,4]])
arr.shape

arr.reshape(3,2)

for x in np.nditer(arr):
  print(x)

np.array_split(arr,3)

