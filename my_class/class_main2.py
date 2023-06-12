import pygame
import os
from my_class.class_baz import Click,Ikon

class Plus(Click):
    def __init__(self, image, px, py,name_fire):
        super().__init__(image, px, py)
        self.name_fire=name_fire
        self.number = 0

    @property
    def fire_take(self):
        return self.name_fire[self.number]

    def handle_event(self, event,Backgroud,player,path,fire):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.number+=1
                if self.number!=7 and player.coins>5:
                    player.change_fire(pygame.image.load(os.path.join(path,self.fire_take)).convert_alpha(Backgroud))
                    fire.image=pygame.image.load(os.path.join(path, self.fire_take)).convert_alpha(Backgroud)
                    player.coins-=5
                else:
                    self.number=6

class Plus1(Click):
    def __init__(self, image, px, py):
        super().__init__(image, px, py)

    def handle_event(self, event,player):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and player.coins>1:
                player.coins-=1
                player.change_speed()

class End(Click):
    def __init__(self,image,px,py):
        super().__init__(image,px,py)

    def handle_event(self, event, window_open):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                window_open[0]=False

class Text:
    def __init__(self, text, text_colour, px, py, font_type=None, font_size=74):
        self.text = str(text)
        font = pygame.font.SysFont(font_type, font_size)
        self.image = font.render(self.text, True, text_colour)
        self.rect = self.image.get_rect()
        self.rect.center = px, py

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self,points):
        self.text=str(points)