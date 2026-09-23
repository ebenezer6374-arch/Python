for num in [8,18]:
    n = num
    r = ""
    while n:    
        r = str(n%2) + r
        n = n //2
    print (r)
