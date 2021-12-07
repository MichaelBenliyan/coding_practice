import turtle


class Snake(): 
    def __init__(self):
        self.snake_chain = []
        self.head = turtle.Turtle(shape="square", visible=False)
        self.head.speed(0)
        self.head.up() 
        self.snake_chain.append(self.head)
        self.add(0, 0)
        
    def add(self, x, y):
        new_piece = turtle.Turtle(shape="square")
        new_piece.speed(0)
        new_piece.up()
        new_piece.color("white")
        new_piece.goto(x, y)
        self.snake_chain.insert(1, new_piece)
    
    def move(self):    
        self.head.forward(20)
        new_xcor = self.head.xcor()
        new_ycor = self.head.ycor()
        self.snake_chain[-1].goto(x=new_xcor, y=new_ycor)
        self.snake_chain.insert(1, self.snake_chain.pop())
    
    def hit_wall(self): 
        return self.head.xcor() < -395 or self.head.xcor() > 395 or self.head.ycor() > 395 or self.head.ycor() < -395

    def hit_itself(self): 
        for limb in self.snake_chain[2:-1]:
            if self.head.distance(limb) < 5:
                return True 
        return False
    
    def got_food(self, food): 
        return self.head.distance(food) < 5
            
    def up(self):
        if self.head.heading() != 270.0:
            self.head.seth(90)
        
    def right(self):
        if self.head.heading() != 180.0:
            self.head.seth(0)

    def left(self):
        if self.head.heading() != 0.0:
            self.head.seth(180)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.seth(270)