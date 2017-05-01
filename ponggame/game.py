# Christopher Geier (cpg3rb)

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
#screen = pygame.display.set_mode((1000, 1000))
#camera = pygame.display.set_mode()
#print(camera.__setattr__())
game_on = False
player1_score = 0
player2_score = 0

# Walls:
walls = [
    gamebox.from_color(800/2, 0, "green", 1000, 50),
    gamebox.from_color(800/2, 600, "green", 1000, 50),
    gamebox.from_color(800, 600/2, "green", 50, 1000),
    gamebox.from_color(0, 600/2, "green", 50, 1000)
]

statics = [
    
]

# Sprites
player1 = gamebox.from_color(350, 300, "red", 25, 25)
player2 = gamebox.from_color(550, 300, "yellow", 25, 25)
cube = gamebox.from_color(450,300,'blue',5,5)
# Speed initialization

def tick(keys):

    # Global Vars
    global game_on
    global rectangle_draging
    global player1_score
    global player2_score
    
    # game_on
    #screen.fill((255, 255, 255))
    if pygame.K_SPACE in keys:
        game_on = True

    
    # Game Logic
    '''
    if pygame.K_UP in keys:
        # Move up
        player.move(0,-16)
    if pygame.K_DOWN in keys:
        # Move Down
        player.move(0,16)
    '''

    if player1.touches(walls[0]):
        ...
    else:
        if pygame.K_UP in keys:
            # Move up
            player1.move(0, -16)
    if player1.touches(walls[1]):
        ...
    else:
        if pygame.K_DOWN in keys:
            player1.move(0, 16)
    if player1.touches(walls[2]):
        ...
    else:
        if pygame.K_RIGHT in keys:
            player1.move(16, 0)
    if player1.touches(walls[3]):
        ...
    else:
        if pygame.K_LEFT in keys:
            player1.move(-16, 0)

    if player2.touches(walls[0]):
        ...
    else:
        if pygame.K_w in keys:
            # Move up
            player2.move(0, -16)
    if player2.touches(walls[1]):
        ...
    else:
        if pygame.K_s in keys:
            player2.move(0, 16)
    if player2.touches(walls[2]):
        ...
    else:
        if pygame.K_d in keys:
            player2.move(16, 0)
    if player2.touches(walls[3]):
        ...
    else:
        if pygame.K_a in keys:
            player2.move(-16, 0)

    if player1.touches(cube):
        player1_score += 1
        cube.x = random.randint(50,500)
        cube.y = random.randint(50,600)
    if player2.touches(cube):
        player2_score += 1
        cube.x = random.randint(50,500)
        cube.y = random.randint(50,600)

    # Render objects
    if game_on:
        camera.clear('black')
        for wall in walls:
            camera.draw(wall)
        for static in statics:
            camera.draw(static)
        camera.draw(player1)
        camera.draw(player2)
        camera.draw(cube)
        camera.draw(gamebox.from_text(300, 50, str(player1_score), "Arial", 50, "White", True))
        camera.draw(gamebox.from_text(500, 50, str(player2_score), "Arial", 50, "White", True))
    # End screen
    if player1_score >= 10:
        camera.draw(gamebox.from_text(400, 100, "Red Wins!", "Arial", 40, "Red", True))
        gamebox.pause()
    if player2_score >= 10:
        camera.draw(gamebox.from_text(400, 100, "Yellow Wins!", "Arial", 40, "Yellow", True))
        gamebox.pause()
    # Start screen
    if not game_on:
        camera.draw(gamebox.from_text(400, 200, 'The Lounge', 'Arial', 70, "Yellow", True))
        camera.draw(gamebox.from_text(400, 100, 'Created by Ryan Kelly (rpk2kn) and Christopher Geier (cpg3rb)'
                                                '', 'Arial', 20, "Green", True))
        camera.draw(gamebox.from_text(400, 300, 'The Lounge is a mess! Sungwoo left all his trash behind', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 335, 'leaving you two alone to clean up.', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 370, 'Move over pieces of trash to pick them up until all is gone.', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 405, 'At the end, the player who has cleaned the most wins.', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 440, 'Player 1 moves with the arrow keys.', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 475, 'Player 2 moves with WASD.', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 550, 'Press SPACE to begin', 'Arial', 30, "Blue", True))

    camera.display()

gamebox.timer_loop(30, tick)