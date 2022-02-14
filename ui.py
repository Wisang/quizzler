import tkinter

THEME_COLOR = "#375362"


class QuizzlerUI:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas.create_text(150, 125, text="quiz here",
                                font=("Arial", 20, "italic"), fill="black")

        self.label = tkinter.Label(text="score: ", bg=THEME_COLOR,
                                   font=("Arial", 20, "normal"))
        self.label.grid(row=0, column=1)

        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image= true_img)
        self.true_button.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image= false_img)
        self.false_button.grid(row=2, column=1)




        self.window.mainloop()