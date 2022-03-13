import pygame as pg
from vector import Vector
from pygame.sprite import Sprite, Group
from copy import copy
from random import randint
from timer import CommandTimer
# from alien import Alien
# from stats import Stats

class Barriers:
    def __init__(self, game):
        self.game = game
        # self.alien_fleet = game.alien_fleet
        for n in range(5):
            self.create_barrier()

    def update(self):
        for barrier in self.barriers:
            barrier.update()

    def draw(self):
        for barrier in self.barriers:
            barrier.draw()
    def create_barrier(self):
        for row in range(4):
            for col in range(4):
                be = BarrierElement(game=self.game, img_list=Barrier.img_list,
                    ul=(2 + col, 2 + row * 12), wh=(16, 16))
                self.barrier_elements.add(be)


class Barrier(Sprite):
    img_list = [pg.image.load(f'images/block{n}.png') for n in range(1)]
    def __init__(self, game, ul, wh):
        self.game = game
        self.barrier_elements = Group()
        self.ul = ul
        self.wh = wh
        self.create_barrier()

    def update(self):
        collisions = pg.sprite.groupcollide(self.barrier_elements,
                                            self.game.lasers.lasers, False, True)
        for be in collisions:
            be.hit()

    def draw(self):
        for be in self.barrier_elements:
            be.draw()
    def create_barrier(self):
        for row in range(self.wh[0]):
            for col in range(self.wh[1]):
                be = BarrierElement(game=self.game, img_list=Barrier.img_list,
                    ul=(self.ul[0] + col, self.ul[1] + row * 12), wh=(16, 16))
                self.barrier_elements.add(be)



class BarrierElement(Sprite):
    def __init__(self, game, img_list, ul, wh):
        self.ul = ul
        self.wh = wh
        self.rect = pg.Rect(ul[0], ul[1], wh[0], wh[1])
        self.timer = CommandTimer(image_list=img_list, is_loop=False)

    def update(self): pass

    def hit(self):
        self.timer.next_frame()
        if self.timer.is_expired():
            self.kill()

    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.x, rect.y = self.rect.x, self.rect.y
        self.screen.blit(image, rect)
