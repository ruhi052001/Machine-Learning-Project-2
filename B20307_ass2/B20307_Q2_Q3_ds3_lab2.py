# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 16:31:00 2021

@author: priyanka kumari
"""

import pandas as pd

df= pd.read_csv('landslide_data3_miss.csv')

# Q2 (a)
print("Q2 (a)")
df2= df.dropna(subset=["stationid"])  
print("old data frame length: ",len(df))
print(df.head())
print("after deleting tuples having missing values: ")
print()
print("new data frame length: ",len(df2))
print(df2.head())

print()
print("The total number of deleted rows are",len(df)-len(df2))
print()

# Q2 (b)

print("Q2 (b)")

#df3=df2[df2.isnull().sum(axis=1)<=3]
df3=df.dropna(thresh=8)
print(df3.head())
print("The total number of rows having equal to or more than one third of attributes with missing values is",len(df2)-len(df3))
print()

# Q3
print("Q3")
print()
print("The number of missing values in each attributes are as follows")
print(df3.isnull().sum(axis=0))
print()
print("The total number of missing values after the deletion of rows are",df3.isnull().sum(axis=0).sum())

