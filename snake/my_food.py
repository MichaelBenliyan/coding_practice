from random import randrange, choice
import turtle


class Food(turtle.Turtle): 
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("green")
        self.speed(0)
       
    def place(self, snake_chain):
        possible_locations = []
        snake_cords = set()
        for bit in snake_chain: 
            snake_cords.add((int(bit.xcor()), int(bit.ycor())))
        for x in range(-380, 400, 20): 
            for y in range(-360, 400, 20): 
                if (x,y) not in snake_cords: 
                    possible_locations.append((x, y))
        self.goto(choice(possible_locations))