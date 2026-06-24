#no =1000
#Num =9999
#
#while no <=Num :
#    prime =True
#    i =2
#    while i*i <=no:
#        if no % i ==0:
#            prime= False
#            break
#        i+=1
#    if prime:
#        print(no)
#        break
#    no +=1
#

#no  = 10000
#Num =99999
#
#if no > Num lcm = no lcm = Num
#while True:
#   if no %  72 ==0 and no % 108 ==0:
#        print(no)
#        break
#   no +=2

no1 = 72
no2 = 108

if no1>no2:
    lcm = no1
else:
    lcm = no2


while True:
    if lcm % no1 == 0 and lcm % no2 ==0:
        break
    lcm +=1
#print (lcm)
#lcm = 216

no = 10000

while no % lcm != 0:
    no += 1

print(no)






















#print (lcm)
