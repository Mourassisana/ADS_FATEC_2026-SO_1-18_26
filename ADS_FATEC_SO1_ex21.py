# Exercício 21: Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
# a. Se a média for >= 6,00, exibir: "APROVADO";
# b. Se a média for >= 3,00, exibir: "EXAME";
# c. Se a média for < 3,00, exibir: "RETIDO".

# Variáveis globais
NB1 = 0.00
NB2 = 0.00
NB3 = 0.00
NB4 = 0.00
MEDIA = 0.00

# Cálculo e situação do estudante
def verificar_situacao():
    global NB1, NB2, NB3, NB4, MEDIA

    MEDIA = ((NB1 + NB2 + NB3 + NB4) / 4)

    print("\n--- Resultado Final ---")
    print(f"Média Final: {MEDIA:g}")

    if MEDIA >= 6.00:
        print("Vc foi... APROVADO! \U0001F973")
    elif MEDIA >= 3.00:
        print("Vc ficou de EXAME... \U0001F610")
    else:
        print("Vc está RETIDO \U0001FAC2")

def main():
    global NB1, NB2, NB3, NB4

    print("Exercício 21: Receba 4 notas bimestrais de um aluno. \nCalcule e mostre a média aritmética. \nMostre a mensagem de acordo com a média")

    NB1 = float(input("Digite a nota do 1º Bimestre: "))
    NB2 = float(input("Digite a nota do 2º Bimestre: "))
    NB3 = float(input("Digite a nota do 3º Bimestre: "))
    NB4 = float(input("Digite a nota do 4º Bimestre: "))

    verificar_situacao()

if __name__ == "__main__":
    main()