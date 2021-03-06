#!/usr/bin/env python3

'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import pygame
from arena import Character, Arena
from pong import PongArena, Ball, Paddle, AutoPaddle

arena = PongArena(600, 400)
Ball(arena, 300, 200)
paddle = Paddle(arena, 100, 200);
AutoPaddle(arena, 200, 50, 250);
AutoPaddle(arena, 400, 50, 100);
AutoPaddle(arena, 500, 200, 100);

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(arena.size())
background = (255, 255, 255)
images = {Ball: pygame.image.load('ball.bmp')}
colors = {Paddle: (0, 0, 255),
          AutoPaddle: (0, 0, 255)}
# if img size ≠ 20x20: pygame.transform.scale

playing = True
while playing:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            playing = False
        elif e.type == pygame.KEYDOWN:
            if e.key in (pygame.K_w, pygame.K_UP):
                paddle.go_up()
            elif e.key in (pygame.K_s, pygame.K_DOWN):
                paddle.go_down()
            if e.key == pygame.K_ESCAPE:
                playing = False
        elif e.type == pygame.KEYUP:
            if e.key in (pygame.K_w, pygame.K_UP, pygame.K_s, pygame.K_DOWN):
                paddle.stay()

    # Apply game logic
    arena.move_all()
        
    screen.fill(background)
    for c in arena.characters():
        if type(c) in images:
            img = images[type(c)]
            screen.blit(img, c.rect())
        else:
            col = colors.get(type(c), (127, 127, 127))
            pygame.draw.rect(screen, col, c.rect())

    # print points        
    font = pygame.font.SysFont('arial', 24)
    surface = font.render(str(arena.points()[0]), True, (0, 255, 0))
    screen.blit(surface, (10, 10))
    surface = font.render(str(arena.points()[1]), True, (0, 255, 0))
    screen.blit(surface, (screen.get_width() - surface.get_width() - 10, 10))

    pygame.display.flip()
    clock.tick(30)

