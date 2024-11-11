#x = int (input("Digite o primeiro número: "))
#y = int (input("Digite o segundo número :"))

#resultadoSOM = x + y
#resultadoSUB = x - y
#resultadoMUL = x * y
#resultadoDIV = x / y
#realizar o calculo
#print(f" {x} + {y} = {resultadoSOM}")
#print(f" {x} - {y} = {resultadoSUB}")
#print(f" {x} * {y} = {resultadoMUL}")
#print(f" {x} / {y} = {resultadoDIV}")


print("\t \t \t \t \t \t CALCULADORA")

print("\n")
operacao = input("Digite aqui qual operação você deseja utilizar(Por favor digite exatamente como está ilustrado a seguir) : \nsoma: + \nsubtração: - \nmultiplicacão: * \ndivisão: /  \n")
print("\n")

if operacao not in ["+" , "-" , "*" , "/"]:
    print ("OPERACAO INEXISTENTE,POR FAVOR TENTE NOVAMENTE")

else:
    x = int (input("Digite o primeiro número desejado para sua operação:"))
    y = int (input("Digite o segundo número desejado:"))
    if operacao == "+":
        print("OK, seu calculo está aqui:\n")
        print(f"{x} + {y} = {x + y}")
    if operacao == "-":
        print("OK, seu calculo está aqui:\n")
        print(f"{x} - {y} = { x - y}")
    if operacao == "*":
        print("OK, seu calculo está aqui:\n")
        print(f"{x} * {y} = { x * y}")
    if operacao == "/":
        print("OK, seu calculo está aqui:\n")
        print(f"{x} / {y} = {y / y}")