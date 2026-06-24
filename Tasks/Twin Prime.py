def prime(n):
    if n<2:
        return False
    i =2
    while i *i <=n:
        if n%i ==0:
            return False
        i+=1
    return True

end = 100
start =2
while start<=end:
    if prime(start) and prime(start+2):
        print (start , start+2)
    start   +=1
