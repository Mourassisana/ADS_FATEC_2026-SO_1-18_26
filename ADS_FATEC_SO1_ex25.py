# Exercício 25: Receba a hora de início e de fim de um jogo (hh:mm). Calcule o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24h e pode começar em um dia e terminar noutro.

# Variáveis globais
HORA_INICIAL = 0
MIN_INICIAL = 0
HORA_FIM = 0
MIN_FIM = 0
DURACAO_HORAS = 0
DURACAO_MIN = 0

def tempo_jogo():
    global HORA_INICIAL, HORA_FIM, MIN_INICIAL, MIN_FIM, DURACAO_HORAS, DURACAO_MIN

    minutos_inicio = ((HORA_INICIAL * 60) + MIN_INICIAL)
    minutos_fim = ((HORA_FIM * 60) + MIN_FIM)

    minutos_totais = ((minutos_fim - minutos_inicio) % 1440)

    DURACAO_HORAS = (minutos_totais // 60)
    DURACAO_MIN = (minutos_totais % 60)

    print("\n --- Duração do Jogo ---")
    if HORA_FIM < HORA_INICIAL:
        print(f"Nota: O jogo começou às {HORA_INICIAL:02d}:{MIN_INICIAL:02d} e terminou às {HORA_FIM:02d}:{MIN_FIM:02d} do DIA SEGUINTE! \U0001F31B")
    else:
        print(f"Nota: O jogo começou às {HORA_INICIAL:02d}:{MIN_INICIAL:02d} e terminou às {HORA_FIM:02d}:{MIN_FIM:02d} do MESMO DIA \u2600 \ufe0f")
    print(f"\nO jogo durou: {DURACAO_HORAS}h e {DURACAO_MIN}min \u23F1")

def main():
    global HORA_INICIAL, MIN_INICIAL, HORA_FIM, MIN_FIM, DURACAO_HORAS, DURACAO_MIN

    print("Exercício 25: Receba a hora de início e de fim de um jogo (hh:mm). \nCalcule o tempo do jogo em horas e minutos, sabendo que: \n1) o tempo máximo é menor que 24h e \n2) pode começar em um dia e terminar noutro.")

    print("\n--- Horário de Início ---")
    HORA_INICIAL = int(input("Digite a hora de início do jogo (0 a 23): "))
    MIN_INICIAL = int(input("Digite os minutos de início do jogo (0 a 59): "))
    print("\n--- Horário de Término ---")
    HORA_FIM = int(input("Digite a hora de término do jogo (0 a 23): "))
    MIN_FIM = int(input("Digite os minutos de término do jogo (0 a 59): "))

    if (HORA_INICIAL < 0 or HORA_INICIAL > 23) or (MIN_INICIAL < 0 or MIN_INICIAL > 59) or (HORA_FIM < 0 or HORA_FIM > 59) or (MIN_FIM < 0 or MIN_FIM > 59):
        print("\n \u274C Oops - Horário inválido")
        print("Por favor, reinicie o programa e digite um horário válido \nconsiderando HORA entre 0 e 23 e MINUTOS entre 0 e 59")
    else:
        tempo_jogo()

if __name__ == "__main__":
    main()