def gemelos(listaPrimo):
    listaGemelo = []
    for i in range(len(listaPrimo)-1):
        if listaPrimo[i]+2 == listaPrimo[i+1]:
            listaGemelo.append(listaPrimo[i])
    #print(f"los gemelos son {listaGemelo}")

def palindromos(listaPrimo):
    listaPalindromo = []
    for i in range(4,len(listaPrimo)):
        aux = str(listaPrimo[i])
        if listaPrimo[i] == int(aux[::-1]):
            listaPalindromo.append(listaPrimo[i])
   # print(f"los palindormos son {listaPalindromo}")

def calcularNumeroPrimo(lista):
    listaPrimo = []
    cont=0
    for i in lista:
        for j in range(2,int(i**0.5)+1):
           if i%j==0:
               cont+=1
        if cont <1:
            listaPrimo.append(i)
        cont=0
    gemelos(listaPrimo)
    palindromos(listaPrimo)
    print(listaPrimo)
        
def ingresarDatos():
    lista = []

    limite = int(input("Ingrese la el limite:"))

    for i in range(2, limite):
        lista.append(i)
        
    calcularNumeroPrimo(lista)
        
ingresarDatos()