horas = eval(input("ingrese sus horas trabajadas: "))

if horas > 0 and horas < 10:
    sueldo = horas * 5
    print("Su sueldo es de: " ,sueldo)
elif horas >= 10 and horas <= 20:
    sueldo = horas * 10 
    print("Su sueldo es de: " ,sueldo)
elif horas > 20: 
    sueldo = horas * 15
    print("Su sueldo es de: " ,sueldo)
else:
    print("Pailas eso no es valido")
    
