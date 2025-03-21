import time
from mergeSort import mergeSort
from quickSort import quickSort
from heapSort import heapSort

vet = []
for i in range(999,0,-1):
    vet.append(i)

inicio = time.process_time()
mergeSort(vet,0,len(vet)-1)
fim = time.process_time()
print("merge ",fim-inicio)
inicio = time.process_time()
quickSort(vet,0,len(vet)-1)
fim = time.process_time()
print("quick ",fim-inicio)
inicio = time.process_time()
heapSort(vet)
fim = time.process_time()
print("heap ",fim-inicio)