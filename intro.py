# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 12:24:40 2018

@author: INF-322
"""

vector=[1,2,3,4,5,6,7,8,9,10,11,12]
print(vector)
print(vector[:2])
print(vector[2:])

matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz)

print ("la matriz:")
matrizej = [vector[:3]]
print(matrizej)

print("la matriz 2")
fila =3
col=4
matriz2 =[vector[col*i : col*(i+1)] for i in range (fila)]
print(matriz2)

#funciones

def suma(a,b):
    return a+b;

def multli(a,b):
    multi=0
    for i in range(b):
        multi=multi+a
    return multi;

print("---------funcines--------")
print(suma(4,5))
print(multli(8,8))

print("cosas raras")        
print(sum(vector))


#vector.append(20)
print(vector)

print("numpy")

import numpy as np

matriznp1 = np.array(vector).reshape(3,4) # solo funciona con el tamaño correcto del array

print("-------------")
print(matriznp1)
print("-------------")
print(matriznp1.mean())
print("-------------")
print(matriznp1.mean(axis=0))
print("-------------")
print(matriznp1.mean(axis=1))
print("-------------")
print("-------------")
print(np.mean(matriznp1))
print("-------------")
print(np.mean(matriznp1,0))
print("-------------")
print(np.mean(matriznp1,1))
print("-------------")
print("-------------")
print(np.median(matriznp1))
print(np.median(matriznp1,0))
print(np.median(matriznp1,1))
print("-------------")
print("-------------")
print(np.std(matriznp1))
print(np.std(matriznp1,0))
print(np.std(matriznp1,1))
print("-------------")
print("-------------")
print(np.var(matriznp1))
print(np.var(matriznp1,0))
print(np.var(matriznp1,1))
print("-------------")
print("-------------")
print(np.corrcoef(matriznp1))
#print(np.corrcoef(matriznp1[0], np.corrcoef(matriznp1))
print(np.ones((3,4)))


