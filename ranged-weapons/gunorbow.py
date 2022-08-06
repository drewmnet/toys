#!/usr/bin/env python3

import pygame

class Gun:
    def __init__(self):
        self.is_aiming = False
        self.tick = 0
        
    def get_input(self):
        if not self.is_aiming and 

if __name__ == "__main__":
    pygame.init()
    
    clock = pygame.time.Clock()
    
    t = pygame.time.get_ticks()
    
    while True:
        clock.tick(60)
        print((pygame.time.get_ticks() - t) // 1000)
        

