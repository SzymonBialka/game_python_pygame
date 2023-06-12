import pygame
import os

class Click(pygame.sprite.Sprite):
    def __init__(self, image, px, py):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = px, py


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event,callback):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                callback()


class Ikon(pygame.sprite.Sprite):
    def __init__(self, image, px, py):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = px, py

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Objective(pygame.sprite.Sprite):
    def __init__(self, image, px, py,speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = px, py
        self.speed = speed

    def update(self):
        self.rect.move_ip(0, self.speed)

    def draw(self,surface):
        surface.blit(self.image,self.rect)

