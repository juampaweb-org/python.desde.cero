


# file: 02.xxxxxxxxxxx.py

from os import strerror

try:
    contador = 0
    archivo = 'recursos/agenda.csv'
    stream = open(archivo, 'rt', encoding='utf-8')
    caracter = stream.read(1)

    while caracter != '':
        print(caracter, end='')
        caracter = stream.read(1)
        contador += 1
    
    stream.close()
    print(f'\n\nSe leyeron {contador} caracteres del archivo {archivo}')

except IOError as e:
    print(f'Error: {strerror(e.errno)}')


