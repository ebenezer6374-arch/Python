ones = ['zero', 'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = [ 'ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

num = int(input("Type a number: "))
result = ""
while num >0:
    if num <20 :    
        print (ones[num] ,end =' ')
        break   
    elif  num <100:
        result = num //10
        print (tens[result -1],end = ' ')
        num = num %10
        # print (ones[num])
    else:
        result = num //100
        print (ones[result], "hundred" , end = ' ')
        num = num %100