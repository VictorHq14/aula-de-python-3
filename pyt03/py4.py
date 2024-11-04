qp = 0
qi = 0

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    if numero % 2 == 0:
        qp += 1
        print(f"{qp} pares e {qi} impares")
    else:
        qi += 1
        print(f"{qi} impares e {qp} pares")