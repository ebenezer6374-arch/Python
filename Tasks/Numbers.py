#Neon Number

given_no = 9
sq_root = given_no * given_no
total_digits = 0
while sq_root>0:
   total_digits = total_digits  + sq_root % 10
   sq_root = sq_root//10
if given_no == total_digits :
    print("Given no is Neon Number")
else:
    print("Not a Neon Number")


#Strong Number
#
