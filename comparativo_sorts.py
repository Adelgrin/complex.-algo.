import time
from mergeSort import mergeSort
from quickSort import quickSort
from heapSort import heapSort
from countingSort import countingSort
from radixSort import radixSort

vet = []
for i in range(999,0,-1):
    vet.append(i)

inicio = time.process_time()
mergeSort(vet[:],0,len(vet)-1)
fim = time.process_time()
print("merge ",fim-inicio)
inicio = time.process_time()
quickSort(vet[:],0,len(vet)-1)
fim = time.process_time()
print("quick ",fim-inicio)
inicio = time.process_time()
heapSort(vet[:])
fim = time.process_time()
print("heap ",fim-inicio)
inicio = time.process_time()
countingSort(vet[:])
fim = time.process_time()
print("count ",fim-inicio)
inicio = time.process_time()
radixSort(vet[:])
fim = time.process_time()
print("radix ",fim-inicio)