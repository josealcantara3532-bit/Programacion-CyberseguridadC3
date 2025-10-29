import datetime

ahora = datetime.datetime.now()
print("Fecha y hora actual: ", ahora)

fecha_especifica = datetime.datetime(2025, 10, 28, 19, 50)
print("Fecha y hora específica: ", fecha_especifica.strftime ("%Y-%m-%d %H:%M:%S"))

