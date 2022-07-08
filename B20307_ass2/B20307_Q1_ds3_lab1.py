# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 16:08:51 2021

@author: priyanka kumari
"""
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('landslide_data3_miss.csv')

# attributes 

x= [1,2,3,4,5,6,7,8,9]  
 
# bar graph

plt.bar(x,df.isnull().sum()) 
 
# labelling xticks with column names

plt.xticks(x,list(df.columns),rotation=90)  
plt.xlabel('Attribute names')
plt.ylabel('Number of missing values')
