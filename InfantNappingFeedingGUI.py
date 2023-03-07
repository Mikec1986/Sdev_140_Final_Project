# Michael Coughlin
# GUI Baby Tracker
# version 1.0
# This program will record an infant's naps and feedings.
# Descriptions of each sub below

import tkinter as tk
from tkinter import *
from tkinter import font
import time
from tkinter import messagebox

babyapp = tk.Tk()

# This is the welcome message only displayed on the welcome page.
welcome = """
Welcome to the Baby Tracking App.
Please select the activity that you would like to track
"""
# This is the Napping message only displayed on the welcome page.
nappingmessage = """
Select Count up to start an increasing timer.
Specify a time to count down.
Stop will pause the timer and finish will calculate the results!
"""
# This is the Feeding message only displayed on the Feeding page.
feedingmessage = """
Press Count Up to start the timer. Stop will pause the count.
Finish will output your stats!
Input the ounces to calculate the infant's rate.
"""

# Declarations
style1 = font.Font(size=15)
style2 = font.Font(size=20)
style3 = font.Font(size=14)
second1 = tk.StringVar()
minute1 = tk.StringVar()
hour1 = tk.StringVar()
ounces1 = tk.StringVar()
second1.set("00")
minute1.set("00")
hour1.set("00")
ounces1.set("0.0")
doTick = True
down = False


# Logic for the timer to count up.
def TimerUp():
    timer1 = 0
    timer1 = 0
    minute2 = 0
    hour2 = 0
    Pause = 0
    while timer1 > -1:
        feeding_page.stopb['state'] = "normal"
        napping_page.countd_b['state'] = "disabled"
        if not doTick:
            return
        time.sleep(1)
        timer1 += 1
        if timer1 == 60:
            minute2 += 1
            timer1 = 0
        if minute2 == 60:
            hour2 += 1
            minute2 = 0
        second1.set(str(timer1))
        minute1.set(str(minute2))
        hour1.set(str(hour2))
        babyapp.update()
    return


