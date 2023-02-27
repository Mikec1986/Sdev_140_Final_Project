#Michael Coughlin
#GUI Baby Tracker
#version 1.0
#This will record an infant's naps and feedings
#Work In Progress

import tkinter as tk
from tkinter import ttk
import time
from PIL import ImageTk, Image


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill= "both", expand=False)

        container.grid_rowconfigure(0, {'minsize': 50})
        container.grid_columnconfigure(0, {'minsize': 15})

        self.frames = {}

        for F in (home_page, Napping, Feeding):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row= 5, column= 4, sticky="nsew")

        self.show_frame(home_page)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class home_page(tk.Frame):
    # Defines the homepage
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        image2 = Image.open("C:\\Users\\aDirt\\PycharmProjects\\images\\baby1.jpg")
        image1 = tk.PhotoImage(file=r"C:\\Users\\aDirt\\PycharmProjects\\images\\babynap.PNG")
        resized = image2.resize((400,400))
        img = ImageTk.PhotoImage(resized)
        background_image = tk.Label(self, image=img)

        background_image.grid()
        labelh = ttk.Label(self,text="Newborn Baby Tracking!", font="Verdana")
        labelh.grid(row=0, column = 4, padx= 10, pady=10)
        mpLabel1= tk.Label(self, text="Welcome! Please select the activity you would like to track.", background="gray", fg="lightblue", height= 1, borderwidth=3)
        mpLabel1.grid(row=3, columnspan=10, padx=10, pady=10)
        napB = ttk.Button(self, text="Nap Tracking",
                          command= lambda : controller.show_frame(Napping))
        napB.grid(row=4, column=2, padx=10, pady=10)
        feedB = ttk.Button(self, text="Bottle Tracking",
                           command=lambda: controller.show_frame(Feeding))
        feedB.grid(row=4, column=6, padx=10, pady=10)


class Napping(tk.Frame):
    # Defines the napping page
    def __init__(self, parent, controller):
        #Timer Logic (Not Complete)
        def TimerUp():
            timer1 = 0
            if int(hour1.get()) > 0 or int(minute1.get()) > 0 or int(second1.get()) > 0:
                timerCount = (int(hour1.get()) * 3600) + (int(minute1.get()) * 60) + int(second1.get())
                timer1 = 0
                minute2 = 0
                hour2 = 0
                Pause = 0
                second1.set("00")
                minute1.set("00")
                hour1.set("00")

                while timer1 < timerCount:
                    if Pause == 0:
                        tkinterApp.update(self)
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
                    else:
                        time.sleep(0)
            else:
                timer1 = 0
                minute2 = 0
                hour2 = 0
                Pause = 0
                while timer1 > -1:
                    if Pause > 0:
                        check = 1

                    else:
                        tkinterApp.update(self)
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

        #Countdown Timer Logic (Not Complete)
        def TimerDown():
            timer1 = 0
            timer1 = (int(hour1.get()) * 3600) + (int(minute1.get()) * 60) + int(second1.get())
            hour2 = int(hour1.get())
            minute2 = int(minute1.get())
            second2 = int(second1.get())
            while timer1 >= 0:
                tkinterApp.update(self)
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

        tk.Frame.__init__(self, parent)
        second1 = tk.StringVar()
        minute1 = tk.StringVar()
        hour1 = tk.StringVar()
        second1.set("00")
        minute1.set("00")
        hour1.set("00")

        homeB = ttk.Button(self, text="Home",
                           command=lambda: controller.show_frame(home_page))
        homeB.grid(row=1, column=3, padx=10, pady=10)
        labelN = ttk.Label(self, text= "Nap Tracking")
        labelN.grid(row=0, column=4, padx=10, pady=10)
        timerS = tk.Entry(self, textvariable=second1, width=2)
        timerS.grid(row=4, column=0)
        timerM = tk.Entry(self, textvariable=minute1, width=2)
        timerM.grid(row=4, column=1, padx=0, pady=0)
        timerH = tk.Entry(self, textvariable=hour1, width=2)
        timerH.grid(row=4, column=2, padx=0, pady=0)
        countUp = ttk.Button(self, text="Count Up", command=TimerUp)
        countUp.grid(row=5, column=1, padx=10, pady=10)
        countDown = ttk.Button(self, text="Count Down", command=TimerDown)
        countDown.grid(row=5, column=4, padx=10, pady=10)


class Feeding(tk.Frame):
    #Defines Feeding Page
    def __init__(self, parent, controller):

        def TimerUp():
            timer1 = 0
            if int(hour1.get()) > 0 or int(minute1.get()) > 0 or int(second1.get()) > 0:
                timerCount = (int(hour1.get()) * 3600) + (int(minute1.get()) * 60) + int(second1.get())
                timer1 = 0
                minute2 = 0
                hour2 = 0
                Pause = 0
                second1.set("00")
                minute1.set("00")
                hour1.set("00")
                pause1 = ttk.Button(text="Pause", state="normal")
                pause1.pack()
                if pause1 == True:
                    Pause = 1
                    # babyapp.pause1['state'] = "disabled"
                    resume1 = tk.Button(text="Resume", state="normal")
                    resume1.pack()
                else:
                    resume1 = tk.Button(text="Resume", state="disabled")
                    resume1.pack()
                while timer1 < timerCount:
                    if Pause == 0:
                        tkinterApp.update(self)
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
                    else:
                        time.sleep(0)
            else:
                timer1 = 0
                minute2 = 0
                hour2 = 0
                Pause = 0
                pause1 = ttk.Button(text="Pause", command=PauseB)
                pause1.pack()
                while timer1 > -1:
                    if Pause > 0:
                        check = 1

                    else:
                        tkinterApp.update(self)
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

        def TimerDown():
            hour1 = tk.StringVar()
            minute1 = tk.StringVar()
            second1 = tk.StringVar()

            timer1 = 0
            timer1 = (int(hour1.get()) * 3600) + (int(minute1.get()) * 60) + int(second1.get())
            hour2 = int(hour1.get())
            minute2 = int(minute1.get())
            second2 = int(second1.get())
            while timer1 >= 0:
                tkinterApp.update(self)
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

        def PauseB():
            Pause = 1
            resume1 = tk.Button(text="Resume", command=Continue)

        def Continue():
            Pause = 0

        hour1 = tk.StringVar()
        minute1 = tk.StringVar()
        second1 = tk.StringVar()
        hour1.set("00")
        minute1.set("00")
        second1.set("00")
        timer1 = 0
        tk.Frame.__init__(self, parent)
        labelN = ttk.Label(self, text="Nap Tracking")
        labelN.grid(row=0, column=4, padx=10, pady=10)

        timerS = tk.Entry(self, textvariable=second1, width=2)
        timerS.grid(row=4, column=0)
        timerM = tk.Entry(self, textvariable=minute1, width=2)
        timerM.grid(row=4, column=1, padx=0, pady=0)
        timerH = tk.Entry(self, textvariable=hour1, width=2)
        timerH.grid(row=4, column=2, padx=0, pady=0)
        countUp = ttk.Button(self, text="Count Up", command=TimerUp)
        countUp.grid(row=5, column=1, padx=10, pady=10)
        countDown = ttk.Button(self, text="Count Down", command=TimerDown)
        countDown.grid(row=5, column=4, padx=10, pady=10)


app = tkinterApp()
app.mainloop()