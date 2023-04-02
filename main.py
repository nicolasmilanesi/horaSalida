import time

# Hora de salida: 7 pm (19:00)
hora_salida = 19

# Obtiene la hora actual
hora_actual = time.localtime().tm_hour

# Comprueba si es la hora de ir a casa
if hora_actual >= hora_salida:
    print("¡Es hora de ir a casa!")
else:
    # Calcula la cantidad de tiempo restante
    tiempo_restante = (hora_salida - hora_actual) * 60 - time.localtime().tm_min
    horas_restantes = tiempo_restante // 60
    minutos_restantes = tiempo_restante % 60
    print(f"Todavía quedan {horas_restantes} horas y {minutos_restantes} minutos para ir a casa.")

