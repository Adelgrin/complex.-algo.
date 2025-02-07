def fib(n):
    if n<= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibcorreto(n):
    listafib = []
    for i in range(0,n):
        if i <= 1:
            listafib.append(i)
        else:
            listafib.append(listafib[i-1]+listafib[i-2])
    return listafib[:]



print(fibcorreto(50))