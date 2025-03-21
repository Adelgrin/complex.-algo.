def quickSort(v,q,p):
    if q < p:
        r = partition(v,q,p)
        quickSort(v,q,r-1)
        quickSort(v,r+1,p)
        return v
def partition(v,q,p):
    x = v[p]
    i = q - 1
    for j in range(q,p):
        if v[j] <= x:
            i += 1
            v[i],v[j] = v[j],v[i]
    v[i+1],v[p] = v[p],v[i+1]
    return i + 1
#print(quickSort([12, 11, 13, 5, 6, 7],0,len([12, 11, 13, 5, 6, 7])-1))
