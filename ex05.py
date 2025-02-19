import time
def soma(V,numV):
    if numV == 0:
        return 0
    else:
        return V[numV-1]+soma(V,numV-1)
    
vetor = []
for i in range(0,1000):
    vetor.append(i)
inicio = time.process_time()
print(soma(vetor,len(vetor)))
fim = time.process_time()
print(fim-inicio)