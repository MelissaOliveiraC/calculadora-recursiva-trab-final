from calcrecursiva import somar, subtrair, multiplicar, dividir, exponencial, fatorial, fibonacci

def menu():
    print("\n=======================# Calculadora #=======================")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão e Resto")
    print("5. Exponenciação")
    print("6. Fatorial")
    print("7. Fibonacci")

    while True:
        try:
            operacao = int(input("Escolha a operação (1/2/3/4/5/6/7 ou 0 para sair): "))
            if operacao == 0:
                print("\n=======================# Calculadora Encerrada #=======================\n\n")
                break
            
            if operacao not in [1, 2, 3, 4, 5, 6, 7]:
                print("Operação inválida! Escolha uma operação válida.")
                continue
            
            if operacao == 6:
                n = int(input("Digite o número para calcular o fatorial (inteiro não negativo): "))
                if n < 0:
                    print("Erro: O número para o fatorial deve ser um inteiro não negativo.")
                    continue
                print(f"Resultado de {n}! = {fatorial(n)}")
            elif operacao == 7:
                n = int(input("Digite o valor de n para calcular Fibonacci (inteiro não negativo): "))
                if n < 0:
                    print("Erro: O número para Fibonacci deve ser um inteiro não negativo.")
                    continue
                print(f"Resultado de Fibonacci({n}) = {fibonacci(n)}")
            else:
                a = int(input("Digite o primeiro número inteiro: "))
                if operacao == 5:
                    b = int(input("Digite o expoente (inteiro não negativo): "))
                    if b < 0:
                        print("O expoente deve ser um número inteiro não negativo.")
                        continue
                else:
                    b = int(input("Digite o segundo número inteiro: "))
                
                if operacao == 1:
                    print(f"Resultado de {a} + {b} = {somar(a, b)}")
                elif operacao == 2:
                    print(f"Resultado de {a} - {b} = {subtrair(a, b)}")
                elif operacao == 3:
                    print(f"Resultado de {a} * {b} = {multiplicar(a, b)}")
                elif operacao == 4:
                    if b == 0:
                        print("Erro: Divisão por 0.")
                    else:
                        quociente, resto = dividir(a, b)
                        print(f"Resultado de {a} / {b} = {quociente}, resto = {resto}")
                elif operacao == 5:
                    print(f"Resultado de {a} ^ {b} = {exponencial(a, b)}")
        except ValueError:
            print("Insira valores válidos.")
        except Exception as e:
            print(f"Falha inesperada: {e}")

# Executar a calculadora
if __name__ == "__main__":
    menu()