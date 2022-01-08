import random
import os
import time
myfile = open("dates.txt","a")



#for loop of  all months
for i in range(0, 480):
    #arrays
   print("Generating random no...")
   daysinamonth = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
   allmonths = [1,2,3,4,5,6,7,8,9,10,11,12]
   #all choices
   date = random.choice(daysinamonth)
   months = random.choice(allmonths)
   time.sleep(0.1)
   print("Writing file...")
   #changing it into string
   forwriting = str(date)
   formonths = str(months)
   myfile.write(forwriting + "/" + formonths + "/" + "2022" + " "+ "," + "" )
   print("Finished all files...")
