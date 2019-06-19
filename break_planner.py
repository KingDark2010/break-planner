# this app make u plan how many breaks u want to take during a study session or something ur doing
import time
import webbrowser

time_in_minutes = 60 
time_in_hours = 60*60


# time choice is a function that define if we will make break based on hours or minutes 
def timeChoice ():
    breakTime = input ("Do you want your breaks to be in:\n 1.Minutes \n 2.Hours\n")
    if int (breakTime) == 1:
        print ("your breaks will be counted in mins\n")
        return time_in_minutes
    elif int (breakTime) == 2:
        print ("your breaks will be counted in hours\n")
        return time_in_hours
    else :
        print ("please provide a valid option \n\n\n")
        return timeChoice()


#timing function sets the time we want to use
def timing ():
    theTime = input ("set the amount of mins/hours you want based on ur last answer\n\n")
    if int (theTime) <= 0 :
        print ("Please provide a valid number \n\n\n")
        return theTime
    elif int (theTime) > 0 and int (theTime) < 500:
        return int (theTime) 
    else :
        print ("number is too large\n")
        return timing()   


breakTime = timeChoice()

theTime = timing()

sleepTime = breakTime * theTime



#replay function sets the last thing so that the app is running in right way
def replay ():
    breakAmount = input ("How many breaks are u planing to take\n")
    if int (breakAmount) <= 0:
        print ("please provide a valid option \n\n\n")
        return replay()
    elif int (breakAmount) > 0 and int (breakAmount) < 10:
        for i in range(int (breakAmount)):
            time.sleep (int (sleepTime))
            webbrowser.open("https://www.youtube.com/watch?v=86sLUOnyCPs")
    else :
        print ("number is too high AKA you are not a robot xD\n")
        return replay()        



breakAmount = replay()
