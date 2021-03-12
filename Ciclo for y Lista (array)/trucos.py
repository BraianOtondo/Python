arreglo=[1,2,3,4,5,6,7]
arreglo2=["PEPE",2,4]
print(arreglo)
#append
arreglo.append(8) #append agrega un elemento a la ultima posicion de la lista
print (arreglo)
print("------------------------------------")
#count
print ("Cuantas veces aparece '8': ",arreglo.count(8))
"""count("elemento que pedimos") cuenta cantidad de elementos en la lista"""
print("-------------------------------------")
#extend
arreglo.extend(arreglo2)#extiende una lista agregando un iterable al final.
print(arreglo)#sirve para concatenar dos arreglos, unirlos
'''
Tambien podemos agregarle un elemento de esta manera
arreglo.extend([2])
Tambien podemos extenderlo de esta manera
array=[2,2,3,4]
array.extend(range(5,7)) 5 6 y 7 no lo cuenta
print array
[2, 2, 3, 4, 5, 6] 5 y 6 son los nuevos

'''
print("----------------------------------------------")
#len
'''len() devuelve cantidad de letras e elementos'''
for i in range(len("Braian")):
    print(i,end="-")
print("---------------------------------------------")
#index
print("El elemento 3 está en la pos: ",arreglo.index(3))
'''lo que hace es que el primer elemento que se busca, imprime su
posicion, sino escuentra muestra value Error'''
print("--------------------------------------")
#insert
arreglo.insert(0,0.1)
'''Inserta un elemento en la pos y lo mueve a la derecha
INSERT(POSICION A CAMBIAR,ELEMENTO)'''
print(arreglo)
print("--------------------------------------")
#pop
arreglo.pop()
'''Saca el ultimo elemento y lo puede guardar en una 
variable. ejemplo ward=arreglo.pop()
Tambien puede ponerle la pos que quiere remover:arreglo.pop(2)'''
print(arreglo)
print("--------------------------------------")
#remove
arreglo.remove(8)
print (arreglo)
'''Se le puede poner el valor a eliminar arreglo.remove(2),sino 
lo encuentra entonces ValueError'''
arreglo.remove("PEPE")
print("--------------------------------------")
#reverse
arreglo.reverse() 
'''Invierte los valores de la lista, al revez'''
print(arreglo)
print("--------------------------------------")
#sort
arreglo.sort() 
'''SORT ordena de menor a mayor, solo
 tiene que tener numeros o palabras la lista o imprimirá error'''
print(arreglo)
print("--------------------------------------")
lista=list(range(5)) #LIST() crea una lista con un rango
print(lista)
print("--------------------------------------")
paises=["Chile","Argentina","Perú","Rusia"]
print(paises)
paisesString=','.join(paises)#JOIN convierte una lista en un string
#agregandole un separador 
print(paisesString)
print("---------------------------------------")
paisesLista=paisesString.split()
print(paisesLista)#SPLIT() transforma una cadena en lista por cada espacio
print("------------------------------------")
#max
print("El maximo del arreglo es ",max(arreglo))
'''
Busca el numero mas mayor de la lista
'''
#min
'''
Busca el numero mas menor de la lista
'''
print("El maximo del arreglo es ",min(arreglo))
print("------------------------------------")
for i in range(len(arreglo)):
    print ("Arreglo[",i,"] = ",arreglo[i])

print("------------------------------------")
''' CONCATENAR'''
print(arreglo +[1,1,1,10])
print("-----------------------------------")
print(arreglo *2) 
''' Al ponerle un signo de multiplicacion, multiplicamos los elementos de 
la lista'''
print("-----------------------------------------")
print(0.1 in arreglo) 
''' Si existe ese elemento en la lista inprime true '''