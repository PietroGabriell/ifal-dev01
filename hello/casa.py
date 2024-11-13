def main():
    nome = input("Qual é o nome do personagem? \n ")
    verificacao(nome)

def verificacao(nome):
    if nome == "herry" or nome == "rony" or nome == "hermione":
        print("Este personagem Mora na Grifinória")
    
    elif nome == "draco":
        print("Este personagem Mora na Sonserina")
    
    elif nome == "luna":
        print("Esta personagem Mora na Corvinal")
    
    elif nome == "cedric":
        print("Este personagem Mora na Lufa-Lufa")
    
    else:
        print("Este personagem não foi encontrado,por favor digite um personagem existente")
    

main()