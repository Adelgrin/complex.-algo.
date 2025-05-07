def maiorsc(tx1, tx2):
    i = len(tx1) - 1
    j = len(tx2) - 1
    return msc(i,j,tx1,tx2)
def msc(i,j,tx1,tx2):
    if i < 0 or j < 0:
        return ""
    if tx1[i] == tx2[j]:
        return msc(i-1,j-1,tx1,tx2) + tx1[i]
    else:
        seq1 = msc(i-1,j,tx1,tx2)
        seq2 = msc(i,j-1,tx1,tx2)
        return maior(seq1,seq2)
def maior(a,b):
    if len(a) > len(b):
        return a
    else:
        return b


def maiorsc_din(tx1,tx2):
    m = len(tx1)
    n = len(tx2)
    tb = [0][0]
    inicializa(tb,m,n)

    for i in range(1,m):
        for j in range(1,n):
            if tx1[i-1] == tx2[j-1]:
                tb[i][j] = tb[i-1][j-1]+1
            else:
                tb[i][j] = max(tb[i-1][j],tb[i][j-1])

def inicializa(V,m,n):
    for i in range(m+1):
        for j in range(n+1):
            V[i][j] = 0
    return V
if __name__ == "__main__":
    #tx1 = "abcde"
    #tx2 = "ace"
    tx1 = "xxxxxxxxadcbe"
    tx2 = "yyyyyyyyyyyyace"
    print(maiorsc(tx1,tx2))
    print(maiorsc_din(tx1,tx2))