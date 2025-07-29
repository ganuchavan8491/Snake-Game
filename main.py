from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - Keyboard Selection")
screen.tracer(0)

levels = [("Easy", 0.15, "green"), ("Medium", 0.10, "yellow"), ("Hard", 0.05, "red")]
selected_index = 0
selector_box = Turtle()
selector_box.hideturtle()
selector_box.penup()
selector_box.pensize(3)

buttons = []
paused = False
game_is_on = False
pause_writer = Turtle()
pause_writer.hideturtle()
pause_writer.color("orange")
pause_writer.penup()

def draw_level_buttons():
    x_positions = [-150, 0, 150]
    for i, (label, _, color) in enumerate(levels):
        x = x_positions[i]
        
        # Button shape
        button = Turtle()
        button.penup()
        button.shape("square")
        button.fillcolor(color)
        button.shapesize(stretch_wid=2, stretch_len=6)
        button.goto(x, 0)
        button.showturtle()
        buttons.append((button, x))

        # Text Turtle exactly centered inside box
        text = Turtle()
        text.hideturtle()
        text.penup()
        text.goto(x, -10)
        text.color("white")
        text.write(label, align="center", font=("Arial", 18, "bold"))

    update_selector()


def update_selector():
    selector_box.clear()
    label, _, color = levels[selected_index]
    _, x = buttons[selected_index]

    selector_box.color(color)
    selector_box.goto(x - 70, 30)
    selector_box.pendown()
    for _ in range(2):
        selector_box.forward(140)
        selector_box.right(90)
        selector_box.forward(60)
        selector_box.right(90)
    selector_box.penup()

def move_selector_right():
    global selected_index
    selected_index = (selected_index + 1) % len(levels)
    update_selector()

def move_selector_left():
    global selected_index
    selected_index = (selected_index - 1) % len(levels)
    update_selector()

def draw_border():
    border = Turtle()
    border.hideturtle()
    border.speed("fastest")
    border.pensize(3)
    border.penup()
    border.goto(-290, -290)
    border.pendown()
    border.color("white")
    for _ in range(4):
        border.forward(580)
        border.left(90)

def toggle_pause():
    global paused
    paused = not paused
    if paused:
        pause_writer.goto(0, 0)
        pause_writer.write("Game Paused", align="center", font=("Courier", 24, "bold"))
    else:
        pause_writer.clear()

def start_game():
    global delay, game_is_on, snake, food, scoreboard
    for btn, _ in buttons:
        btn.hideturtle()
    selector_box.clear()
    screen.clear()
    screen.bgcolor("black")
    draw_border()

    label, selected_delay, _ = levels[selected_index]
    delay = selected_delay
    game_is_on = True

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard(level_name=label)

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(toggle_pause, "space")
    screen.onkey(start_game, "r")

    run_game()

def run_game():
    global game_is_on
    while game_is_on:
        screen.update()
        if not paused:
            time.sleep(delay)
            snake.move()

            if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend()
                scoreboard.increase_score()

            if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
                game_is_on = False
                scoreboard.game_over()

            for seg in snake.segments[1:]:
                if snake.head.distance(seg) < 10:
                    game_is_on = False
                    scoreboard.game_over()
    screen.exitonclick()

# Keyboard controls for selector
screen.listen()
screen.onkey(move_selector_right, "Right")
screen.onkey(move_selector_left, "Left")
screen.onkey(start_game, "Return")

draw_level_buttons()
screen.mainloop()
