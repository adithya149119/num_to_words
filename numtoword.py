# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:11:29 2020

@author: astrobout
"""
a = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
b = {'0':'ten','1':'eleven','2':'twelve','3':'thirteen','4':'fourteen','5':'fifteen','6':'sixteen','7':'seventeen','8':'eighteen','9':'ninenteen'}
c = {'2':'twenty','3':'thirty','4':'fourty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninty'}

x=input("enter")
y=list(x)
s=len(y)
while s<7:
    y.insert(0,'0')
    s=len(y)
z=y.copy()
y.reverse()
st=''
for i in range(0,s):
    if i == 0:
        if y[i+1]=='1':
            st=' '+b[y[i]]+st
        else:
            if y[i] != '0':
                st=' '+a[y[i]]+st+' '
    elif i == 1:
        if y[i]!='1' and y[i]!='0':
            st=c[y[i]]+st+' '
    elif i == 2:
        if y[i] != '0':
            st= a[y[i]]+" hundred "+st
    elif i == 3:
        if y[i+1]=='1':
            st=' '+b[y[i]]+' thousand '+st
        else:
            if y[i] != '0':
                st = a[y[i]]+" thousand "+st
            if y[i] ==  '0':
                if y[i+1] != '0':
                    st = ' thousand '+st
    elif i == 4:
        if y[i] != '0' and y[i]!='1':
            st = c[y[i]]+st
    elif i == 5:
        if y[i+1]=='1':
            st=' '+b[y[i]]+' lakh '+st
        else:
            if y[i] != '0':
                st = a[y[i]]+" lakh "+st
            if y[i] ==  '0':
                if y[i+1] != '0':
                    st = ' lakh '+st
    elif i == 6:
        if y[i] != '0' and y[i] != '1':
            st = c[y[i]]+st

print(st)
            
        
    
