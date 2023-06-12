import pygame
import os
from game import main1
from my_class.class_main import *

pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("Gwiezdna Strzelanka")

clock = pygame.time.Clock()

path = os.path.join('.', 'image')
file_names = sorted(os.listdir(path))
Backgroud = pygame.image.load(os.path.join(path, '1backgroud.jpg')).convert()
button=pygame.image.load(os.path.join(path,'start.jpg')).convert_alpha(Backgroud)

# pygame.mixer.music.load(os.path.join('.', 'mp', 'muzyka.mp3'))
# pygame.mixer.music.play(-1)

start=Start(button,1366 // 2, 768 // 2,main1)
window_open = True
while window_open:
    screen.blit(Backgroud, (0, 0))

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            window_open=False

    start.handle_event(event)

    start.draw(screen)




    pygame.display.flip()
    clock.tick(30)
pygame.quit()
