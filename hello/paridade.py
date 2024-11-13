def main():
    num = int(input("Por favor, digite um número que eu te direi se será par ou impar \n "))
    verificacao(num)


def verificacao(num):
    if num % 2 == 0:
        print("\nEste número é Par")
    else:
        print("\nEste número é Impar")

main()