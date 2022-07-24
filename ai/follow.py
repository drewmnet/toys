#!/usr/bin/env python3

import math
import pygame
import numpy

class Mob(pygame.Rect):
    def __init__(self, colour, rect):
        pygame.Rect.__init__(self, rect)
        self.image = pygame.Surface(rect[2:]).convert()
        self.image.fill(colour)
        
        self.x_axis = 0
        self.y_axis = 0
        
        self.following = None
        self.controller = None
        self.is_moving = False
        
    def update(self):
        self.controller(self)
        self.x += self.x_axis
        self.y += self.y_axis
        
    def render(self, surface):
        surface.blit(self.image, self[:2])
        
def player_control(mob):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mob.y_axis = -1
            elif event.key == pygame.K_DOWN:
                mob.y_axis = 1
            if event.key == pygame.K_LEFT:
                mob.x_axis = -1
            elif event.key == pygame.K_RIGHT:
                mob.x_axis = 1
                
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
                
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                mob.y_axis = 0
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                mob.x_axis = 0
                
        mob.is_moving = bool(mob.x_axis + mob.y_axis)
        
def follower_control(mob):
    if mob.following != None:
        if mob.following.is_moving:
            pythag = numpy.subtract(mob.center, mob.following.center) ** 2
            distance = int(math.sqrt(sum(pythag)))
            
            if distance >= 10:
                mob.x += mob.following.x_axis
                mob.y += mob.following.y_axis
        
if __name__ == "__main__":
    pygame.init()
    
    display = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()
    
    player = Mob((255,0,0), (10,10,32,32))
    player.controller = player_control
    
    follower = Mob((0,255,0), (52, 10, 32, 32))
    follower.controller = follower_control
    follower.following = player
    
    while True:
        clock.tick(60)
        
        player.update()
        follower.update()
        player.render(display)
        follower.render(display)
        pygame.display.flip()
        display.fill((0,0,0))
