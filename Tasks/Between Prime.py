no =11
Num =60

while no <= Num:
    prime = True
    i = 2
    while i *i <=no:
        if no %i ==0:
            prime = False
            break
        i+=1

    if prime:
        print(no)


    no +=1
