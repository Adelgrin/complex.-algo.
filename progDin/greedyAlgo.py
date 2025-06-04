def greedy_selector(s,f,n):
    A = [(s[0],f[0])]
    k = 0
    for m in range(1,n):
        if s[m] >= f[k]:
            A = A + [(s[m],f[m])]
            k = m
    return A
if __name__ == "__main__":
    s = [1,3,0,5,3,5,6,7,8,2,12]
    f = [4,5,6,7,9,9,10,11,12,14,16]
    n = len(s)
    print(greedy_selector(s,f,n))