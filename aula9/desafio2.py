for x in range(1000, 10000):
    n1 = x // 100
    n2 = x % 100
    if(n1+n2)**2 == x:
        print(x)
