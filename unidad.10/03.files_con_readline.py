


# file: 02.xxxxxxxxxxx.py
import os
from os import strerror


try:
    contador_caracter = contador_linea = 0
    archivo = os.path.join(os.path.dirname(__file__), 'recursos', 'agenda.csv')
    stream = open(archivo, 'rt', encoding='utf-8')
    
    linea = stream.readline()

    while linea != '':
        contador_linea += 1
        for caracter in linea:
            print(caracter, end='')
            contador_caracter += 1
        
        linea = stream.readline()
    
    stream.close()
    
    print("\n\n")
    print(f'Se leyeron {contador_caracter} caracteres.')
    print(f'Se leyeron {contador_linea} líneas del archivo {archivo}')

except IOError as e:
    print(f'Error: {strerror(e.errno)}')


