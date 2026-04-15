from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    df=pd.read_csv('data/Not_learnt.csv')
except FileNotFoundError:
    df=pd.read_csv('data/french_words.csv')
    to_learn=df.to_dict(orient="records")
else:
    to_learn=df.to_dict(orient="records")

current_card={}

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"])
    canvas.itemconfig(card_title,fill="black")
    canvas.itemconfig(card_word,fill="black")
    canvas.itemconfig(card_background,image=front_image)
    flip_timer=window.after(3000,flip_card)

def known_card():
    to_learn.remove(current_card)
    next_card()
    df1=pd.DataFrame(to_learn)
    df1.to_csv("data/Not_learnt.csv",index=False)
        
def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_image)
# -----------------------------------UI----------------------------------
window =Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
front_image=PhotoImage(file="images/card_front.png")
back_image=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=front_image)

card_title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))

card_word=canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

right_image= PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0,command=known_card)
right_button.grid(row=1,column=0)


wrong_image= PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=1)

next_card()
window.mainloop() 
