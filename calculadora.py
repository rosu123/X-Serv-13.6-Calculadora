#!/usr/bin/python3


import sys
from sys import argv


def sum(numero1, numero2):
    return numero1 + numero2


def res(numero1, numero2):
    return numero1 - numero2


def mult(numero1, numero2):
    return numero1 * numero2


def div(numero1, numero2):
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        sys.exit("Error: division por cero")


if len(sys.argv) != 4:
    sys.exit("Numero argumentos invalido")

funcion = argv[1]
try:
    operando1 = float(argv[2])
    operando2 = float(argv[3])
except ValueError:
    sys.exit("Argumentos invalidos")

    
if funcion == "sumar":
    print(sum(operando1, operando2))
elif funcion == "restar":
    print(res(operando1, operando2))
elif funcion == "multiplicar":
    print(mult(operando1, operando2))
elif funcion == "dividir":
    print(div(operando1, operando2))
else:
    sys.exit("Operacion invalida")
