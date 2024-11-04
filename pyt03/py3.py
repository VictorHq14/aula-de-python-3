def encontrar_maior_menor(num1, num2, num3):
    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    return maior, menor

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))

    maior, menor = encontrar_maior_menor(numero1, numero2, numero3)

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

except ValueError:
    print("Por favor, insira apenas números válidos.")
