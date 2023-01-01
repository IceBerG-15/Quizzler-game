from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT=('Arial',20,'italic')

class UI():
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label=Label(text='Score:0',bg=THEME_COLOR,highlightthickness=0,fg='white',font=(20))
        self.score_label.grid(column=1,row=0)


        self.canvas=Canvas(width=300,height=250)
        self.question_text=self.canvas.create_text(
            150,
            125,
            width=280,
            text='I am a quizzler.',
            font=FONT)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        
        #calling next_question function
        self.get_next_question()

        true_img=PhotoImage(file='.\\images\\true.png')
        self.true_button=Button(
            image=true_img,
            highlightthickness=0,
            command=self.is_true
            )
        self.true_button.grid(column=0,row=2)


        false_img=PhotoImage(file='.\\images\\false.png')
        self.false_button=Button(
            image=false_img,
            highlightthickness=0,
            command=self.is_false
            )
        self.false_button.grid(column=1,row=2)


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f'Score:{self.quiz.score}')
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reachde the last question.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def is_true(self):
        is_right=self.quiz.check_answer('True')
        self.give_feedback(is_right)
    
    def is_false(self):
        is_right=self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self,output:bool):
        if output:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)
