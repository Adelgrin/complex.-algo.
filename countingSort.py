def countingSort(V):
    count = []
    for _ in range(maxVal(V)+1):
        count.append(0)
    acu = [count[0]-1]
    for j in V:
        count[j] += 1
    for k in range(1,len(count)):
        acu.append(acu[k-1]+count[k])
    saida = []
    for _ in range(len(V)):
        saida.append(0)
    for m in range(len(V)-1,-1,-1):
        saida[m] = acu.index(m)
        acu[saida[m]] -= 1
    return saida

def maxVal(V):

    max = V[0]
    for i in V:
        if i > max:
            max = i
    return max
if __name__ == "__main__":
    teste = [7,9,7,5,3,2,8,5,4,12,10,10,6]
    #teste = [13,8,2,9,2,3]
    print(countingSort(teste))

#bgl é loco
