import tkinter

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzlerUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="quiz here",
            font=("Arial", 20, "italic"),
            fill="black")

        self.score_label = tkinter.Label(text="score: ", bg=THEME_COLOR,
                                         font=("Arial", 16, "normal"))
        self.score_label.grid(row=0, column=1)

        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(
            image=true_img,
            command=self.on_true_button_clicked
        )
        self.true_button.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(
            image=false_img,
            command=self.on_false_button_clicked
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def on_true_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def on_false_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question())

