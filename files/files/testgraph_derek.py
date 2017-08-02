# NFL stats Derek and Brian

   
# Get the directory name for data files
import os.path

def compareDates(a,b):
    if (int(a[2])>int(b[2])):
        return False
    elif(int(a[2])<int(b[2])):
       return True        
    if(int(a[0])>int(b[0])):
        return False
    elif(int(a[0])<int(b[0])):
        return True       
    elif (int(a[1])>int(b[1])):
        return False
    elif(int(a[1])<int(b[1])):
        return True
    else:
        True


directory = os.path.dirname(os.path.abspath(__file__)) 
   
#initialize the aggregators
weeksPass=[]
weeksRun=[]
run_count = 0
pass_count = 0
yearNumber  = 1
weeks = 0
weekends = ["9/13/2015", "9/20/2015", "9/27/2015", "10/4/2015","10/11/2015","10/18/2015","10/25/2015","11/1/2015","11/8/2015","11/15/2015","11/22/2015","11/29/2015","12/6/2015","12/13/2015","12/20/2015","12/27/2015","1,6,2016"]
newyear = weekends[0]
    
# Collect data for one year at a time
weeksdata = []


# Open the file
filename = os.path.join(directory, 'NFL2015.csv')
datafile = open(filename, 'r')
# Go through all the weeks in that year
newdate1 = newyear.split('/')

totalRecords = 0

for line in datafile:
        totalRecords += 1    
        year, playType = line.split(',')         # collect year and type of play

        newdate2 = year.split('/')
        
        if compareDates(newdate2,newdate1):     # Is date earlier
            if 'Run' in playType:
                run_count += 1
            elif 'Pass' in playType:
                pass_count += 1
        else:        
            weeksdata.append(yearNumber)
            weeksRun.append(run_count)
            weeksPass.append(pass_count)
            if yearNumber < 17:
                yearNumber += 1
            if yearNumber != 17:
                print "toal records "+str(totalRecords)+" number of weeks "+str(yearNumber)
            if totalRecords > 5948 and totalRecords < 5961:
                print newdate2, newdate1
            run_count = 0
            pass_count = 0
            if yearNumber < 17:
                newyear = weekends[(yearNumber-1)]
                print newyear
                newdate1 = newyear.split('/')            
            #print yearNumber


# Close that year's file
datafile.close()

#print weeksdatas
#print weeksRun
#print weeksPas
print weekends
    


  
# Plot on one set of axes.
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot(weeksdata, weeksRun, '#0000FF')       # years and number of runs
ax.plot(weeksdata, weeksPass, '#FF00FF')       # years and number of passes  
  
ax.set_title('Number of play types each week Run(blue) or Pass(pink)')
fig.show()