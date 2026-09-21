# Exercício 20: Receba 3 coeficientes A, B e C de uma equação de 2º grau da fórmula Ax² + Bx + C = 0. Verifique e mostre a existência de raízes reais e, se caso exista, calcule e mostre.

# Variáveis globais
A = 0.0
B = 0.0
C = 0.0
DELTA = 0.0
X1 = 0.0
X2 = 0.0

#Cálculo Bhaskara
def calc_raizes():
    global A, B, C, DELTA, X1, X2

    DELTA = (B ** 2) - (4 * A * C)

    print("\n--- Resultado do cálculo ---")
    print(f"O valor de Delta é: {DELTA:g}")

    if DELTA < 0:
        print("Não existem raízes - Delta negativo.")
    else:
        X1 = (-B + (DELTA ** 0.5)) / (2 * A)
        X2 = (-B - (DELTA ** 0.5)) / (2 * A)
        print(f"x1 = {X1:g}")
        print(f"x2 = {X2:g}")

#Função Principal
def main():
    global A, B, C

    print("Exercício 20: Receba 3 coeficientes A, B e C de uma equação de 2º grau da fórmula Ax² + Bx + C = 0. Verifique e mostre a existência de raízes reais e, se caso exista, calcule e mostre.")

    A = float(input("Digite o coeficiente A: "))
    B = float(input("Digite o coeficiente B: "))
    C = float(input("Digite o coeficiente C: "))

    if A == 0:
        print("Não é uma equação de 2º grau se A for igual a 0!")
    else:
        calc_raizes()

if __name__ == "__main__":
    main()