arreglo=[1,2,3,4,5,6,7]
print(arreglo)
arreglo.append(8) #append agrega un elemento a la ultima lista
print (arreglo)
print("------------------------------------")
arreglo.append(8)
print ("Cuantas veces aparece '8': ",arreglo.count(8))
#count("elemento que pedimos") cuenta cantidad de elementos en la lista
print("-------------------------------------")
arreglo.extend([10])#extend puede agregar un arreglo dentro de este
print(arreglo)#es como concatenar dos arreglos, unirlos
print("--------------------------------------")
for i in range(len("Braian")):#len() devuelve cantidad de letras
    print(i,end="-")
print("--------------------------------------") 
for i in range(len(arreglo)): #0<7 tambien la cantidad de elementos
    print ("Arreglo[",i,"] = ",arreglo[i])
print("--------------------------------------")
print("El elemento 3 está en la pos: ",arreglo.index(3))
#INDEX() lo que hace es que el primer elemento que se busca, imprime su
#posicion, sino escuentra muestra value Error
print("--------------------------------------")
arreglo.insert(0,0.1)#Inserta un numero en la pos y lo mueve a la derecha
# INSERT(POSICION A CAMBIAR,ELEMENTO)
print(arreglo)
print("--------------------------------------")
arreglo.pop()#POP Remueve el ultimo elemento y lo puede guardar en una
 #variable, tambien puede ponerle la pos que quiere remover:arreglo.pop(2)
print(arreglo)
print("--------------------------------------")
arreglo.remove(8)#Remueve el primer elemento que encuentra que se así
print (arreglo)#Se eliminó el 8, sino lo encuentra entonces ValueError
print("--------------------------------------")
arreglo.reverse()#Ordena de mayor a menor
print(arreglo)
print("--------------------------------------")
arreglo.sort()#SORT ordena de menor a mayor
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
