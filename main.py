import pandas
import turtle

STYLE = ("Comic Sans", 12, "normal")

screen = turtle.Screen()
screen.setup(width=1000, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()


while len(states_list) > 0:
  answer_state = screen.textinput(title=f"{50 - len(states_list)}/50", prompt="What's another state's name?").title()
  if answer_state in states_list:
    state_xcor = states_data[states_data["state"] == answer_state]["x"].to_list()[0]
    state_ycor = states_data[states_data["state"] == answer_state]["y"].to_list()[0]
    state_name = turtle.Turtle()
    state_name.hideturtle()
    state_name.penup()
    state_name.goto(x=state_xcor, y=state_ycor)
    state_name.write(answer_state, align="center")

    states_list.remove(answer_state)
  if answer_state == "stop":
    break

turtle.mainloop()