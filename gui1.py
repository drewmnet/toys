import pygame
import numpy

pygame.init()
display = pygame.display.set_mode((500,500))

window_head = pygame.Rect((10, 10, 300, 16))

is_clicked = False
is_on_head = False
calc_x = calc_y = 0

running = True
while running:
    pygame.event.get()
    if pygame.mouse.get_pressed()[0] and not is_clicked:
        is_clicked = True
        if window_head.collidepoint(pygame.mouse.get_pos()):
            calc = numpy.subtract(pygame.mouse.get_pos(), window_head[:2])
            is_on_head = True
    elif not pygame.mouse.get_pressed()[0] and is_clicked:
        is_clicked = False
        is_on_head = False
    
    if is_on_head:
        x, y = tuple(numpy.subtract(pygame.mouse.get_pos(), calc))
        window_head.x = x
        window_head.y = y
    
    pygame.draw.rect(display, (0,0,0xff), window_head)

    pygame.display.flip()
    display.fill((0,0,0))
