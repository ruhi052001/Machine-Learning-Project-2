# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:37:15 2021

@author: priyanka kumari
"""

# Q 5
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df_miss=pd.DataFrame(pd.read_csv('landslide_data3_miss.csv'))
df_org=pd.DataFrame(pd.read_csv('landslide_data3_original.csv'))
df1=df_miss.drop(['dates','stationid'],axis=1)
df2=df_org.drop(['dates','stationid'],axis=1)
df3=df1.interpolate()


P=df3['rain']

plt.boxplot(P)
plt.show()

Q_1 = 0
Q_3 = 987.750000
IQR = Q_3 - Q_1
min_rain_percent = Q_1 - (1.5* IQR)
max_rain_percent = Q_3 + (1.5* IQR)
l=[]
ind=[]
a=0
for i in P:
    if i<=min_rain_percent:
        l.append(i)
        ind.append(a)
       
    elif i>=max_rain_percent:
        l.append(i)
        ind.append(a)
        
    a+=1
    
for j in ind:
    P[j]=P.median()
plt.boxplot(P)
plt.show()