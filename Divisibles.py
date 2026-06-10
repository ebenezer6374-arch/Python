#Divisible by 11:

no = 1001045
ones= 0
tens= 0

while no >0:
    last_two = no % 100
    ones =ones + last_two % 10
    tens = tens + last_two //10
    no = no //100


if (ones -tens) %11 ==0:
    print("divisible")
else :
    print ("not divisible")



#Tasks -------------------------------
#
#no = 1234
#total = 0
#while no>1:
#    print(no%100 ,end = " ") # 34 23 12
#    total = total + no %100
#    no = no // 10
#print (total)


#
#no = 1234
#total = 0
#while no>1:
#    print(no%100 ,end = " ") # 34 12
#    total = total + no%100
#    no = no // 100
#print (total)



#no = 123456
#while no >0:
#    print (no % 1000 ,end = " ")
#    no = no //1000
