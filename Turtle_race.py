import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['pink', 'light blue','light green','thistle','steel blue','pale violet red','light grey', 'misty rose','rosy brown','medium aquamarine']

def get_number():
     racers = 0
     while True:
         racers = int(input('Enter Number of racers: '))

         if 2 <= racers <= 10:
             return racers
         else:
            print('The number is not Valid')


def race(colours):
    turtles = create_racers(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
 
def create_racers(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+ 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles
        
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Race!!')


racers = get_number()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The Winner is", winner)