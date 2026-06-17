#There are four Mobile Phones in a house. At 5 a.m, all the four Mobile
#Phones will ring together. Thereafter, the first one rings every 15 minutes, the second one
#rings every 20 minutes, the third one rings every 25 minutes and the fourth one rings
#every 30 minutes. At what time, will the four Mobile Phones ring together again?
#
#we Initialize the current time with 300 that is exactly 5 and I am checking for the loop for 24 hrs that is 1440 minutes




start = 5
current_time = 30


while True:
    if current_time%15==0 and current_time % 20 ==0 and current_time % 25 ==0:
#        print (current_time)
        break
    current_time +=30
hours = current_time//60
Alarm_Ring = print(start + hours)
#print(hours)
