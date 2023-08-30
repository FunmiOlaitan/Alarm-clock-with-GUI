#Install required modules and libraries to form alarm clock 
from tkinter import *
import time
import datetime
from pygame import mixer

def alarm(set_alarm_timer):                                   # function named alarm(), which performs alarm clock work.                 
    while True:                                               # Infinite Loop
# Wait for one second using time module
        time.sleep(1)                                         # Wait for one second using time module
        current_time = datetime.datetime.now()                # Get current time using datetime module
        timeNow = current_time.strftime("%H:%M:%S")           # convert the current time in strings
        dateNow = current_time.strftime("%d/%m/%Y")           # #convert the current date in strings
        print("The Set Date is:",dateNow)
        print(timeNow)
# Check whether set alarm timer is equal to current time or not
        if timeNow == set_alarm_timer:                            
            print("WAKE UP!")
            mixer.init()
# play sound using winsound module
            mixer.music.load()
            mixer.music.play()
            break
# Set Alarm 
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}" # User's value for setting the alarm in the string format
    alarm(set_alarm_timer)
    
# to create GUI Object
clock = Tk()                       # To Initialize tkinter

clock.title("Alarm Clock")         # The dialog box has the title as Alarm Clock
clock.geometry("400x200")          # "Alarm Clock" with a geometry of (400*200). 

# mention the time format for 24 hours using time_format.
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)

addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#creating input boxes for time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10).place(x =110,y=70)

clock.mainloop()
#Execution of the window.