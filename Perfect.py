no = 496
sum = 0
i =1

while i <no:
    if no%i==0:
        sum +=i
    i+=1

if sum ==no:
    print("perfect")
else:
    print("Not Perfect")


#no =6
#sum = 0
#for i in range(1,no):
#    if no%i ==0:
#        sum+=i
#if sum ==no:
#    print("perfect")
#else:
#    print("Not Perfect")
