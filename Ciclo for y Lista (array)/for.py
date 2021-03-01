
for nombres in ["pepe","rodolfo","meme"]:#3 elementos 0<3
    print(nombres)
print("----------------------")
for i in [1,2,3,7]: # De 0<4 Porque son 4 elementos 
    print(i)
print("----------------------")
for i in [3,"Lolo",False]:#3 elementos 0<3
    print(i)
print("-----------------------")
for i in "Braian": #6 elementos string 0<6
    print ("Hola")
print("-----------------------")
for i in "Braian":
    print("Hola",end=" ")
print("-----------------------")
contar=0
for i in "Braian":#tambien se pudo poner una variable nombre cargada
    if(i=='a'):
        contar=contar+1
print(f"Tu nombre tiene: {contar} 'a' ")
print("-----------------------")
for i in range(5):
    print(f"i= {i}")
print("------------------------")
for i in range(5,10):#desde el 5<10
    print(i)
print("-------------------------------------")
for i in range(0,20,2):
    print(i)
print("--------------------------------------")
