N =11
prime_sum = 0
num = 2
no1 =0
while num<=N:
    prime = True
    i =2
    while i*i<=num:
            if num%i ==0:
                prime = False
                break
            i+=1
    if prime:
        print(num , end = " ")
        print(num +2 ,end = " ")
        prime_sum +=num

    num +=1

#print (prime_sum)


#N =11
#prime_sum = 2
#num = 3
#while num<=N:
#    prime = True
#    i = 3
#    while i*i <=num:
#        if num%i==0:
#            prime =False
#            break
#        i+=2
#    if prime:
#        prime_sum  +=num
#    num +=2
#
#print (prime_sum)
