# Exercício 22: Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

# Variáveis globais
NUM_1 = 0
NUM_2 = 0

# Ordenar e exibir

def ordem_cresc():
    global NUM_1, NUM_2

    print("\n--- Valores em Ordem Crescente ---")

    if NUM_1 < NUM_2:
        print(f"{NUM_1} \u27A1 {NUM_2}")
    else:
        print(f"{NUM_2} \u27A1 {NUM_1}")

# Função principal
def main():
    global NUM_1, NUM_2

    print("Exercício 22: Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.")

    NUM_1 = int(input("Digite um número inteiro: "))
    NUM_2 = int(input("Digite outro número inteiro: "))

    if NUM_1 == NUM_2:
        print("Digite números diferentes! Bora tentar de novo?!")
    else:
        ordem_cresc()

if __name__ == "__main__":
    main()