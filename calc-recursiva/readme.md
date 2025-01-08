# Calculadora Recursiva - Operações Básicas e Funcionalidades Avançadas 🧮

Este projeto implementa uma calculadora simples que suporta as operações aritméticas básicas (soma, subtração, multiplicação e divisão) utilizando apenas soma e subtração. Além disso, foram implementadas funções adicionais como exponenciação, fatorial e cálculo de números da sequência de Fibonacci utilizando memoização (hash) para otimizar a performance.


## Funcionalidades

- **Soma**: Realiza a soma de dois números inteiros.
- **Subtração**: Realiza a subtração de dois números inteiros.
- **Multiplicação**: Realiza a multiplicação de dois números inteiros utilizando somas sucessivas.
- **Divisão**: Calcula a parte inteira da divisão e o resto utilizando subtrações recursivas.
- **Exponenciação**: Calcula a exponenciação (base ^ expoente) utilizando multiplicações.
- **Fatorial**: Calcula o fatorial de um número inteiro não negativo.
- **Fibonacci**: Calcula o n-ésimo número da sequência de Fibonacci utilizando memoização para melhorar a eficiência do cálculo.

## Observações

- A função de divisão retorna um tupla com dois valores: o quociente e o resto.
- A função Fibonacci usa memorização (armazenamento de resultados anteriores em um dicionário) para otimizar o tempo de execução em números grandes.
- Todas as operações são realizadas recursivamente.

## Requisitos

- Python