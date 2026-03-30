import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")

guessed_states=[]
all_states=data.state.to_list()
missing_states=[]


while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"score{len(guessed_states)}/50 statesGuess the state",prompt="What's anothe states name")
    if answer_state=="exit":
        break
    answer_state=answer_state.title()
    guessed_states.append(answer_state)
    missing_states.clear()
    for state in all_states:
        if state not in guessed_states:
            missing_states.append(state)
    new_data=pandas.DataFrame(missing_states)
    new_data.to_csv("states to learn.csv")
    ans_x=data.x[data.state==answer_state]
    ans_y=data.y[data.state==answer_state]
    ans_x=ans_x.item()
    ans_y=ans_y.item()
    turtle.penup()
    turtle.goto(int(ans_x),int(ans_y))
    ans=turtle.write(answer_state,align="center",font="bold")
    turtle.setpos(x=0,y=0)

   