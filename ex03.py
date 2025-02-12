import time
def insertion_sort(V,n):
    for i in range(1,n):
        chave = V[i]
        j = i - 1
        while(j>=0 and V[j] > chave):
            V[j+1] = V[j]
            j = j - 1
        V[j + 1] = chave
    return V
def troca(V,v,e):
    a = v
    V[v] = e
    V[e] = a
def selection_sort(V,n):
    for i in range(0,n-1):
        menor = i
        for j in range(i + 1,n):
            menor = j
            troca(V,i,menor)

def bubble_sort(V,n):
    for i in range(0,n-1):
        for j in range(n-1,i+1,-1):
            if V[j] < V[j-1]:
                troca(V,j,j-1)
    return V

#errado = [6,5,4,3,2,1]
errado = []
for x in range(10000,0,-1):
    errado.append(x)
inicio = time.process_time()
insertion_sort(errado[:],len(errado))
fim = time.process_time()
print("insertion ",fim-inicio)

inicio = time.process_time()
selection_sort(errado[:],len(errado))
fim = time.process_time()
print("selection ",fim-inicio)

inicio = time.process_time()
bubble_sort(errado[:],len(errado))
fim = time.process_time()
print("bubble ",fim-inicio)