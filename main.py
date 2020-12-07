import time
from score import Score
from turtle import Screen
from player import Player
from car_management import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Score()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if player.ycor() > 300:
        player.reset_pos()
        score.increase_score()
        car_manager.next_level()

    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            score.game_over()
            game_is_on = False

screen.exitonclick()
