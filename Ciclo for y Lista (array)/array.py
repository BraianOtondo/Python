arreglo2=[2,5,"Pepe",False,"Domingo"]
print(arreglo2,type(arreglo2))#TYPE imprime l tipo de dato es: lista
guardado=arreglo2[2] #guardar un elemento de la lista
print(guardado)#Imprime ese elemento de la lista: FALSE
print("---------------------------------------")
arreglo=[1,2,3,4,5,6,7]
for i in arreglo:#desde 0 hasta terminar de imprimir el arreglo
    print ("-",i)
print("---------------------------------------")
print(arreglo[-1])#Imprime el ultimo elemento con -1
print("---------------------------------------")
print(arreglo2[-len(arreglo2)])#-4 IMprime el primer elemento
#con el la cantidad de elementos menos se imprime el primero
#arreglo[-4]=PRIMER ELEMENTO
print("--------------------------------")
listaDoble=[1,2,3,5,6]
listaSimple=["Maria",2,False,listaDoble]
print(listaSimple[3][1])