# Christopher Geier (cpg3rb)
# Pong (Starter Code)

import pygame
import gamebox
import random
import time
import urllib.request
from pygame import Color,Surface

camera = gamebox.Camera(800, 600)
screen = pygame.display.set_mode((800, 600))
ball_velocity = 5
game_on = False

ticker = 0
translation = 0
clear = Color(0,0,0,0)

walls = [
    gamebox.from_color(400, 600, "green", 1000, 10),
    gamebox.from_color(400, 0, clear, 1000, 0),
]

top_barrier = gamebox.from_color(800, 59, "red", 20, 600)
bot_barrier = gamebox.from_color(800, 759, "red", 20, 600)
bird = gamebox.from_color(400, 300, "green", 20, 20)
bird.yspeed = ball_velocity
top_barrier.xspeed = -5
bot_barrier.xspeed = -5
img = urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/1/13/Long_sky_background.jpg","bg.jpg")
bg = pygame.image.load('bg.jpg')
def tick(keys):

    global game_on
    global ticker
    global translation

    translation += (1/30)
    if translation*15 > 2000:
        translation= 0
    screen.blit(bg, (-translation*15, 0))
    if game_on:
        bird.move_speed()
        top_barrier.move_speed()
        bot_barrier.move_speed()

    if top_barrier.x == 0:
        seperation = random.randint(60,100)
        top_displacement = random.randint(-200, 200)
        top_on_screen = 300 + top_displacement
        bot = 600 - top_on_screen - seperation
        bot_displacement = 300 + 600 - bot
        top_barrier.move(800, 0)
        bot_barrier.move(800, 0)
        top_barrier.center = [800, bot_displacement]
        bot_barrier.center = [800, top_displacement]

    if pygame.K_UP in keys:
        game_on = True

    if pygame.K_SPACE in keys:
        bird.move(0, -16)

    if game_on:
        camera.draw(gamebox.from_text(400, 50, str(int(ticker)), "Arial", 50, "Yellow", True))
        for wall in walls:
            camera.draw(wall)
        camera.draw(top_barrier)
        camera.draw(bot_barrier)
        camera.draw(bird)

    if game_on:
        ticker += (1/30)
    if top_barrier.touches(bird) or bot_barrier.touches(bird) or bird.touches(walls[0]) or bird.touches(walls[1]):
        camera.clear("black")
        bird.center = [200, 100]
        camera.draw(gamebox.from_text(400, 100, 'SCORE:', "Arial", 70, "Yellow", True))
        camera.draw(gamebox.from_text(400, 300, str(int(ticker)), "Arial", 100, "Yellow", True))
        gamebox.pause()

    if not game_on:
        camera.draw(gamebox.from_text(400, 200, 'Flappybird.py', 'Arial', 70, "Yellow", True))
        camera.draw(gamebox.from_text(400, 300, 'By Christopher Geier (cpg3rb)', 'Arial', 40, "Yellow", True))
        camera.draw(gamebox.from_text(400,350,'Press Up to Start','Arial',20,"Yellow",True))
    camera.display()

gamebox.timer_loop(30, tick)