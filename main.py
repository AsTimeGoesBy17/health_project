import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import pandas as pd

from tkinter import Tk, Frame
from tkinter.ttk import Label, Button

LARGE_FONT = ('Verdana', 12)

DATA = pd.read_csv('C:\Python38\programy\zdrowie\BMI.csv')

def get_data_country(country):
    x = DATA[DATA['COUNTRY'] == country]['YEAR']
    y = DATA[DATA['COUNTRY'] == country]['VALUE']
    return (x, y)

def get_data_country_group(country_grp):
    x = DATA[DATA['COUNTRY_GRP'] == country_grp]['YEAR']
    y = DATA[DATA['COUNTRY_GRP'] == country_grp]['VALUE']
    return (x, y)


class HealthApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, 'Obesity')

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, CENTRAL_ASIA, RUSSIA, EU, POLAND, DEUTCHLAND):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        label = Label(self, text='HomePage', font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button1 = Button(self, text="CENTRAL_ASIA",
                        command=lambda: controller.show_frame(CENTRAL_ASIA))
        button1.pack()

        button2 = Button(self, text="RUSSIA",
                        command=lambda: controller.show_frame(RUSSIA))
        button2.pack()


        button3 = Button(self, text="EU",
                        command=lambda: controller.show_frame(EU))
        button3.pack()

        button4 = Button(self, text="POLAND",
                        command=lambda: controller.show_frame(POLAND))
        button4.pack()


        button5 = Button(self, text="DEUTCHLAND",
                        command=lambda: controller.show_frame(DEUTCHLAND))
        button5.pack()

        home_page_text = """



        Hello everyone :)

        I'd like to present you a change of BMI rate in a few exemplary countries from 1975 to 2016.

        Enjoy yourself while analysing figures.



        """

        welcome_text = Label(self, text=home_page_text) #dpoisać potem
        label.configure(anchor="center")
        welcome_text.pack()

class CENTRAL_ASIA(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        label = Label(self, text='CENTRAL_ASIA', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

        (x, y) = get_data_country_group('CARINFONET')
        a.plot(x, y)

class RUSSIA(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        label = Label(self, text='RUSSIA', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

        (x, y) = get_data_country('RUS')
        a.plot(x, y)

class DEUTCHLAND(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        label = Label(self, text='DEUTCHLAND', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

        (x, y) = get_data_country('DEU')
        a.plot(x, y)


class EU(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        label = Label(self, text='EU', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

        (x, y) = get_data_country_group('EU_MEMBERS')
        a.plot(x, y)

class POLAND(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        label = Label(self, text='POLAND', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

        (x, y) = get_data_country('POL')
        a.plot(x, y)

app = HealthApp()
app.mainloop()
