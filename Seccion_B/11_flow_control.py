

# flow control

age = int(input("Introduce tu edad: "))
if age < 0:
    print('Edad no puede ser negativa')
elif age <= 12:
    print('Eres un nene')
elif age <= 18:
    print('Eres un adolescente')
elif age <= 64:
    print('Eres un adulto')
else:
    print('Yaa estas chochito')