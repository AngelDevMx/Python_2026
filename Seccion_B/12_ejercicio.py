
name = input("Dame tu nombre: ")
experience_years = int(input("Cuando años de experiencia tienes: "))
skills = [skill.strip() for skill in input("Escribe tus lenguajes de programacion: ").lower().split(",")]
#STRIP QUITA LOS ESPACIOS PARA EVITAR ERRORES
evaluate_skills = "python" in skills

result = ""

if evaluate_skills:
    if experience_years >= 3:
        result = "Candidato optimo"
    elif experience_years >=1:
        result = "Buen candidato"
    else:
        result = "Posible candidato"
else:
    result = "No apto"

print(f"El candidato {name.capitalize()} es {result}")
