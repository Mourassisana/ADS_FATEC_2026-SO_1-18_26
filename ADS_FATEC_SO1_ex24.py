# Exercício 24: Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

# Variável global
NUMERO = 0

# verificar se é divisível por 2 e 3 ao mesmo tempo.
def divisivel():
    global NUMERO

    print("\n--- Verificando divisão... ---")

    if (NUMERO % 2 == 0) and (NUMERO % 3 == 0):
        print(f"O número {NUMERO} é divisível por 2 e 3 ao mesmo tempo!")
    elif NUMERO % 2 == 0:
        print(f"O número {NUMERO} é divisível por 2, mas NÃO é divisível por 3")
    elif NUMERO %3 == 0:
        print(f"O número {NUMERO} é divisível por 3, mas NÃO é divisível por 2")
    else:
        print(f"O número {NUMERO} NÃO é divisível nem por 2 e nem por 3")

def main():
    global NUMERO

    print("Exercício 24: Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.")
    NUMERO = int(input("Digite um número inteiro: "))
    
    divisivel()

if __name__ == "__main__":
    main()