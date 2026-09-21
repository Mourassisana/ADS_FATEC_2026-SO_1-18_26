# 🐍 Lista de Exercícios - Modularização e Docker em Python

Repositório desenvolvido para a disciplina de **Sistemas Operacionais** do curso de Análise e Desenvolvimento de Sistemas (ADS) na **FATEC Zona Leste**.

## 👤 Identificação
* **Estudante:** Ana Assis | Mourassisana
* **Instituição:** FATEC ZL (Faculdade de Tecnologia de São Paulo - Zona Leste)
* **Professor:** Leandro Colevati (Exercícios cedidos pelo Prof. Ricardo Satoshi)
* **Linguagem Utilizada:** Python 3.10+

---

## 🛠️ Diretrizes de Desenvolvimento (Padrão Colevati)
Todos os scripts deste lote foram estruturados seguindo regras rígidas de arquitetura para o primeiro semestre:
*   **Modularização com Função Principal:** Código gerenciado a partir da chamada de uma função `main()`.
*   **Procedimentos sem Retorno:** Funções focadas em processamento e exibição de dados, sem o uso da cláusula `return`.
*   **Sem Passagem de Parâmetros:** Toda a comunicação entre funções e escopos foi feita estritamente via variáveis `global`.
*   **Indentação Estrita:** Margens e blocos de código rigorosamente alinhados para o interpretador Python 3.

---

## 📋 Enunciados Resolvidos (18 ao 26)

Este projeto contempla a resolução em código Python dos seguintes problemas:

18. **Diferença do Maior pelo Menor:** Recebe 2 inteiros, calcula e mostra a subtração do maior valor pelo menor. *(Fluxo corrigido para coletar inputs antes da exibição).*
19. **Maior Valor Real:** Recebe 2 números reais e mostra o maior deles. *(Utiliza formatação `:g` para ocultar o `.0` desnecessário em inteiros).*
20. **Equação do 2º Grau (Bhaskara):** Calcula as raízes reais de uma equação. *(Contém trava que valida se o Delta é negativo antes de extrair a raiz, evitando quebras).*
21. **Média Bimestral:** Calcula a média aritmética de 4 notas e exibe se o aluno está Aprovado, em Exame ou Retido. *(Customizado com códigos Unicode nativos do Python para exibição estável de emojis no terminal).*
22. **Ordem Crescente de 2 Números:** Recebe 2 inteiros diferentes e os exibe organizados do menor para o maior.
23. **Encaixe de 4º Número:** Recebe 3 números em ordem crescente e encaixa um 4º número desordenado na posição correta. *(Possui **Blindagem de Entrada** que encerra o programa com alerta caso os 3 primeiros números não venham ordenados).*
24. **Divisibilidade por 2 e 3:** Verifica se um número inteiro é divisível por 2 e por 3 simultaneamente. *(Possui **Análise Detalhada** informando se divide por ambos, apenas por um deles ou por nenhum).*
25. **Duração de Jogo:** Calcula o tempo de jogo em horas e minutos considerando viradas de dia. *(Algoritmo linear usando resto de divisão por 1440. Possui **Sanitizador de Horários** que barra horas maiores que 23 ou minutos maiores que 59).*
26. **Verificação de Múltiplos:** Recebe 2 inteiros e descobre se o maior é múltiplo do menor. *(Contém trava de segurança que impede divisões por zero).*

---

## 💻 Tecnologias e Ambiente de Desenvolvimento
* **Sistema Operacional:** Xubuntu Linux (Máquina Virtual no VirtualBox)
* **Editor de Código:** Visual Studio Code (VS Code)
* **Interpretador:** Python 3

## 🚀 Como Executar os Arquivos (Parte 1)
Para rodar qualquer um dos exercícios direto no terminal do Linux, navegue até a pasta do projeto e execute:

```bash
python3 nome_do_arquivo.py
```

## 🐳 Próximos Passos - Docker (Parte 2)
Na próxima etapa do projeto, os scripts contidos neste repositório serão encapsulados e executados em um ambiente isolado utilizando **Docker**:
* **Imagem oficial:** `python`
* **Tag exata exigida:** `3.10.20`
* **Conectividade:** Uso de volumes permanentes (`-v`) mapeando a pasta do hospedeiro com o contêiner.

---
*Desenvolvido com 📝 e 🎓 por uma estudante de ADS da FATEC ZL.*