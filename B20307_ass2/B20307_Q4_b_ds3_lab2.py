# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:59:52 2021

@author: priyanka kumari
"""

# Q4

import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df_miss=pd.DataFrame(pd.read_csv('landslide_data3_miss.csv'))
df_org=pd.DataFrame(pd.read_csv('landslide_data3_original.csv'))
df1=df_miss.drop(['dates','stationid'],axis=1)
df2=df_org.drop(['dates','stationid'],axis=1)
df3=df1.interpolate()


# Q4 Part b (1)  
d={}
e={}
def cal(d,a): #function rd to store values of mean,mode,median,std in dictionary  
    for i in a:
        keys = i 
        values = [round(a[i].mean(),3),round(a[i].median(),3),round(a[i].mode()[0],3),round(a[i].std(),3)] # here i have taken values as integers
        d[keys] = values
    return d
cal(d,df3)
cal(e,df2)
x = pd.DataFrame(d,index=['mean_miss','median_miss','mode_miss','std_miss'])
y = pd.DataFrame(e,index=['mean_original','median_original','mode_original','std_original'])
print("Mean,Median,Mode,Std values of each attribute in missing values file:")
print(x)
print("Mean,Median,Mode,Std values of each attribute in original file:")
print()


# Q4 part b(2)
df_final=df2-df3
a=[]
b=[]
for j in df_final:
    sum=0
    for i in df_final[j]:
        sum=sum+i**2
    Na=df_miss[j].isnull().sum()
    a.append(j)
    b.append((sum/Na)**0.5)
    print("RMSE for:",j,":",(sum/Na)**0.5)
plt.figure(figsize=(8,5))   
plt.bar(a,b)  
plt.title("Plot for RMSE")
plt.show()     
