no =1000
Num =9999

while no <=Num :
    prime =True
    i =2
    while i*i <=no:
        if no % i ==0:
            prime= False
            break
        i+=1
    if prime:
        print(no)
        break
    no +=1
