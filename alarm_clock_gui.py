# Import necessary modules and libraries 
from tkinter import *
import time
import datetime
from pygame import mixer

# Function to perform alarm clock functionality
def alarm(set_alarm_timer):                                                    
    while True:                                               
        time.sleep(1)                                         
        current_time = datetime.datetime.now()                
        timeNow = current_time.strftime("%H:%M:%S")           
        dateNow = current_time.strftime("%d/%m/%Y")           
        print("The Set Date is:",dateNow)
        print(timeNow)
        
        # Check whether set alarm timer is equal to the current time or not
        if timeNow == set_alarm_timer:                            
            print("WAKE UP!")
            mixer.init()
            # Play sound using pygame.mixer
            mixer.music.load(r'C:/Users/funmi/GitRepositories/Alarm-clock-with-GUI/iPhoneAlarm.mp3')
            mixer.music.play()
            return
# Function to get user input and set the alarm
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

# Create the GUI window
clock = Tk()                       
clock.title("Alarm Clock")         
clock.geometry("400x200")           

# Label to display time format
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)

# Labels for input fields
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# Variables to store user input
hour = StringVar()
min = StringVar()
sec = StringVar()

# Entry widgets for user input
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

# Button to set the alarm
submit = Button(clock, text="Set Alarm", fg="red", width = 10, command=actual_time).place(x=110,y=70)

# Execute the GUI window
clock.mainloop()
