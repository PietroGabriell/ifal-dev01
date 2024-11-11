pontos = float(input("Qual a pontuação do aluno?\n"))



if pontos >= 80 and pontos <= 100:
    print("\no aluno Tirou nota A na prova")
elif pontos >= 60 and pontos  <= 80:
    print("\no aluno Tirou nota B na prova")
elif pontos >= 40 and pontos <= 60:
    print("\no aluno Tirou nota C na prova")
elif pontos >= 20 and pontos <= 40:
    print("\no aluno Tirou nota D na prova")
elif pontos >= 10 and pontos <= 20:
    print("\no aluno Tirou E na prova")
else:
    print("\no aluno Tirou F na prova INFELIZMENTE")