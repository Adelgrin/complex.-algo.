def fibonacci(n):
    if n <= 0 or n == 1:
        return n
    else:
        if n in tb.keys():
            return tb[n]
        tb[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return tb[n]
        #return fibonacci(n - 1) + fibonacci(n - 2)
    
#def inicializa(V,tam):
#    for _ in range(tam):
#        V.append(0)
#    return V
#
#def fibonacci_din(n):
#    V = [0] * (n + 1)
#    #V = inicializa(V,n+1)
#    V[0] = 0
#    V[1] = 1
#    for i in range(2,n+1):
#        V[i] = V[i-1] + V[i-2]
#    return V[n]

if __name__ == "__main__":

    tb = {}
    tb[0] = 0
    tb[1] = 1
    print(fibonacci(40))
    #for i in range(3,9999):
    #    print(fibonacci_din(i))
    #print(fibonacci_din(1000000000))
