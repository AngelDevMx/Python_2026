

# Evaluar condiciones

# AND Evalua si dos o mas condiciones son verdaderas
print("AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# OR al menos un valor debe ser positivo
print("OR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# NOT
print("NOT")
print(not True)
print(not False)

print("Ejemplo")

age = 25
is_licensed = True

if age>= 18 and is_licensed:
    print("Estas grande y puedes manejar")

is_student = False
memebership = True

if is_student or memebership:
    print("Tienes un desceunto especial")

is_admin=False

if not is_admin:
    print("Acceso denegado")