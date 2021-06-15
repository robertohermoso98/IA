import numpy as np
import pandas as pa
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
x_train,x_test,y_train,y_test=train_test_split(datos,etiquetas)
# ahora debemos de hacer la red neuronal
# para ello utlizaremos alguna libreria que nos ayude con el proceso
#

from sklearn import linear_model
algoritmo= linear_model.LinearRegression()
algoritmo.fit(x_train, y_train)
result=algoritmo.predict(x_test)


tasaFallo=0
for i in range(34):
    r= result[i]
    v=y_test[i]
    print('Resultado '+str(result[i])+' Valor real '+str(y_test[i]))
    if r>v:
        val=r-v
    else:
        val=v-r
    tasaFallo=tasaFallo+val
print(tasaFallo/34)

print(algoritmo.score(x_train,y_train))

print(algoritmo.coef_)
print(algoritmo.intercept_)
