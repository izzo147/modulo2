#Código Práctica 1

import sys #importa librería sys

numero = int(sys.argv[1]) + 1 #declara variable con la entrada de la terminal
#después del numero de entrada de la terminal le suma 1 para que tome el valor 
#completo cuando se haga la lista, por ejemplo sin esa suma al poner 9 solo tomaría 
#del 1 al 8 como valores, sin embargo al sumarle ya toma el valor completo al num deseado

def lista(numero): #se define la función donde se toma el número como argumento 
#en esta función se crea una lista vacía y agrega números emmpezando desde el 1
#hasta el valor de la variable número
    
    lis = [] #esta es la declaración de una lista vacía
    
    for i in range (1,numero): #ciclo for para determinar el rango de la lista
        lis.append(i) #esto agrega los numeros a la lista
    return lis #regresa el valor de la lista
    
def primo(n): #función para determinar cuando es número primo 
  for i in range(2,n): #aquí se empieza desde el número 2 ya que el 1 no nos interesa
    if (n%i) == 0: #si el residuo de la división es igual a cero, se termina el proceso
    #y regresa falso resultando en un valor no primo.
      return False
  return True
  
listaprimo = [] #aquí se guardan los valores primos en una lista
for i in range(1,numero): #ciclo for para rango entre 1 y número
    
    if primo(i): 
        listaprimo.append(i) #si el número fue primo en la función anterior se guarda aquí
        
print(lista(numero)) #imprime la lista con los números desde el 1 hasta el número ingresado     
print("Los números primos son",listaprimo) #imprime un String + la lista de los num que si son primos
        


    

    