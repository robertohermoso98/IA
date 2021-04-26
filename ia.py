import numpy as np
import pandas as pa
#import keras as kr
#import tensorflow as ts
from sklearn.model_selection import train_test_split 
# calunalmos la canitdad de datos que nos proporcionan
tam=0
fichero = open("datosBien.txt")
for i in fichero:
    tam=tam+1
# guardamos los datos y las etiquestas en el vector de caracteristicas
fichero = open("datosBien.txt")
array=np.empty([tam+1,14])
fila=0;
for i in fichero:
    dat=i.rstrip().split(" ")
    columna=0
    for e in dat:
        if e!="":
            array[fila][columna]=float(e)
            columna=columna+1
    fila=fila+1
# probamos que los vectores de caracteristicas estan correctos   
# print(array[0])
# print(array[tam-1])
# ahora ya estan todos los datos en el array
# lo siegiente es separar los datos en los conjuntos para las pruebas y test
# y las etiquetas para ello separamos las etiquetas de los datos


datos=np.empty([tam+1,13])
etiquetas=np.empty([tam+1,1])
indice=0
for i in array:
   datos[indice]=array[indice][0:13]
   etiquetas[indice]=array[indice][13]
   indice=indice+1
# ya estan los datos en los dos arrays ahora se les separa en los conjuntos
xtrain,xtest,ytrain,ytest=train_test_split(datos,etiquetas)
# ahora debemos de hacer la red neuronal
# para ello utlizaremos alguna libreria que nos ayude con el proceso
