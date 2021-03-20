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

    if seleccion == 2:
        binomial()

    if seleccion == 3:
        normal()

def poisson():
    resultadoslist = []
    system("cls")
    print("POISSON")
    print("a continuación deberas proporcionar los siguientes datos")
    E = float(input("e: "))
    U = float(input("U: "))
    K = float(input("K: "))
    resultadofloat = ((U**K)*(E**(U*-1)))/factorial(K)
    resultadoString = "P(K = "+str(K)+") = "+str(resultadofloat)

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
            resultadofloat = ((U**K)*E**(U*-1))/factorial(K)
            resultadoString = "P(K = "+str(K)+") = "+str(resultadofloat)

            valor =  VALORES()
            valor.valor = resultadofloat
            valor.resultado = resultadoString
            valor.k = K

            resultadoslist.append(valor)

            print(resultadoString)
            
        if seleccion == 2:
            print("---Resultados---")
            porct = 0
            for x in range(len(resultadoslist)):
                porct+= resultadoslist[x].valor
                print(resultadoslist[x].resultado+" = "+"{:^10.8f}".format(resultadoslist[x].valor*100)+" %")
            print("en porcentaje: "+str("{:^10.8f}".format(float(porct*100)))+" %")
            print("1) SI\n2)NO, SALIR")
            seleccionmenu = int(input("quieres volver al menu?: ")) 
            if seleccionmenu == 1:
                menu()

def binomial():
    n = int(input("Digite número de ensayos: "))
    k = int(input("Digite número de exitos: "))
    p = float(input("Digite número probabilidad de exitos: "))

    q=1-p
    res=(factorial(n))/(factorial(k)*(factorial(n-k)))
    res2=pow(p,k)*(pow(q,(n-k)))
    resultado= (res*res2)*100
    print("El resultado es: " +(format(resultado,'.3f')+ "%"))
    print("1) SI\n2)NO, SALIR")
    seleccionmenu = int(input("¿quieres volver al menu?: ")) 
    if seleccionmenu == 1:
        menu()
    
def normal():
    system("cls")
    print("NORMAL")
    print("a continuación deberas proporcionar los siguientes datos")
    X = float(input("X: "))
    U = float(input("U: "))
    O = float(input("O: "))
    resultadofloat = (X-U)/O
    resultadoString = "Z = "+str(resultadofloat)


    print(resultadoString)
    print("1) SI\n2)NO, SALIR")
    seleccionmenu = int(input("¿quieres volver al menu?: ")) 
    if seleccionmenu == 1:
        menu()

menu()    