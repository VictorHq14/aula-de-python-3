pessoas = int(input(" digite quantas pessoas tem em sua sala:   "))
idade = 0
while True:
    for i in range(pessoas):
        idades = int(input("Digite a idade de cada uma dessas pessoas:  "))
        idade += idades
        mdi = idade / pessoas
    if mdi >= 60:
        print("sua sala é predominantemente idosa")
        break
    elif mdi >= 26:
        print("sala adulta")
        break
    elif mdi >= 0:
        print("salsa jovem")
        break
    else:
        print("Algo deu errado...")
        break