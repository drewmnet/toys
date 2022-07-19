import pygame
import numpy


pygame.init()
display = pygame.display.set_mode((500, 500))

head_rect = pygame.Rect((10, 10, 300, 16))
window_head = pygame.Surface(head_rect[2:]).convert()
window_head.fill((0xff, 0xff, 0xff))
window_head.set_alpha(32)

is_clicked = False
is_on_head = False
calc = ()

running = True
while running:
    pygame.event.get()
    if pygame.mouse.get_pressed()[0] and not is_clicked:
        is_clicked = True
        mouse_pos = pygame.mouse.get_pos()
        if head_rect.collidepoint(mouse_pos):
            calc = numpy.subtract(mouse_pos, head_rect[:2])
            is_on_head = True
    elif not pygame.mouse.get_pressed()[0] and is_clicked:
        is_clicked = False
        is_on_head = False
    
    if is_on_head:
        x, y = tuple(numpy.subtract(pygame.mouse.get_pos(), calc))
        head_rect.x = x
        head_rect.y = y
    
    display.blit(window_head, head_rect[:2])

    pygame.display.flip()
    display.fill((0,0,0))

