# Exercício 26: Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

# Variáveis globais
NUM1 = 0
NUM2 = 0

# Verificar se são múltiplos
def multiplo():
    global NUM1, NUM2

    if NUM1 > NUM2:
        maior = NUM1
        menor = NUM2
    else:
        maior = NUM2
        menor = NUM1

    print("--- Verificando se são múltiplos ---")

    if maior % menor == 0:
        print(f"O número {maior} É múltiplo de {menor} \U0001F4DF")
    else:
        print(f"O número {maior} NÃO é múltiplo de {menor} \u274C")

def main():
    global NUM1, NUM2

    print("Exercício 26: Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.")

    NUM1 = int(input("Digite um número inteiro: "))
    NUM2 = int(input("Digite outro número inteiro: "))

    if NUM1 == 0 or NUM2 == 0:
        print("\u274C Nenhum número pode ser igual a 0, tente de novo.")
    else:
        multiplo()

if __name__ == "__main__":
    main()