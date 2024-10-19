from tkinter import *
import random
from tkinter import messagebox

window=Tk()
window.title('Quiz game')
window.geometry("400x400")
window.config(background="black")

score = 0
answers = ["r","wrong","cold","candle","silence","bottle"]
questions = ["What is middle of Paris?","Which word is spelt wrong in every dictionary?","What can you catch but not throw?","I'm tall when I'm young but I'm short when I'm old, what am I?", "What is so fragile that saying its name breaks it?","What has a neck but no head?"]
counter = 0

def check():
    global score, counter
    user_answer = enter_answer.get()

    if user_answer == answers[counter]:
        messagebox.showinfo("correct","You got the correct answer!")
        score += 1
        score2.config(text=f"Score:{score}")
        enter_answer.delete(0,END)
        counter += 1
        chosen_question.config(text=questions[counter],fg="white")
    else:
        score -= 1
        messagebox.showinfo("wrong","You got it wrong, next question")
        score2.config(text=f"Score:{score}")
        enter_answer.delete(0,END)
        counter += 1
        chosen_question.config(text=questions[counter],fg="white")


score2 = Label(window,text="Score:{}".format(score),background="black",fg="white",font=("Aerial",16))
score2.place(x=50,y=300)
quiz_game = Label(window,text="quiz game",background="black",fg="white",font=("Aerial",16))
quiz_game.pack(side=TOP)

chosen_question = Label(window,text=questions[0],background="black",fg="white",font=("Aerial",12))
chosen_question.place(x=75,y=100)

enter_answer = Entry(window,width=30)
enter_answer.place(x=105,y=150,height=30)

check_button = Button(window,text="Check",command=check)
check_button.place(x=175,y=200)

window.mainloop()