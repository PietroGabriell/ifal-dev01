armas = {
    "mp40" : {
        "Dano no Capa" : "134",
        "Precisão" : "80%",
        "Velocidade de disparo" : "20", 
        "Dano na Mira 4x" : "Não tem Mira 4x",
        "Dano na Mira 2x" : "Não tem Mira 2x",
        "Dano no Colete" : "25"
    },
    "ump" : {
        "Dano no Capa" : "137",
        "Precisão" : "75%",
        "Velocidade de disparo" : "10", 
        "Dano na Mira 4x" : "25",
        "Dano na Mira 2x" : "18",
        "Dano no Colete" : "25"
    },
    "baubau" : {
        "Dano no Capa" : "Não há Dano Definido",
        "Precisão" : "80%",
        "Velocidade de disparo" : "2", 
        "Dano na Mira 4x" : "Não tem Mira 4x",
        "Dano na Mira 2x" : "Não tem Mira 2x",
        "Dano no Colete" : "Não há Dano definido"
    },
    "m1014" : {
        "Dano no Capa" : "Não tem Dano determinado",
        "Precisão" : "80%",
        "Velocidade de disparo" : "8", 
        "Dano na Mira 4x" : "Não tem Mira 4x",
        "Dano na Mira 2x" : "Não tem Mira 2x",
        "Dano no Colete" : "Não tem Dano determinado"
    },
    "awm" : {
        "Dano no Capa" : "1100",
        "Precisão" : "100%",
        "Velocidade de disparo" : "1", 
        "Dano na Mira 4x" : "Não tem Mira 4x",
        "Dano na Mira 2x" : "Não tem Mira 2x",
        "Dano no Colete" : "150 a 300"
    },
    "desert" : {
        "Dano no Capa" : "495",
        "Precisão" : "90%",
        "Velocidade de disparo" : "7", 
        "Dano na Mira 4x" : "Não tem Mira 4x",
        "Dano na Mira 2x" : "Não tem Mira 2x",
        "Dano no Colete" : "90"
    },
    "xm8" : {
        "Dano no Capa" : "187",
        "Precisão" : "75%",
        "Velocidade de disparo" : "10", 
        "Dano na Mira 4x" : "Não tem Mira 4x",
        "Dano na Mira 2x" : "187",
        "Dano no Colete" : "34"
    },
    "usp" : {
        "Dano no Capa" : "110",
        "Precisão" : "60%",
        "Velocidade de disparo" : "70%", 
        "Dano na Mira 4x" : "Não tem Mira 4x",
        "Dano na Mira 2x" : "Não tem Mira 2x",
        "Dano no Colete" : "15 a 20"
    },
    "carapina" : {
        "Dano no Capa" : "341",
        "Precisão" : "80%",
        "Velocidade de disparo" : "8", 
        "Dano na Mira 4x" : "62",
        "Dano na Mira 2x" : "Não tem Mira 2x",
        "Dano no Colete" : "62"
    },
    "svd" : {
        "Dano no Capa" : "440",
        "Precisão" : "80%",
        "Velocidade de disparo" : "8", 
        "Dano na Mira 4x" : "112",
        "Dano na Mira 2x" : "Não tem Mira 2x",
        "Dano no Colete" : "112"
    },
    "aug" : {
        "Dano no Capa" : "172",
        "Precisão" : "70%",
        "Velocidade de disparo" : "9", 
        "Dano na Mira 4x" : "32",
        "Dano na Mira 2x" : "172",
        "Dano no Colete" : "32"
    }
}

def exibir(nome):
    if nome in armas:
        arma = armas[nome]
        print(f"\nNome: {nome}\n")
        print(f"Dano no Capa: {arma['Dano no Capa']}\n")
        print(f"Precisão: {arma['Precisão']}\n")
        print(f"Velocidade de disparo: {arma['Velocidade de disparo']}\n")
        print(f"Dano na Mira 4x: {arma['Dano na Mira 4x']}\n")
        print(f"Dano na Mira 2x: {arma['Dano na Mira 2x']}\n")
        print(f"Dano no Colete: {arma['Dano no Colete']}\n")
        
    else:
        print("arma não encontrada")

armas_freefire = input("digite uma arma: ").lower()

exibir(armas_freefire)