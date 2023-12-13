numeroImpressao = 0
numeroAnterior = 1
i = 10

for _ in range(i):
    print(numeroImpressao)    
    numeroImpressao += numeroAnterior
    numeroAnterior = numeroImpressao - numeroAnterior
