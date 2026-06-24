sentence = "I love you                            "
# for letter in sentence:
#     if letter != " ":
#         print(letter, end = "")

# space = False
# for letter in sentence:
#     if letter!= " ":
#         space = True
#     if  space == True:
#         print(letter , end = '')

# last_index = 0
# for index in range (len(sentence)-1,-1,-1):
#     # print(sentence[index] ,end = " ")
#     if sentence[index] != " ":
#             last_index = index  
#             break

# print (sentence[0:last_index +1])


word = "My favourite player is Dhoni, Dhanraj , Vinayagam"
key = "Dhoni"
key_length = len(key)

found = False
for i in range( len(word) - key_length+1):
    result = word [i: i +key_length]
    print(result)
    if result == key:
       found = True
       break
if found:
    print ("present")
else:
    print ("not present")   

