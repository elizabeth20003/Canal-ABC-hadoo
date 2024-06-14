el comando que se ejecuta en la maquina virtual es el siguiente 
comando: cat join2_gen*.txt | ./join2_mapperNH.py | sort | ./join2_reducerNH.py
este comando realiza una agregación de datos para sumar los espectadores de cada programa,
filtrando y procesando específicamente los programas del canal 'ABC'. En otras palabras, 
toma una serie de archivos de entrada, transforma los datos para resaltar la información del canal 'ABC',
los ordena y luego los reduce para obtener una suma total de espectadores por programa, 
eliminando duplicados y programas no pertenecientes a 'ABC'.
