import pygame
from settings import Settings
from spritesheets import Spritesheet
import characters

class Enemy:
    
    def __init__(self, win, data):
        self.settings = Settings()
        self.screen = win
        self.data = data
        self.right = False
        self.left = True
        self.fpsCounter = 0
        self.x = self.settings.enemypos[0][0]
        self.y = self.settings.enemypos[0][1]
        self.win = win
        self.battle = False

        self.draw = Spritesheet(data[0],data[1], data[2], data[3], data[6])
        self.enemyRect = pygame.Rect(self.settings.enemypos[0][0], self.settings.enemypos[0][1],
                                    self.settings.charHeight, self.settings.charWidth)
        
         
    def animation(self):
        self.hitbox = pygame.Rect(self.x + 20, self.y + 110, 100, 100)
        pygame.draw.rect(self.win, (0,255,0), self.hitbox, 2 )

        
        if self.fpsCounter < 48:
            self.draw.drawsprite(self.screen, self.enemyRect, self.fpsCounter//3)
            self.fpsCounter += 1
        
        if self.fpsCounter >= 48:
            self.fpsCounter = 0   

    def battleAnimation(self):

        pass
        
    def collision(self, mainchar):
        collision = self.hitbox.colliderect(mainchar.hitbox)
        
        if collision: 
            
            self.battle = True 
        
       


