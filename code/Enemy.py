#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_cooldown = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self,):
        self.shot_cooldown -= 1
        if self.shot_cooldown <= 0:
            self.shot_cooldown = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

