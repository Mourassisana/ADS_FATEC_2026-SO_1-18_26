# Receba dois valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor.

# Variáveis globais
VAL_1 = 0
VAL_2 = 0
DIF = 0

#procedimento sem retorno e sem parâmetro
def calcular_dif():
    global VAL_1, VAL_2, DIF

    if VAL_1 > VAL_2:
        DIF = VAL_1 - VAL_2
    else:
        DIF = VAL_2 - VAL_1

    print("\n--- Resultado ---")
    print(f"O resultado calculado é: {DIF}")

#Função Principal
def main():
    global VAL_1, VAL_2

    print("Exercício 18: Receba dois valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor.")
    VAL_1 = int(input("Digite o primeiro valor: "))
    VAL_2 = int(input("Digite o segundo valor: "))
    calcular_dif()

#Iniciaização
if __name__ == "__main__":
    main()