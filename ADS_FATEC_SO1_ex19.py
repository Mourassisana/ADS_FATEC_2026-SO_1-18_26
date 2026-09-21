# Receba 2 valores reais. Cacule e mostre o maior deles.

# Variáveis globais
VALOR_1 = 0.0
VALOR_2 = 0.0
MAIOR = 0.0

# procedimento sem retorno e sem parâmetro
def MAIOR():
    global VALOR_1, VALOR_2, MAIOR

    if VALOR_1 > VALOR_2:
        MAIOR = VALOR_1
    else:
        MAIOR = VALOR_2

    print(f"\n--- O maior valor real é: {MAIOR:g} ---")

#Função Principal
def main():
    global VALOR_1, VALOR_2

    print("Exercício 19: Receba 2 valores reais. Cacule e mostre o maior deles.")
    VALOR_1 = float(input("Digite o primeiro valor: "))
    VALOR_2 = float(input("Digite o segundo valor: "))
    MAIOR()

#Iniciaização
if __name__ == "__main__":
    main()