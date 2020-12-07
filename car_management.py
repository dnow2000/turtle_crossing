from turtle import Turtle
import random

COLORS = ["blue", "red", "purple", "magenta", "green", "yellow", "orange"]
INCREMENT_BY = 10
STARTING_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=2, stretch_len=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-200, 250)
            new_car.setpos(280, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def next_level(self):
        self.car_speed += INCREMENT_BY
