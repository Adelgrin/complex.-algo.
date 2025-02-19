def expon(num,exp):
    if exp == 0:
        return 1
    else:
        return num*expon(num,exp-1)

print(expon(3,2))