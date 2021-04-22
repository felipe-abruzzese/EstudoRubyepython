import math

input("Probabilidade de acerto no dados \nDigite qualquer tecla para continuar")
dMin = 1
qnt = int(input("Adicione a quantidade de dados:"))

for tipo in range(1, 5):
    print("Digite a para o Dado de 4 faces (d4)")
    print("Digite b para o Dado de 6 faces (d6)")
    print("Digite c para o Dado de 10 faces (d10)")
    print("Digite d para o Dado de 12 faces (d12)")
    print("Digite e para o Dado de 20 faces (d20)")
    tipo = str(input("Digite o tipo de dado: "))
    if tipo == "a":
        dMax = 4
        print("Dado de 4 faces")
        break
    elif tipo == "b":
        dMax = 6
        print("Dado de 6 faces")
        break
    elif tipo == "c":
        dMax = 10
        print("Dado de 10 faces")
        break
    elif tipo == "d":
        dMax = 12
        print("Dado de 12 faces")
        break
    elif tipo == "e":
        dMax = 20
        print("Dado de 20 faces")
        break
    else:
        print("digite outro valor")

vMin = dMin*qnt
vMax = dMax*qnt


for res in range(1,5):
    res = int(input("Digite o resultado esperado: "))
    if res > vMax:
        print("Valor impossível, digite outro valor")
    elif res < vMin:
        print("Valor impossível, digite outro valor")
    else:
        break

prob_p = 1/vMax


def combinacao(n, k): #combinação
    return (math.factorial(n))/(math.factorial(k)*math.factorial(n-k))

def dist_binomial(n, p, k, q):
    return combinacao(n, k)*(p**k)*(q**(n-k))

for prob in range(res,vMax):
    prob += dist_binomial(vMax-vMin,prob_p,res,1-prob_p)
    print ("A probabilidade é: " + str(prob))
