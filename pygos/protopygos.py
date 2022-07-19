#!/usr/bin/env python3

import pygame

class Deskbar:
    def __init__(self, rect, rgba, display):
        self.rect = rect
        self.buffer = pygame.Surface(self.rect[2:]).convert()
        self.buffer.blit(display.subsurface(self.rect), (0, 0))
        self.image = pygame.Surface(self.rect[2:]).convert()
        self.image.fill(rgba[:3])
        self.image.set_alpha(rgba[-1])
        
        self.is_sliding = False
        
        self.name = "Deskbar"
        
    def draw(self, display):
        display.blit(self.image, (self.rect[0], self.y))
    
    def erase(self, display):
        display.blit(self.buffer, self.rect[:2])
        
    def start(self, funcs):
        if not self.is_sliding:
            print("starting")
            funcs[self.name] = self.update
            self.is_sliding = True
            self.y = -self.rect[3]
            
    def update(self, display):
        if self.is_sliding:
            print(self.y)
            if self.y < self.rect[1]:
                self.erase(display)
                self.y += 2
                self.draw(display)
                pygame.display.flip()
            elif self.y == self.rect[1]:
                self.is_sliding = False
                print(self.is_sliding)

if __name__ == "__main__":
    pygame.init()
    display = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    wallpaper = pygame.image.load("pygos-wallpaper.jpg")
    display.blit(wallpaper, (0, 0))
    pygame.display.flip()
    
    msg_window = Deskbar((8, 0, 784, 32), (0, 0, 0, 128), display)
    funcs = {}
    
    is_running = True
    while is_running:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                if event.key == pygame.K_RETURN:
                    msg_window.start(funcs)
                        
        for func in funcs.values():
            func(display)
