#Início do programa
print("Iniciando conversor de Decimal para Binário...")

#Solicita o número decimal que será convertido
numDec = int(input("Digite um número inteiro do sistema decimal: "))

#Loop para realizar várias conversões sem ter que sair do programa
while(numDec != 0):

    #Cria variável de apoio
    i = 0

    #Cria array para guardar os binários
    bin = []

    #Executar divisão recorrente do número decimal informado até o quociente ser 0
    while(numDec > 0):
        numDecAntes = numDec
        numDec = int(numDec / 2)
        numBin = numDecAntes % 2
        bin.append(numBin)

    #Informa ao usuário o binário convertido e na ordem correta de leitura
    size = len(bin)
    print("Convertido para binário: ", end ="")
    while( size > 0 ):
        print(bin[size-1], end ="")
        size -= 1

    #Opção para que o usuário possa sair após a conversão    
    numDec = int(input("\n\nDigite zero para sair ou outro número inteiro: "))
