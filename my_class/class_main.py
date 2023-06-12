import pygame
import os

class Start(pygame.sprite.Sprite):
    def __init__(self, image, px, py,callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = px, py
        self.callback=callback

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
