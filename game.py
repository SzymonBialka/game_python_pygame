import pygame
import os
from sklep import main2
from my_class.class_main1 import *
from my_class.class_baz import Ikon

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1366,768))
path = os.path.join('.', 'image')
file_names = sorted(os.listdir(path))
Background = pygame.image.load(os.path.join(path, 'niebo.jpg')).convert()

file_names.remove('niebo.jpg')
file_names.remove('1backgroud.jpg')
IMages = {}
IMages_F=[]
LIGHTBLUE = pygame.color.THECOLORS['lightblue']
for file_name in file_names:
    image_name = file_name[:5].upper()
    IMages[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(Background)
    if image_name=="METEO":
        IMages_F.append( pygame.image.load(os.path.join(path, file_name)).convert_alpha(Background))
METEOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(METEOR_EVENT, 500)
start = Ikon(IMages['START'], 1366 // 2, 768 // 2)
player = Player(IMages['PLAYE'], 1366 // 2, 768 // 2, IMages['FIRE1'])
curret_lv = Level(player, IMages_F, LIGHTBLUE)
sklep = Ikon(IMages['SKLEP'], 1258, 704)
end = Ikon(IMages['ENDEN'], 1366 // 2, 768 // 2)
win = Ikon(IMages['WINWI'], 1366 // 2, 768 // 2)
tab_sklep_left, tab_sklep_top = [1156, 1244], [604, 679]
def main1():
    window_open = [True]
    while window_open:
        screen.blit(Background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open[0] = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open[0] = False
            elif event.type == METEOR_EVENT:
                curret_lv.handle_event_meteor()
            curret_lv.handle_event_bullet(event)
        if curret_lv.player.lives<=0:
            end.draw(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    exit(0)
        if curret_lv.number<=0:
            win.draw(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    exit(0)

        curret_lv.update()
        keys = pygame.key.get_pressed()

        player.handle_event(keys)
        curret_lv.destroy()
        curret_lv.kill_player()
        player.update()

        sklep.draw(screen)
        player.draw(screen)
        curret_lv.draw(screen,IMages['LAYER'])

        curret_lv.update_score(LIGHTBLUE)
        curret_lv.text_points.draw(screen)


        if(tab_sklep_left[0] <= player.rect.left <= tab_sklep_left[-1] and
    tab_sklep_top[0] <= player.rect.top <= tab_sklep_top[-1]):
            start.draw(screen)
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                main2(player)



        pygame.display.flip()
        clock.tick(100)
