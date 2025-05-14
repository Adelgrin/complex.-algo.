def mochila(itens,capacidade,n):
    itens = ordena(itens)
    #itens.sort(key=lambda x: x[1] / x[0], reverse=True)
    total = 0
    for i in range(n):
        peso = itens[i][0]
        valor = itens[i][1]
        if peso <= capacidade:
            total += valor
            capacidade -= peso
        else:
            total += valor * (capacidade / peso)
            capacidade = 0
        if capacidade == 0:
            return total
def ordena(itens):
    valorPeso = {}
    for i in itens:
        valorPeso[i[1] / i[0]] = i
    valorPeso = sorted(valorPeso.items(), key=lambda x: x[0])
    a = []
    for i in range(len(valorPeso)-1,-1,-1):
        a.append(valorPeso[i][1])
    return a
if __name__ == "__main__":
    itens = [(30,120),(10,60),(20,100)]
    print(mochila(itens,50,len(itens)))
    