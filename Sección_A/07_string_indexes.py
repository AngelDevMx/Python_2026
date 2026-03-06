
name = 'Ricardo'
print(name)

print(name[0])
print(name[-1])
print(name[6])
print(name[5])

# [ Start:Stop] el stop no lo toma en cuenta

print(name[0:3])

# [ Start:Stop:Step over] EL step over default es 1
# R I C A R D O
print(name[0:6:2])

print(name[::2]) # Si no tiene start y stop toma todo el string y salta de 2 en 2

# Prueba de nuevo cambio


#Ejercicio voltea tu nombre
my_name = "Luis Angel"
print(my_name[::-1])