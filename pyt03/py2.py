while True:
    idade = input("digite sua idade ou 'sair' para encerrar o programa:  ")
    if idade >= 60:
        print("vocẽ é idoso")
    elif idade >=18:
        print("vocẽ é adulto")
    elif idade >= 12:
        print("voce é adolescente")
    elif idade < 12:
        print("voce é criança")
    elif idade == "sair":
        break
    else:
        print("Idade inválida.")