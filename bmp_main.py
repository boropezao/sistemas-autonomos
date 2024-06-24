import bmpsensor
import time 
while True:
    temp, pres, alt = bmpsensor.readBmp180()
    #Impresión de pantalla de la data obtenida para BMP180
    print("Temperatura = ", temp) 
    print("Presion = ", pres )
    print("Altitud = ", alt)   #De la variable alt se obtiene la data
    print("\n")
    time.sleep(0.8)  #Tiempo para que siga leyendo la data (actualización)
    