# Logic for the Countdown Timer
def TimerDown():
    global hourm
    global hour2
    global minutem
    global minute2
    global secondm
    global second2
    timer1 = (int(hour1.get()) * 3600) + (int(minute1.get()) * 60) + int(second1.get())
    hour2 = int(hour1.get())
    minute2 = int(minute1.get())
    second2 = int(second1.get())
    hourm = hour2
    minutem = minute2
    secondm = second2
    while timer1 > 0:
        napping_page.nstopb['state'] = "normal"
        napping_page.countup_b['state'] = "disabled"
        if not doTick:
            return
        time.sleep(1)
        timer1 -= 1
        if second2 == 0:
            if minute2 == 0:
                if hour2 > 0:
                    hour2 -= 1
                    minute2 = 59
                    second2 = 59
            elif minute2 > 0:
                minute2 -= 1
                second2 = 59
        else:
            second2 -= 1
        second1.set(str(second2))
        minute1.set(str(minute2))
        hour1.set(str(hour2))
        babyapp.update()
        if timer1 == 0:
            napping_page.nstopb['state'] = "disabled"
            if timer1 == 0:
                if hourm > 0:
                    if minutem == 0:
                        if secondm == 0:
                            timerupm = "Wow. The nap lasted " + str(hourm) + "hour(s) long"
                            messagebox.showinfo("Time", timerupm)
                            second1.set("00")
                            minute1.set("00")
                            hour1.set("00")
                            napping_page.countup_b['state'] = "normal"
                            napping_page.nstopb['state'] = "disabled"
                            napping_page.home_b['state'] = "normal"
                            napping_page.feeding_b2['state'] = "normal"
                            feeding_page.home_b2['state'] = "normal"
                            feeding_page.napping_b2['state'] = "normal"
                            return
                        elif secondm > 0:
                            timerupm = "Wow. The nap lasted " + str(hourm) + "hour(s) and" + str(
                                secondm) + " second(s) long"
                            messagebox.showinfo("Time", timerupm)
                            second1.set("00")
                            minute1.set("00")
                            hour1.set("00")
                            napping_page.countup_b['state'] = "normal"
                            napping_page.nstopb['state'] = "disabled"
                            napping_page.home_b['state'] = "normal"
                            napping_page.feeding_b2['state'] = "normal"
                            feeding_page.home_b2['state'] = "normal"
                            feeding_page.napping_b2['state'] = "normal"
                            return
                    elif minutem > 0:
                        if secondm == 0:
                            timerupm = "Wow. The nap lasted " + str(hourm) + "hour(s) and" + str(
                                minutem) + "minute(s) long"
                            messagebox.showinfo("Time", timerupm)
                            second1.set("00")
                            minute1.set("00")
                            hour1.set("00")
                            napping_page.countup_b['state'] = "normal"
                            napping_page.nstopb['state'] = "disabled"
                            napping_page.home_b['state'] = "normal"
                            napping_page.feeding_b2['state'] = "normal"
                            feeding_page.home_b2['state'] = "normal"
                            feeding_page.napping_b2['state'] = "normal"
                            return
                        elif secondm > 0:
                            timerupm = "Wow. The nap lasted " + str(hourm) + "hour(s)," + str(
                                minutem) + "minute(s) and" + str(secondm) + "second(s) long"
                            messagebox.showinfo("Time", timerupm)
                            second1.set("00")
                            minute1.set("00")
                            hour1.set("00")
                            napping_page.countup_b['state'] = "normal"
                            napping_page.nstopb['state'] = "disabled"
                            napping_page.home_b['state'] = "normal"
                            napping_page.feeding_b2['state'] = "normal"
                            feeding_page.home_b2['state'] = "normal"
                            feeding_page.napping_b2['state'] = "normal"
                            return
                elif hourm == 0:
                    if minutem > 0:
                        if secondm == 0:
                            timerupm = "Wow. The nap lasted " + str(minutem) + "minute(s) long"
                            messagebox.showinfo("Time", timerupm)
                            second1.set("00")
                            minute1.set("00")
                            hour1.set("00")
                            napping_page.countup_b['state'] = "normal"
                            napping_page.nstopb['state'] = "disabled"
                            napping_page.home_b['state'] = "normal"
                            napping_page.feeding_b2['state'] = "normal"
                            feeding_page.home_b2['state'] = "normal"
                            feeding_page.napping_b2['state'] = "normal"
                            return
                        elif secondm > 0:
                            timerupm = "Wow. The nap lasted " + str(minutem) + "minute(s) and" + str(
                                secondm) + " second(s) long"
                            messagebox.showinfo("Time", timerupm)
                            second1.set("00")
                            minute1.set("00")
                            hour1.set("00")
                            napping_page.countup_b['state'] = "normal"
                            napping_page.nstopb['state'] = "disabled"
                            napping_page.home_b['state'] = "normal"
                            napping_page.feeding_b2['state'] = "normal"
                            feeding_page.home_b2['state'] = "normal"
                            feeding_page.napping_b2['state'] = "normal"
                            return
                    elif minutem == 0:
                        timerupm = "Wow. The nap lasted " + str(secondm) + " second(s) long"
                        messagebox.showinfo("Time", timerupm)
                        second1.set("00")
                        minute1.set("00")
                        hour1.set("00")
                        napping_page.countup_b['state'] = "normal"
                        napping_page.nstopb['state'] = "disabled"
                        napping_page.home_b['state'] = "normal"
                        napping_page.feeding_b2['state'] = "normal"
                        feeding_page.home_b2['state'] = "normal"
                        feeding_page.napping_b2['state'] = "normal"
                        return
    second1.set("00")
    minute1.set("00")
    hour1.set("00")
    napping_page.countup_b['state'] = "normal"
    napping_page.nstopb['state'] = "disabled"
    napping_page.home_b['state'] = "normal"
    napping_page.feeding_b2['state'] = "normal"
    feeding_page.home_b2['state'] = "normal"
    feeding_page.napping_b2['state'] = "normal"
    return


