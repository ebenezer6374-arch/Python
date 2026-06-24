#
#no1 = 1184
#no2 = 1210
#
#def ToFindDivisors(no):
#    div =2
#    divisor_sum = 1
#    while div <= no //2:
#        if no % div == 0:
#            divisor_sum = divisor_sum + div
#        div +=1
#    return divisor_sum
#
#if ToFindDivisors(no1) == no2 and  ToFindDivisors(no2) == no1:
#    print("Amicbale")
#else:
#    print("Not Amicbale")
#
#A book seller has 175 English books, 245 Science books and 385 Mathematics
#books. He wants to sell the books in a box, subject-wise in equal numbers. What will be
#the greatest number of the boxes required? Also find the number of books for each subject
#in a box.

english = 175
science = 245
maths = 385
hcf= 0
no = 2

while no <=175 //2:
    if english % no == 0 and science % no ==0 and maths % no ==0:
        hcf= no
    no +=1

each_english = english //hcf
each_science = science //hcf
each_maths = maths //hcf

print( "HCF --->" , hcf)
print ("No.of books in english = " , each_english)
print ("No.of books in science = " , each_science)
print ("No.of books in maths = " , each_maths)
