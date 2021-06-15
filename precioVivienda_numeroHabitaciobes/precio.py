import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

### importamos el dataset

boston = datasets.load_boston()
print(boston)
print()

######### entedemos la data 

print('Informacion del dataset')
print(boston.keys())
print()

print('Caracteristicas del dataset')
print(boston.DESCR)

print('Cantidad de datos')
print(boston.data.shape)

print('Nombres de las columnas')
print(boston.feature_names)

### preparamos los datos para el modelo de regresion linea simple
# la data va en la variable x cogeremos las columas 5 6 y 7
x = boston.data[:, 5:8]

# las etiquetas van el la variable y
y = boston.target

#plt.scatter(x,y)
#plt.xlabel('Numero de habitacioenes')
#plt.ylabel('Valor medio')
#plt.show()

### implementacion del modelo de regresion linela simple

from sklearn.model_selection import train_test_split
# separamos los datos en entremiento y prueba 
# usaremos el 20% de los datos para los test por esos test_size=0.2 
x_train, x_test, y_train, y_test= train_test_split(x,y, test_size=0.2)

# definimos el algoritmo que vamos a utilizar 
lr = linear_model.LinearRegression()

# entrenamos al modelo 
lr.fit(x_train,y_train)

# realizamos la prediccion del modelo
y_pred = lr.predict(x_test)

for i in range(y_pred.size):
    print(str(y_test[i])+' vs '+str(y_pred[i]))

print()
print('Predicion del modelo')
print(lr.score(x_train,y_train))





