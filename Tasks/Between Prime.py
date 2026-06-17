no =11
Num =60
count = 0

while no <= Num:
    prime = True
    i = 2
    while i *i <=no:
        if no %i ==0:
            prime = False
            break
        i+=1

    if prime:
        count +=1
        print(no)



    no +=1
print("No of prime numbers are between 11 and 60 is" , count)
