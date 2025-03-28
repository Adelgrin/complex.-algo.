from countingSort import maxVal
def countingSort(V,x):
    v = []
    for a in range(len(V)):
        v.append(0)
        v[a] = get_digito(V[a],x)
    count = []
    for i in range(10):
        count.append(0)
    acu = [count[0]-1]
    for j in v:
        count[j] += 1
    for k in range(1,len(count)):
        acu.append(acu[k-1]+count[k])
    saida = []
    for l in range(len(v)):
        saida.append(0)
    for m in range(len(v)-1,-1,-1):
        saida[acu[v[m]]] = V[m]
        acu[v[m]] -= 1
    return saida

def get_qtd_digitos(num):
    a=0
    while num > 0:
        num = num // 10
        a+=1
    return a
def get_digito(num,pos):
    return (num//(10**pos))%10

    
def radixSort(V):
    for i in range(get_qtd_digitos(maxVal(V))):
        V = countingSort(V,i)
    return V
    


if __name__ == "__main__":
    teste = [73,19,37,25,13,21]
    print(radixSort(teste))