# input verification for timer fields
def isinteger(field):
    try:
        int(field)
    except ValueError:
        return True


# Input verification for ounces field
def isfloat(field):
    try:
        float(field)
    except ValueError:
        return True


# Logic to stop the count down timer on the Napping page
def nStopd():
    global doTick
    doTick = False
    napping_page.home_b['state'] = "normal"
    napping_page.feeding_b2['state'] = "normal"
    feeding_page.home_b2['state'] = "normal"
    feeding_page.napping_b2['state'] = "normal"
    napping_page.nstopb['state'] = "disabled"
    feeding_page.stopb['state'] = "disabled"
    return


# Logic to stop the count up timer on the Napping page
def nStopu():
    global doTick
    doTick = False
    napping_page.nfinishb['state'] = "normal"
    napping_page.home_b['state'] = "normal"
    napping_page.feeding_b2['state'] = "normal"
    feeding_page.home_b2['state'] = "normal"
    feeding_page.napping_b2['state'] = "normal"
    napping_page.nstopb['state'] = "disabled"
    feeding_page.stopb['state'] = "disabled"
    return


# Logic to stop the count up timer on the Feeding page
def fStopup():
    global doTick
    doTick = False
    feeding_page.finishb['state'] = "normal"
    napping_page.home_b['state'] = "normal"
    napping_page.feeding_b2['state'] = "normal"
    feeding_page.home_b2['state'] = "normal"
    feeding_page.napping_b2['state'] = "normal"
    napping_page.nstopb['state'] = "disabled"
    feeding_page.stopb['state'] = "disabled"
    return


# Logic for the finish button on the Feeding page
def finish():
    if not isfloat(ounces1.get()):
        ounces = ounces1.get()
        if float(ounces) > 0:
            fedcalc = '{0:.2f}'.format(float((ounces1.get())) / (int(minute1.get()) + (int(second1.get()) / 60)))
            bottlemessage = "Your infant drank " + str(ounces1.get()) + " ounces at a rate of " + str(
                fedcalc) + " ounces per minute!"
            messagebox.showinfo("Fed Timer", bottlemessage)
        else:
            if int(minute1.get()) == 0:
                bottlemessage = "Your infant was fed for " + str(second1.get()) + " seconds!"
                messagebox.showinfo("Fed Timer", bottlemessage)
            else:
                bottlemessage = "Your infant was fed for " + str(minute1.get()) + "minute(s) and " + str(
                    second1.get()) + " seconds!"
                messagebox.showinfo("Fed Timer", bottlemessage)
        second1.set("00")
        minute1.set("00")
        hour1.set("00")
        ounces1.set("00")
        feeding_page.stopb['state'] = "disabled"
        feeding_page.finishb['state'] = "disabled"
        return
    else:
        messagebox.showinfo("Error", "The character entered is not a floating point number. \n"
                                     "Please enter a floating point number like 2.5")
        second1.set("00")
        minute1.set("00")
        hour1.set("00")
        ounces1.set("00")
        return


