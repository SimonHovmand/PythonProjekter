from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Digital clock")
app_window.geometry("960x60")
app_window.resizable(1,1)

text_font = ("Boulder", 35, "bold")
background = "#fff"
foregrund = "#000"
border_with = 1

label = Label(app_window, font=text_font, bg=background, fg=foregrund, bd=border_with)
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%a %d. %B %y - %H:%M:%S - Day %j" )
    label.config(text=time_live)
    label.after(20, digital_clock)

digital_clock()
app_window.mainloop()