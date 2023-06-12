import pygame
import os
from my_class.class_main2 import *
from my_class.class_baz import Ikon

pygame.init()

screen = pygame.display.set_mode((1366,768))


clock = pygame.time.Clock()

path = os.path.join('.', 'image')
file_names = sorted(os.listdir(path))
Backgroud = pygame.image.load(os.path.join(path, '1sklep.jpg')).convert()
button=pygame.image.load(os.path.join(path,'plus.jpg')).convert_alpha(Backgroud)
IMages = {}
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
for file_name in file_names:
    image_name = file_name[:5].upper()
    IMages[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(Backgroud)
IMages_N=[IMages['ZEROO'],IMages['JEDEN'],IMages['DWAAA'],IMages['TRZYY'],IMages['CZTER'],IMages['PIECC'],IMages['SZESC'],IMages['SIEDE'],IMages['OSIEM'],IMages['DZIEW']]
File_fire = []
for i in file_names:
    if i[:4].upper() == "FIRE":
        File_fire.append(i)

def main2(player):
    fire=Ikon(player.b_img,456,160)
    window_open = [True]
    plus = Plus(button, 250, 160,File_fire)
    plus1=Plus1(button,250,300)
    text=Text(player.coins, LIGHTBLUE,1210,700, font_size=76)
    end=End(button,1300,45)
    while window_open[0]:
        screen.blit(Backgroud, (-100,-100))
        fire.draw(screen)
        plus.draw(screen)
        plus1.draw(screen)
        end.draw(screen)
        text.update(player.coins)
        text.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open[0] = False
            end.handle_event(event,window_open)
            plus.handle_event(event,screen,player,path,fire)
            plus1.handle_event(event,player)


        pygame.display.flip()
        clock.tick(100)