# Logic for the finish button on the Napping Page
def nfinish():
    if down:
        if hourm - hour2 == 0:
            if minutem - minute2 == 0:
                if secondm - second2 == 0:
                    return
                else:
                    nfinishd_mess = "Wow! The nap lasted for " + str((secondm - second2)) + " seconds!"
                    messagebox.showinfo("Nap Timer", nfinishd_mess)
            else:
                nfinishd_mess = "Wow! The nap lasted for " + str((minutem - minute2)) + " minutes and " + str(
                    (secondm - second2)) + " seconds!"
                messagebox.showinfo("Nap Timer", nfinishd_mess)
        else:
            nfinishd_mess = "Wow! The nap lasted for " + str((hourm - hour2)) + " hour(s), " + str(
                (minutem - minute2)) + " minutes, and " + str(
                (secondm - second2)) + " seconds!"
            messagebox.showinfo("Nap Timer", nfinishd_mess)
    else:
        if int(hour1.get()) == 0:
            if int(minute1.get()) == 0:
                napUpm = "Wow! The nap lasted for " + str(second1.get()) + " seconds!"
                messagebox.showinfo("Nap Timer", napUpm)
            else:
                napUpm = "Wow! The nap lasted for " + str(minute1.get()) + " minute(s) and " + str(
                    second1.get()) + " seconds!"
                messagebox.showinfo("Nap Timer", napUpm)
        else:
            napUpm = "Wow! The nap lasted for " + str(hour1.get()) + " hour(s), " + str(
                minute1.get()) + " minute(s) and " + str(second1.get()) + " seconds!"
            messagebox.showinfo("Nap Timer", napUpm)
    second1.set("00")
    minute1.set("00")
    hour1.set("00")
    napping_page.nstopb['state'] = "disabled"
    napping_page.countd_b['state'] = "normal"
    napping_page.nfinishb['state'] = "disabled"
    return


# Logic to start the count down timer
def Startd():
    global doTick
    global down
    if not isinteger(second1.get()):
        if not isinteger(minute1.get()):
            if not isinteger(hour1.get()):
                doTick = True
                down = True
                napping_page.nstopb['state'] = "normal"
                napping_page.home_b['state'] = "disabled"
                napping_page.feeding_b2['state'] = "disabled"
                feeding_page.home_b2['state'] = "disabled"
                feeding_page.napping_b2['state'] = "disabled"
                TimerDown()
            else:
                messagebox.showinfo("Error",
                                             "The character entered is not an integer. Please enter an integer")
        else:
            messagebox.showinfo("Error", "The character entered is not an integer. Please enter an integer")
    else:
        messagebox.showinfo("Error", "The character entered is not an integer. Please enter an integer")


# Logic to start the Count up Timer
def Startu():
    global doTick
    doTick = True
    napping_page.nstopb['state'] = "normal"
    napping_page.home_b['state'] = "disabled"
    napping_page.feeding_b2['state'] = "disabled"
    feeding_page.home_b2['state'] = "disabled"
    feeding_page.napping_b2['state'] = "disabled"
    TimerUp()


# Logic to switch to Home page
def homecall():
    home.tkraise()
    return


# Logic to switch to Napping page
def napping():
    second1.set("00")
    minute1.set("00")
    hour1.set("00")
    ounces1.set("00")
    napping_page.nstopb['state'] = "disabled"
    napping_page.nfinishb['state'] = "disabled"
    Napping.tkraise()
    return


# Logic to switch to Feeding Page
def feeding():
    second1.set("00")
    minute1.set("00")
    hour1.set("00")
    ounces1.set("0.0")
    feeding_page.stopb['state'] = "disabled"
    feeding_page.finishb['state'] = "disabled"
    napping_page.countd_b['state'] = "normal"
    Feeding.tkraise()
    return


# Quit button logic
def Quit():
    babyapp.destroy()
    return


# Frame Creation
home = Frame(babyapp, borderwidth=0, highlightthickness=0)
Napping = Frame(babyapp, borderwidth=0, highlightthickness=0)
Feeding = Frame(babyapp, borderwidth=0, highlightthickness=0)
# Frame Placement
home.grid(row=0, column=0, sticky="nsew")
Napping.grid(row=0, column=0, sticky="nsew")
Feeding.grid(row=0, column=0, sticky="nsew")


# Home Page labels, picture, and buttons grouping
class home_page:

    home_label = Label(home, text=welcome, font=style2)
    home_label.pack(pady=20)

    babyhome = PhotoImage(file=r"images\\babysmile.PNG")
    home_pic = Label(home, image=babyhome)
    home_pic.pack()

    napping_b = Button(home, text="Napping", command=napping)
    napping_b.place(x=50, y=500)

    feeding_b = Button(home, text="Feeding", command=feeding)
    feeding_b.place(x=550, y=500)

    quit_b = Button(home, text="Quit", command=Quit)
    quit_b.pack(side="bottom")


