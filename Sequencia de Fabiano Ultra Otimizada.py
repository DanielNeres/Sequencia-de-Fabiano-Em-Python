numeroImpressao = 0
numeroAnterior = 1
# inicia um for que define o tamanho da sequência atravez da variavel i 
while numeroImpressao < = 34:
    # importante imprimir o numero antes que o valor seja modificado, pois a sequencia possui um zero
    print(numeroImpressao)    
    # aqui "numeroImpressao" recebe a soma do valor anterior de "numeroImpressao" e "numeroAnterior", enquanto "numeroAnterior" recebe o valor anterior de "numeroImpressao". isso pois, o python possui a atribuição múltipla
    numeroImpressao, numeroAnterior = numeroImpressao + numeroAnterior, numeroImpressao
