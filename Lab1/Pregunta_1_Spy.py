
#Importación de la librería Numpy y Random para la creación de un Vector con valores aleatorios.
import random 
import numpy as np

#Creación del Vector con números aleatorios 

#Primero se crea una lista para crear los valores requeridos para el Vector
Lista = random.sample(range(0,500),20)      #Se asigna que la lista saque un total de 20 números aleatorios enteros entre 0 y 500.
Lista.sort()                                #Se ordenan los valores para que estén de menor a mayor.


Vector = np.array(Lista)                    #Se pasan los valores de la lista hacia el Vector y indica que se imprima con su respectivo nombre.
print('Vector =', Vector) 

#Creación de la "if statement":
for index, i in enumerate(Lista):           #Se indica que cada valor de la lista se reemplazará dependiendo de en que rango se encuentre.
    
    if i > 0 and i <= 100:                  #Rangos que los valores seguirán para reemplazarse por otro. 
        Lista[index] = i**0.5               #Se indica que se reemplacen los valores transformados en la lista .
        
    if i > 100 and i <= 300:
        Lista[index] = i-5    
        
    if i > 300:
        Lista[index] = 50 

Resultado = np.array(Lista)                 #Se pasan los nuevos valores de la lista hacia el vector "Resultados" y indica que se imprima con su respectivo nombre.
print('Resultado =', Resultado)             #Se indica que se muestre el Vector resultados con su respectivo nombre.
