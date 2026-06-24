no = 10
Num =99
first = 0
last= 0

while no <=Num:
    prime =True
    i =2
    while i *i <=no:
        if no % i ==0:
            prime = False
            break
        i +=1
    if prime:
        if first ==0:
            first = no
        last =no

    no +=  1
print (first ,last)
