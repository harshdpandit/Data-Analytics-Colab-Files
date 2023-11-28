# -*- coding: utf-8 -*-
"""Data Analytics 11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_8-sD4oL2jJ6KZvPQFMuD7S6sD7XS6i7
"""

import pandas as pd

import statistics

d={'Name':pd.Series(['Harsh','DV','Tom']),'Age':pd.Series([25,21,23]),'Rating':pd.Series([4,2,1])}

df=pd.DataFrame(d)

print(df.std())

print(df.skew())

li=[1.2,2,3,8,9,3,4,7]

print('The population variance of data is: {}'.format(statistics.pvariance(li)))

print('The variance of data is: {}'.format(statistics.variance(li)))

