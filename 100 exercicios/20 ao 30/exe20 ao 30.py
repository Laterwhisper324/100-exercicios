# Exercício 1
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Exercício 2
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exercício 4
letra = input("Digite uma letra: ").lower()

if letra in 'aeiou':
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")

# Exercício 5
a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    print("Os números formam um triângulo.")
else:
    print("Os números não formam um triângulo.")

# Exercício 6
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

# Exercício 7
senha = input("Digite uma senha: ")
senha_predefinida = "senha123"

if senha == senha_predefinida:
    print("A senha está correta.")
else:
    print("A senha está incorreta.")

# Exercício 8
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 < num2 < num3:
    print("Os números estão em ordem crescente.")
else:
    print("Os números não estão em ordem crescente.")

# Exercício 9
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Exercício 10
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

print("O resultado da operação é:", resultado)