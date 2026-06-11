
def digit(no):
    sum =0
    while no >0:
        sum = sum + no%10
        no = no //10
    return sum


no = 10
Num = 99

while no <=Num:

    prime =True
    i =2
    while i*i <=no:
        if no %i ==0:
            prime = False
            break
        i+=1
    if prime:
        if digit(no) ==10:
#            print(no)
            if 57%no==0:
                print(no)

    no +=1
