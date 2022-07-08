# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:32:28 2021

@author: priyanka kumari
"""

# Question 4
# Import libraries
# Question 4 Part a (1)
import pandas as pd
import matplotlib.pyplot as plt
df_org = pd.read_csv('landslide_data3_original.csv')
df_miss = pd.read_csv('landslide_data3_miss.csv')
df1 = df_miss.drop(['dates','stationid'],axis=1)
df2 = df_org.drop(['dates','stationid'],axis=1)
df3 = df_miss.fillna(df_miss.mean())
df4 = df3.drop(['dates','stationid'],axis=1)
df5 = df3.drop(['dates','stationid'],axis=1)
df6 = df5.interpolate()            
df7 = df_org.drop(['dates','stationid'],axis=1) 


d={}
e={}
# function cal to store values of mean,mode,median,std in dictionary
def cal(d,a):   
    for i in a:
        keys = i 
# here i have taken values as integers        
        values = [round(a[i].mean(),3),round(a[i].median(),3),round(a[i].mode()[0],3),round(a[i].std(),3)] 
        d[keys] = values
    return d
cal(d,df4)
cal(e,df7)
x = pd.DataFrame(d,index=['mean_miss','median_miss','mode_miss','std_miss'])
y = pd.DataFrame(e,index=['mean_original','median_original','mode_original','std_original'])
print("Mean,Median,Mode,Std values of each attribute in missing values file:")
print(x)
print("Mean,Median,Mode,Std values of each attribute in original file:")
print(y)


# Question 4 a part(2)
m=[]
n=[]
for i in df1: # i is the attribute
    a=0
    b=0
    rmse=0
    n.append(i)
    for j in df1[i].isnull(): 
        if (j==True):
            dif=(df2[i][b] - df1[i].mean())**2
            rmse=rmse+dif
            a=a+1
        b+=1
    print("rmse for",i,":",(rmse/a)**0.5)
    m.append((rmse/a)**0.5)
plt.figure(figsize=(8,5))   
plt.bar(n,m)
plt.title("plot of RMSE") 

plt.show()  

