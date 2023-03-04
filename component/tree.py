import pygame
import data.config as config
from random import randint

class Tree(pygame.sprite.Sprite):
    def __init__(self, side, y):
        super().__init__()
        self.image = pygame.image.load('image/wood.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (config.tree_weight, config.tree_height))
        self.x = config.tree_start_x
        self.y = y

        if side == 'up':
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect = self.image.get_rect(bottomleft = (self.x, self.y))
        else:
            self.rect = self.image.get_rect(topleft = (self.x, self.y+config.tree_distance))

    def delete(self):
        if self.x <= -config.tree_weight:
            self.kill()

    def update(self):
        self.rect.x -= config.tree_speed
        self.delete()