# Napping page picture, buttons, labels, and entries grouping
class napping_page:
    napping_label = Label(Napping, text=nappingmessage, font=style1)
    napping_label.pack(pady=5)

    babynap = PhotoImage(file=r"images\\baby1.PNG")
    nap_pic = Label(Napping, image=babynap)
    nap_pic.pack()

    sec_entry = Entry(Napping, textvariable=second1, width=2)
    sec_entry.place(x=380, y=450)

    sec_label = Label(Napping, text="seconds")
    sec_label.place(x=400, y=450)

    min_entry = Entry(Napping, textvariable=minute1, width=2)
    min_entry.place(x=310, y=450)

    min_label = Label(Napping, text="minutes")
    min_label.place(x=330, y=450)

    hour_entry = Entry(Napping, textvariable=hour1, width=2)
    hour_entry.place(x=240, y=450)

    hour_label = Label(Napping, text="hours")
    hour_label.place(x=260, y=450)

    countup_b = Button(Napping, text="Count Up", command=Startu, width=10)
    countup_b.place(x=240, y=500)

    countd_b = Button(Napping, text="Count Down", command=Startd, width=10)
    countd_b.place(x=325, y=500)

    nstopb = Button(Napping, text="Stop", state="disabled", command=nStopu)
    nstopb.place(x=270, y=472)

    nfinishb = Button(Napping, text="Finish", state="disabled", command=nfinish, width=10)
    nfinishb.place(x=310, y=472)

    home_b = Button(Napping, text="Home", command=homecall)
    home_b.place(x=50, y=525)

    feeding_b2 = Button(Napping, text="Feeding", command=feeding)
    feeding_b2.place(x=550, y=525)

    quit_b = Button(Napping, text="Quit", command=Quit)
    quit_b.pack(side="bottom")


# Feeding page picture, buttons, labels, and entries grouping
class feeding_page:
    feeding_label = Label(Feeding, text=feedingmessage, font=style3)
    feeding_label.pack(pady=10)

    babybottle = PhotoImage(file=r"images\\babybottle.PNG")
    feeding_pic = Label(Feeding, image=babybottle)
    feeding_pic.pack()

    oz_entry = Entry(Feeding, textvariable=ounces1, width=4)
    oz_entry.place(x=150, y=460)

    oz_label = Label(Feeding, text="ounces")
    oz_label.place(x=170, y=460)

    sec_entry = Entry(Feeding, textvariable=second1, width=2)
    sec_entry.place(x=380, y=460)

    sec_label = Label(Feeding, text="seconds")
    sec_label.place(x=400, y=460)

    min_entry = Entry(Feeding, textvariable=minute1, width=2)
    min_entry.place(x=300, y=460)

    min_label = Label(Feeding, text="minutes")
    min_label.place(x=320, y=460)

    countup_b = Button(Feeding, text="Count Up", command=Startu, width=10)
    countup_b.place(x=175, y=500)

    stopb = Button(Feeding, text="Stop", state="disabled", command=fStopup, width=10)
    stopb.place(x=275, y=500)

    finishb = Button(Feeding, text="Finish", state="disabled", command=finish, width=10)
    finishb.place(x=375, y=500)

    home_b2 = Button(Feeding, text="Home", command=homecall)
    home_b2.pack(padx=45, pady=45, side="left")

    napping_b2 = Button(Feeding, text="Napping", command=napping)
    napping_b2.pack(padx=45, pady=0, side="right")

    quit_b = Button(Feeding, text="Quit", command=Quit)
    quit_b.pack(side="bottom")


# start and build tkinter window
home.tkraise()
babyapp.geometry("650x600")
babyapp.title("The Baby Tracking App")
babyapp.resizable(False, False)
babyapp.mainloop()
