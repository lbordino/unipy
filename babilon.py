def alg(a,x):
    y = 0.5*(x+a/x)
    return y


def rad():
    num=int(input("Numero di cui fare la radice: "))
    z = alg(num,1)
    j = 1
    while j > 0.00000001:
        k = alg(num,z)  
        z = alg(num,k) 
        j = abs(k - z)
    print(z)


rad()
