from os import system
from math import factorial
import math

class VALORES (object):
    resultado = ""
    valor = 0.0
    k = 0.0

def menu():
    system("cls")
    print("Bienvenido al laboratorio 2")
    print("Integrantes: Wilson Caxaj y Nicol Macario")
    print("opciones:")
    print("1) Poisson")
    print("2) Binomial")
    print("3) Normal")
    seleccion = int(input("Seleccion: "))
    if seleccion == 1:
        poisson()

def poisson():
    resultadoslist = []
    system("cls")
    print("POISSON")
    print("a continuación deberas proporcionar los siguientes datos")
    E = float(input("e: "))
    U = float(input("U: "))
    K = float(input("K: "))
    resultadofloat = ((U**K)*(E**(U*-1)))/factorial(K)
    resultadoString = "P(x = "+str(K)+") = "+str(resultadofloat)
    valor =  VALORES()
    valor.valor = resultadofloat
    valor.resultado = resultadoString
    valor.k = K

    resultadoslist.append(valor)
    print(resultadoString)
    seleccion = 1
    while seleccion == 1:
        print("¿deseas agregar otro dato K?")
        print("1) SI")
        print("2) NO")
        seleccion = int(input("continuar: "))
        if seleccion == 1:
            K = float(input("K: "))
            resultado = ((U**K)*E**(U*-1))/factorial(K)
            resultadoString = "P(x = "+str(K)+") = "+str(resultado)

            valor =  VALORES()
            valor.valor = resultadofloat
            valor.resultado = resultadoString
            valor.k = K

            resultadoslist.append(valor)
            print(resultadoString)
        if seleccion == 2:
            print("---Resultados---")
            for x in range(len(resultadoslist)):
                print(resultadoslist[x].resultado+"  "+str(resultadoslist[x].valor))

menu()    