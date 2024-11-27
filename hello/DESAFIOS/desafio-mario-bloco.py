def main ():
    tamanho = int(input("Quantos blocos você deseja?\t"))
    bloco(tamanho)

def bloco(tamanho):
    bloco = ("[]" * tamanho)
    print(f"{bloco}\n" * tamanho, end = "")

main()