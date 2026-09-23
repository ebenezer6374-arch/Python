for num in [100 ,101]:
    n = num
    r = 0
    s = 0
    while n :
        r += (n % 10) * (2 **s)
        n = n//10
        s= s+1
    print (r)
    

