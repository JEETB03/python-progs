import turtle
import pandas

## Configurations
screen = turtle.Screen()
screen.title("Guess the US. State!")
image = "pandas library/states game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

## reading files to check for the answer
data = pandas.read_csv("pandas library/states game/50_states.csv")
all_states = data.state.to_list()         ## pulls the list of states and converts it into a list.

guesses = []                              ## stores all the user answers


while len(guesses) < 50:
    """Game continuation logic. Keeps the game running until user guesses all the states."""
## answering prompt
    answer_state = screen.textinput(title=f"{len(guesses)}/50 States correct", prompt="What's another state name").title() 

    if answer_state == "Exit":
        """Ends the game if user types exit and creates a new csv files of all the states not answered."""
        missing_states = [state for state in all_states if state not in guesses]   ### iterates all over the all states list and check for states not present in the guesses list. 
        new_data = pandas.DataFrame(missing_states)                                ### captures the missed states
        new_data.to_csv("pandas library/states game/missing_states.csv")           ### converts it into a csv file
        break                                                                      ### ends the game
    
    elif answer_state in all_states:
        """If answered correctly then turtle prints the name of the state on the state location on the map and continues the game until all 50 states are answered correctly."""
        guesses.append(answer_state)                          ### adds answers to guesses list every time user answers correctly
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_check = data[data.state == answer_state]        ### checks for user answer and matches with the state list
        t.goto(state_check.x.item(), state_check.y.item())    ### turtle goes to the respective coordinates of the answered state
        t.write(state_check.state.item())                     ### writes the name of the state in that coordinate




screen.exitonclick()