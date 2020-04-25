# Class for displaying the main GUI
from tkinter import *


class Layout:

    def create_grid(self, canvas):
        canvas.create_line(2, 2, 800, 2)
        canvas.create_line(2, 63, 800, 63)
        canvas.create_line(2, 124, 800, 124)
        canvas.create_line(2, 185, 800, 185)
        canvas.create_line(2, 242, 800, 242)
        canvas.create_line(2, 302, 800, 302)
        canvas.create_line(2, 362, 800, 362)
        canvas.create_line(2, 422, 800, 422)
        canvas.create_line(2, 482, 800, 482)
        canvas.create_line(2, 542, 800, 542)
        canvas.create_line(2, 602, 800, 602)
        canvas.create_line(2, 662, 800, 662)
        canvas.create_line(2, 722, 800, 722)
        canvas.create_line(2, 782, 800, 782)
        canvas.create_line(2, 842, 800, 842)
        canvas.create_line(2, 902, 800, 902)
        canvas.create_line(2, 2, 2, 902)
        canvas.create_line(135, 2, 135, 902)
        canvas.create_line(268, 2, 268, 902)
        canvas.create_line(401, 2, 401, 902)
        canvas.create_line(534, 2, 534, 902)
        canvas.create_line(667, 2, 667, 902)
        canvas.create_line(800, 2, 800, 902)

    def create_weekdays(self, canvas):
        Time = canvas.create_text(70, 30, font="LARGE", text="Time")
        Monday = canvas.create_text(200, 30, font="LARGE", text="Monday")
        Tuesday = canvas.create_text(335, 30, font="LARGE", text="Tuesday")
        Wednesday = canvas.create_text(470, 30, font="LARGE", text="Wednesday")
        Thursday = canvas.create_text(600, 30, font="LARGE", text="Thursday")
        Friday = canvas.create_text(730, 30, font="LARGE", text="Friday")

    def create_time(self, canvas):
        time1 = canvas.create_text(70, 93, font="LARGE", text="8:00-9:00")
        time2 = canvas.create_text(70, 153, font="LARGE", text="9:00-10:00")
        time3 = canvas.create_text(70, 213, font="LARGE", text="10:00-11:00")
        time4 = canvas.create_text(70, 273, font="LARGE", text="11:00-12:00")
        time5 = canvas.create_text(70, 333, font="LARGE", text="12:00-13:00")
        time6 = canvas.create_text(70, 393, font="LARGE", text="13:00-14:00")
        time7 = canvas.create_text(70, 453, font="LARGE", text="14:00-15:00")
        time8 = canvas.create_text(70, 513, font="LARGE", text="15:00-16:00")
        time9 = canvas.create_text(70, 573, font="LARGE", text="16:00-17:00")
        time10 = canvas.create_text(70, 633, font="LARGE", text="17:00-18:00")
        time11 = canvas.create_text(70, 693, font="LARGE", text="18:00-19:00")
        time12 = canvas.create_text(70, 753, font="LARGE", text="19:00-20:00")
        time13 = canvas.create_text(70, 813, font="LARGE", text="20:00-21:00")
        time14 = canvas.create_text(70, 873, font="LARGE", text="21:00-22:00")

    def create_checkbuttons(self, master):
        Label(master, text="Modes:").grid(row=1, column=0)
        default = Checkbutton(master, text="Default").grid(row=1, column=1)
        delete = Checkbutton(master, text="Delete").grid(row=1, column=2)
        add = Checkbutton(master, text="Add").grid(row=1, column=3)

    def create_entry(self, master):
        Label(master, text="Enter Course Code").grid(row=0, columnspan=2)

    def add_course_code(self, master):

        Label(master, text=self.entry.get()).grid(row=0, column=4)

    def __init__(self, master):
        self.create_checkbuttons(master)
        self.create_entry(master)
        self.entry = Entry(master)
        self.entry.grid(row=0, column=2)
        self.button = Button(master, text="Add Course", command=lambda: self.add_course_code(master))
        self.button.grid(row=0, column=3)
        canvas = Canvas(master, width=800, height=910)
        canvas.grid(rowspan=60, columnspan=60)
        self.create_grid(canvas)
        self.create_weekdays(canvas)
        self.create_time(canvas)


root = Tk()
layout = Layout(root)
root.mainloop()
