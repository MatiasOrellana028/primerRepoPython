import sys

from paquete.funciones_matematicas import sumar, restar, multiplicar, dividir, potencia

if len(sys.argv)==3:
    primernumero= int(sys.argv[1])
    segundonumero= int(sys.argv[2])

    print(f"La suma de {primernumero} y {segundonumero} es {sumar(primernumero,segundonumero)}")

else:
    print("te equivocaste!")
