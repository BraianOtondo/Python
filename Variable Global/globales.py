# Define función
km = 10
def acelerar():
    # Declara la variable 'km' como global
    # Ahora se podrá utilizar dentro de la función
    global km
    
    
    km+= 5




acelerar()
# Muestra variable 'km'
print('Velocidad:', km)  # velocidad: 15
