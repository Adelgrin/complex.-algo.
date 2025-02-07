def localizar(V,k):
    for i in range(0,len(V)):
        if V[i] == k:
            return True
    return False
vetor = [1,2,5,4,7,6]
print(localizar(vetor,6))
#O(n)