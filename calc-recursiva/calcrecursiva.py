def somar(a, b):
    return a + b
    # return a + (-b if b < 0 else b)

def subtrair(a, b):
    return a - b
    # return a - (-b if b < 0 else b)

def multiplicar(a, b):
    if b == 0:
        return 0  # Caso base: multiplicação por zero
    if b > 0:
        return a + multiplicar(a, b - 1)  # Adiciona 'a' b vezes
    return -multiplicar(a, -b)  # Caso b negativo: inverte o sinal

def dividir_parte_inteira(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")  # Verifica divisão por zero
    if a < b:
        return 0  # Caso base: quociente é 0 se o divisor é maior que o dividendo
    if a < 0 and b > 0:
        return -1 + dividir_parte_inteira(a + b, b)  # Ajusta para caso de números negativos
    if a > 0 and b < 0:
        return -1 + dividir_parte_inteira(a + b, b)
    if a < 0 and b < 0:
        return 1 + dividir_parte_inteira(a - b, b)
    return 1 + dividir_parte_inteira(a - b, b)  # Quociente incrementado recursivamente

def resto_divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")  # Verifica divisão por zero
    if a < b:
        return a if a >= 0 else a + b  # Retorna o restante da subtração
    if a < 0 and b > 0:
        return resto_divisao(a + b, b)  # Ajusta caso o dividendo seja negativo
    if a > 0 and b < 0:
        return resto_divisao(a + b, b) 
    if a < 0 and b < 0:
        return resto_divisao(a - b, b)
    return resto_divisao(a - b, b)  # Resto calculado recursivamente

# Retorna o quociente e o resto
def dividir(a, b):
    return dividir_parte_inteira(a, b), resto_divisao(a, b)

def exponencial(base, expoente):
    if expoente == 0:
        return 1  # Qualquer número elevado a 0 é 1
    return multiplicar(base, exponencial(base, expoente - 1))

def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não está definido para números negativos.")  # Verifica se tem num negativos
    if n == 0 or n == 1:
        return 1  # Caso base: fatorial de 0 ou 1 é 1
    return multiplicar(n, fatorial(n - 1)) 

# Dicionário p/ valores da sequência de Fib
mem_fib = {}

# obs: O seguinte site foi usado para as verificações: https://www.calculatorsoup.com/calculators/discretemathematics/fibonacci-calculator.php 

def fibonacci(n):
    if n < 0:
        raise ValueError("Números negativos não fazem parte da sequência.")  # Verifica entrada negativa
    if n == 0:
        return 0  # Caso base: Fib(0) = 0
    if n == 1:
        return 1  # Caso base: Fib(1) = 1
    if n in mem_fib:
        return mem_fib[n]  # Retorna o valor armazenado no cache
    mem_fib[n] = somar(fibonacci(n - 1), fibonacci(n - 2))
    return mem_fib[n]