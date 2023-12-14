numeroImpressao = 0
numeroAnterior = 1
# inicia um for que define o tamanho da sequência atravez da variavel i 
while numeroImpressao < = 34:
    # importante imprimir o numero antes que o valor seja modificado, pois a sequencia possui um zero
    print(numeroImpressao)    
    numeroImpressao, numeroAnterior = numeroImpressao + numeroAnterior, numeroImpressao
