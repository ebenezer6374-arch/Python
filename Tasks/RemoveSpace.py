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


word = "My favourite player is Dhoni , Dhanraj , Vinayagam"
key = "Vinayagam"
key_length = len(key)
# result =  (word[:key_length]) 
# print (result)
# if result == key:
#     print ("present")
# result = (world[1 :key_length+1])
# print  (result)
# if result = key:
#     print ("present")
found = True
for i in range(key_length):
    if word[i] != key[i]:
       found = False
       break
if found:
    print ("present")
    # else:  
else:
    print ("not present")   
    #     key_length+=1
