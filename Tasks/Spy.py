def check(num):
    sums = 0
    product = 1
    while num:
        digit  = num % 10
        sums = sums +digit
        product = product * digit
        num = num //10
    print (sums, product)
check(1412)
