# Exercício 23: Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

# Variáveis globais
N1 = 0
N2 = 0
N3 = 0
N4 = 0

def ordenar():
    global N1, N2, N3, N4

    print("\n --- Valores em ordem crescente ---")

    if N4 >= N3:
        print(f"{N1} \u27A1 {N2} \u27A1 {N3} \u27A1 {N4}")
    elif N4 >= N2:
        print(f"{N1} \u27A1 {N2} \u27A1 {N4} \u27A1 {N3}")
    elif N4 >= N1:
        print(f"{N1} \u27A1 {N4} \u27A1 {N2} \u27A1 {N3}")
    else:
        print(f"{N4} \u27A1 {N1} \u27A1 {N2} \u27A1 {N3}")

def main():
    global N1, N2, N3, N4

    print("Exercício 23: Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor \nnão necessariamente em ordem. Mostre os 4 números em ordem crescente.")

    print("Digite os três primeiros OBRIGATORIAMENTE em ordem crescente")
    N1 = int(input("Digite o primeiro valor: "))
    N2 = int(input("Digite o segundo valor: "))
    N3 = int(input("Digite o terceiro valor: "))

    if N2 < N1 or N3 < N2:
        print("\n\u274C Ooops... Vc não seguiu a ordem correta \nTente rodar novamente o programa, inserindo os 3 primeiros números em ordem crescente")
    else:
        print("Agora insira o último valor em qualquer ordem:")
        N4 = int(input("Digite o quarto valor: "))

        ordenar()

if __name__ == "__main__":
    main()