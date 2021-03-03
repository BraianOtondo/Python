def GetNombre(nombre):
    return "Tu nombre es: "+ nombre
def GetNumero():
    return numero**2
def Palabras(palabra,cantidad=4):
    print(cantidad*palabra)
nombre="Braian"
print(GetNombre(nombre))
print("-----------------------------")
numero=int(input("Ingrese numero para elevarlo al cuadrado: "))
resultado=GetNumero()
print("El numero elevado es : ",resultado)
print("-------------------------------")
Palabras("PEPE ") 
print("-------------------------------")
ItemsValibles=["ropa","calzado","perfumeria"]
def Validar(item):
    return item in ItemsValibles

print(Validar("fotos"))
