import random
import os
import datetime
myfile = open("dates.csv","a")


#for loop of  all months
for i in range(0, 480):
    #arrays
   daysinamonth = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
   allmonths = [1,2,3,4,5,6,7,8,9,10,11,12]
   #all choices
   date = random.choice(daysinamonth)
   months = random.choice(allmonths)
   
   print(date)
   #changing it into string
   forwriting = str(date)
   formonths = str(months)
   myfile.write(forwriting + "/" + formonths + "/" + "2022" + " "+ "," + "" )