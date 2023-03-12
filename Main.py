def binTOdec(numBin):

    qtdAlgarismos = len(str(abs(numBin)))
    
    #Guarda binário em uma string (array)
    binStr = str(numBin)
    
    #criar array para guardar resultados das potências
    arrayRes = []

    #cria variável de apoio
    i = 0

    #trata cada posição com as potências
    while (qtdAlgarismos > 0):
        res = int(binStr[qtdAlgarismos-1])*2**i
        arrayRes.append(res)
        qtdAlgarismos -= 1
        i += 1

    #Imprime o que conseguiu guardar na array de soma
    return sum(arrayRes)

def decTObin(numDec):
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

print("\nBem vindo ao conversor de números do Bruno.")
escolha = -1
while (escolha != 0):
    print("\nMENU PRINCIPAL")
    print("1 - Conversão Binário -> Decimal")
    print("2 - Conversão Decimal -> Binário")
    print("0 - Sair")
    escolha = int(input("\nDigite aqui o número da opção desejada: "))
    if(escolha == 1):
        numbin = int(input("\nDigite um valor binário: "))
        print("Convertido para decimal: " , str(binTOdec(numbin)))

    elif(escolha == 2):
        numdec = input("\nDigite um valor decimal para converter: ")
        decTObin(numdec)

    elif(escolha == 0):
        print("\nEncerrando...")

    else:
        print("\nErro")