from os import system
from math import factorial
import math

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
    resultado = ((U**K)*(E**(U*-1)))/factorial(K)
    resultadoString = "P(x = "+str(K)+") = "+str(resultado)
    resultadoslist.append(resultadoString)
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
            resultadoslist.append(resultadoString)
            print(resultadoString)
        if seleccion == 2:
            print(resultadoslist)

menu()    