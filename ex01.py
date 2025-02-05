def localizar(V,n,k):
    for i in range(0,n):
        if V[i] == k:
            return True
    return False
vetor = [1,2,5,4,2,6]
print(localizar(vetor,len(vetor),6))