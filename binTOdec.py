numBin = int(input('Digite um valor em binário: '))
#Loop para sair quando digitar zero ou continuar convertendo
while (numBin != 0):
    #para converter um número binário em um número decimal, devemos obter o resultado da potência posicional de cada algarismo
    #primeiro precisamos saber quantos algarísmos binários foram digitados - Isso será útil para o cálculo das potências posicionais*
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
    print("Valor convertido para decimal:", sum(arrayRes))

    numBin = int(input('\n\nDigite zero para sair ou outro valor binário para conversão: '))