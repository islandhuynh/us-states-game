import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()

while len(states_list) > 0:
  answer_state = screen.textinput(title=f"{50 - len(states_list)}/ 50", prompt="What's another state's name?")
  if answer_state in states_list:
    states_list.remove(answer_state)
  if answer_state == "stop":
    break

def get_mouse_click_coor(x, y):
  print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()