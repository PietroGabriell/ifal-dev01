def main():
    x = int(input("Escolha o seu primeiro número\n \t"))
    y = int(input("Escolha o seu segundo número\n \t"))
    verificacao(x,y)



def verificacao(x,y):
    if x < y:
        print(f" {x} é menor que {y}")
    elif x > y:
        print(f"{x} é maior que {y}")
    else:
        print(f"{x} é igual a {y}")


main()