#!/usr/bin/python
# -*- coding: utf-8 -*-
from turtle import position

import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, Player_KEY_RIGHT, Player_KEY_DOWN, Player_KEY_UP, \
    Player_KEY_LEFT, ENTITY_SHOT_DELAY, PLAYER_KEY_SHOOT
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    # new
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.shot_cooldown = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):

        pressed_key = pygame.key.get_pressed()

        if pressed_key[Player_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[Player_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[Player_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[Player_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        self.shot_cooldown  -= 1
        if self.shot_cooldown == 0:
            self.shot_cooldown = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
