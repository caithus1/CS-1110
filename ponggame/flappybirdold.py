# Christopher Geier (cpg3rb)
# Pong (Starter Code)

import pygame
import gamebox
import random
import time
camera = gamebox.Camera(800,600)

p_width = 10
p_height = 80
ball_velocity = 15
player_speed = 14
p1_score = 0
p2_score = 0
game_on = False

ticker = 0

walls = [
    gamebox.from_color(400, 600, "green", 1000, 20),
    gamebox.from_color(400, 0, "green", 1000, 20),
]

top_barrier = gamebox.from_color(700,-100,"red",20,600)
bot_barrier = gamebox.from_color(700,700,"red",20,600)

p1 = gamebox.from_color(20, 400, "red", 15, 15)
count = 0
#ball.xspeed = ball_velocity
#ball.yspeed = ball_velocity
top_barrier.xspeed = -7
bot_barrier.xspeed = -7

def tick(keys):
    global game_on
    global p1_score
    global p2_score
    if game_on:
        top_barrier.move_speed()
        bot_barrier.move_speed()

    # ------- INPUT ---------
    if pygame.K_SPACE in keys:
        game_on = True
    '''

    '''
    #top_barrier.move(8,0)
    # Draw all the walls
    for wall in walls:
        camera.draw(wall)

    camera.draw(top_barrier)
    camera.draw(bot_barrier)
    #camera.draw(ball)

    # ---- CHECKING FOR WIN ----
    if p1_score >= 10:
        camera.draw(gamebox.from_text(400, 100, "Red Wins!", "Arial", 40, "Red", True))
        gamebox.pause()
    if p2_score >= 10:
        camera.draw(gamebox.from_text(400, 100, "Yellow Wins!", "Arial", 40, "Yellow", True))
        gamebox.pause()
    camera.display()


ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)