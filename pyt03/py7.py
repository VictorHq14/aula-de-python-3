total_gasto = 0
contagem_acima_1000 = 0
nome_produto_mais_barato = ""
preco_produto_mais_barato = float('inf')


while True:
    nome_produto = input("Digite o nome do produto: ")

    try:
        preco_produto = float(input("Digite o preço do produto: R$ "))
    except ValueError:
        print("Por favor, insira um valor numérico válido para o preço.")
        continue 

    total_gasto += preco_produto

    if preco_produto > 1000:
        contagem_acima_1000 += 1

    if preco_produto < preco_produto_mais_barato:
        preco_produto_mais_barato = preco_produto
        nome_produto_mais_barato = nome_produto

    continuar = input("Deseja continuar inserindo produtos? (s/n): ").lower()
    if continuar != 's':
        break

print("\nResumo da Compra:")
print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Quantidade de produtos acima de R$ 1000: {contagem_acima_1000}")
print(f"Produto mais barato: {nome_produto_mais_barato} (R$ {preco_produto_mais_barato:.2f})")
