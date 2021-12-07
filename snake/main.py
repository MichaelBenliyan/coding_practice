from my_food import Food
from my_snake import Snake
import turtle
import time

def main(): 
    snake = Snake()
    food = Food()
    food.place(snake.snake_chain)

    board = turtle.Screen()
    board.setup(width=800, height=800)
    board.bgcolor("black")
    board.tracer(0)
    board.title("My Snake Game")

    board.listen()
    board.onkeypress(snake.up, "Up")
    board.onkeypress(snake.right, "Right")
    board.onkeypress(snake.left, "Left")
    board.onkeypress(snake.down, "Down")


    while True: 
        board.update()
        time.sleep(0.018)
        snake.move()
        board.update()
        time.sleep(0.018)
        if snake.hit_itself() or snake.hit_wall(): 
            break
        elif snake.got_food(food): 
            snake.add(food.xcor(), food.ycor())
            food.place(snake.snake_chain)
        board.update()
    time.sleep(1)
        
if __name__ == '__main__': 
    main()