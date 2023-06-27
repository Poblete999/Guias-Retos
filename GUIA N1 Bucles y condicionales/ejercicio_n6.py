#Ejercicio n°6
"Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos de un día desde las 00:00:00 horas hasta las 23:59:59 horas."

from time import sleep

for hora in range(0,12): 
    for minutos in range(0,60):
        for segundos in range(0,60):
            sleep(1)
            print("hrs",hora,":","min",minutos,":","seg",segundos)
    










