import pygame
import os
import random
from my_class.class_baz import Objective

class Player(pygame.sprite.Sprite):
    def __init__(self, image, px, py,b_img):
        super().__init__()
        self.orginal_image=image
        self.image = self.orginal_image
        self.rect = self.image.get_rect()
        self.rect.center = px, py
        self.angel=0
        self.movement_speed = 2
        self.b_img=b_img
        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()
        self.lives=3
        self.coins=0

    def change_speed(self):
        self.movement_speed+=0.5

    def change_fire(self,img):
        self.b_img=img
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self,keys):
        if keys[pygame.K_LEFT]:
            self.rect.move_ip([-self.movement_speed, 0])
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip([self.movement_speed, 0])
        if keys[pygame.K_DOWN]:
            self.rect.move_ip([0,self.movement_speed])
        if keys[pygame.K_UP]:
            self.rect.move_ip([0,-self.movement_speed])

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height






class Bullet(Objective):
    def __init__(self, image, px, py):
        super().__init__(image,px,py,-2)



class Level:
    def __init__(self, player,m_img,LIGHTBLUE):
        self.player = player
        self.bullets = pygame.sprite.Group()
        self.meteor=pygame.sprite.Group()
        self.m_image=m_img
        self.number=200
        self.text_points = Text(self.player.coins, LIGHTBLUE, 1266, 50, font_size=76)

    def update_score(self,LIGHTBLUE):
        self.text_points = Text(self.player.coins, LIGHTBLUE, 1266, 50, font_size=76)

    def update(self):
        self.bullets.update()
        self.meteor.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        for meteorr in self.meteor.copy():
            if meteorr.rect.bottom >= pygame.display.get_surface().get_height():
                self.meteor.remove(meteorr)

    def handle_event_meteor(self):
        choice_img=random.randint(0,19)
        choice_x=random.randint(0,pygame.display.get_surface().get_width())
        meteor=Meteor(self.m_image[choice_img],choice_x,0)
        self.meteor.add(meteor)
        self.number-=1

    def handle_event_bullet(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(self.bullets) < 12:
                bullet = Bullet(self.player.b_img, self.player.rect.centerx-20, self.player.rect.top)
                bullet1 = Bullet(self.player.b_img, self.player.rect.centerx+20, self.player.rect.top)
                self.bullets.add(bullet)
                self.bullets.add(bullet1)

    def draw(self, surface,img):
        self.bullets.draw(surface)
        self.meteor.draw(surface)
        for i in range(self.player.lives):
            surface.blit(img, [20 + 40 * i, 15])

    def kill_player(self):
        if pygame.sprite.spritecollide(self.player,self.meteor, False):
            self.player.lives-=1
            self.player.rect.center=1366 // 2, 768 // 2


    def destroy(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.meteor, True, True)
        for bullet, collided_meteors in collisions.items():
            for meteor in collided_meteors:
                self.meteor.remove(meteor)
                self.player.coins+=1



class Meteor(Objective):
    def __init__(self, image, px, py):
        super().__init__(image, px, py,1)


class Text:
    def __init__(self, text, text_colour, px, py, font_type=None, font_size=74):
        self.text = str(text)
        font = pygame.font.SysFont(font_type, font_size)
        self.image = font.render(self.text, True, text_colour)
        self.rect = self.image.get_rect()
        self.rect.center = px, py

    def draw(self, surface):
        surface.blit(self.image, self.rect)
