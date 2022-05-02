#import colorgram
# colors = colorgram.extract("Hirstspotpainting.jpeg", 10)
# color_list = []
# for color in colors:
#     rgb = (color.rgb.r, color.rgb.g, color.rgb.b) 
#     color_list.append(rgb)
# print(color_list)
import turtle
import random
t = turtle.Turtle()
t.speed(0)
t.ht()
screen = turtle.Screen()
screen.screensize(750, 750)
screen.colormode(255)
color_list = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81)]
def dot_maker(num_dots_per_side, window_size): 
    delta = 750/(num_dots_per_side+1)
    x, y = -750/2, -750/2
    while y <= 375 - delta: 
        t.up()
        y += delta
        t.goto(x, y)
        for _ in range(num_dots_per_side): 
            x += delta
            t.goto(x, y)
            t.down()
            t.dot(20, random.choice(color_list))
            t.up()
        x = -750/2
            
dot_maker(10, 750)

    
screen.exitonclick()