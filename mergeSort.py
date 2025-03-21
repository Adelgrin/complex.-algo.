from math import floor
def mergeSort(v,left,right):
    if(left<right):
        mid = floor((left+right)/2)
        mergeSort(v,left,mid)
        mergeSort(v,mid+1,right)
        Merge(v,left,mid,right)
        return v
def Merge(v,left,mid,right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = v[left + i]

    for j in range(n2):
        R[j] = v[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        v[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        v[k] = R[j]
        j += 1
        k += 1
#print(mergeSort([12, 11, 13, 5, 6, 7],0,5))
