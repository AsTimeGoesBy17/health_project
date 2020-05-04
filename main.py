from tkinter import Tk, Frame
from tkinter.ttk import Label, Button

LARGE_FONT = ('Verdana', 12)

class HealthApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, 'Obesity')

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, WORLD, USA, EU, POLAND):
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


        button1 = Button(self, text="WORLD",
                        command=lambda: controller.show_frame(WORLD))
        button1.pack()

        button2 = Button(self, text="USA",
                        command=lambda: controller.show_frame(USA))
        button2.pack()


        button3 = Button(self, text="EU",
                        command=lambda: controller.show_frame(EU))
        button3.pack()

        button4 = Button(self, text="POLAND",
                        command=lambda: controller.show_frame(POLAND))
        button4.pack()

        welcome_text = Label(self, text='hgfgh') #dpoisać potem
        welcome_text.pack()

class WORLD(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        label = Label(self, text='WORLD', font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

class USA(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        label = Label(self, text='USA', font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

class EU(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        label = Label(self, text='EU', font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

class POLAND(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        label = Label(self, text='POLAND', font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

app = HealthApp()
app.geometry('500x400')
app.mainloop()
