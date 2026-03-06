
#REGISTRO
# RECIBAS DE FORMA DINAMICA EL NOMBRE, EL ANO DE NACIMIENTO, CORREO Y PASSWORD

"""
    Nombre:
    Email:
    Tendras 55 anos en el 2050 
    Tu contraseña es: ****
    
"""

name = input("Dame tu nombre: ")
age = input("Año de nacimiento? ")
email = input("Tu email: ")
password = input("Tu password: ")

new_age = 2050 - int(age)
new_pass = len(password)

card = f"""
    Nombre: {name}
    Email:" {email}
    Tendras {new_age} en el 2050!
    Tu contraseña es: {'*' * new_pass}
"""

print(card)