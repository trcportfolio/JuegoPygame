import pygame
from settings import Settings
from spritesheets import Spritesheet



class Background:

    def __init__(self, win):
        self.settings = Settings()
        self.screen = win
    
    def loadBackground(self, filename):
        
        self.background = pygame.image.load(f"Assets/Images/Backgrounds/{filename}")
        self.background = self.background.convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.settings.winWidth, self.settings.winHeight))
        
    
    def blitbg(self):
        self.screen.blit(self.background, (0,0))

    def setBgList(self, tiles):
        if type(tiles) is str:
            self.tiles = [[loadBackground(tiles)]]
        elif type(tiles[0]) is str:
            self.tiles = [[self.loadBackground(i) for i in tiles]]
        else:
            self.tiles = [[self.loadBackground(i) for i in row] for row in tiles]
       
        
        self.tilePosX = 0 
        self.tilePosY = 0
        self.screen.blit(self.tiles[0][0], [0, 0])
        self.tileWidth = self.settings.winWidth
        self.tileHeight = self.settings.winHeight

    def scroll(self, x, y):
        self.tilePosX -= x
        self.tilePosY -= y
        col = (self.tilePosX % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        xOff = (0 - self.tilePosX % self.tileWidth)
        row = (self.tilePosY % (self.tileHeight * len(self.tiles))) // self.tileHeight
        yOff = (0 - self.tilePosY % self.tileHeight)

        col2 = ((self.tilePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        row2 = ((self.tilePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))) // self.tileHeight
        self.screen.blit(self.tiles[row][col], [xOff, yOff])
        self.screen.blit(self.tiles[row][col2], [xOff + self.tileWidth, yOff])
        self.screen.blit(self.tiles[row2][col], [xOff, yOff + self.tileHeight])
        self.screen.blit(self.tiles[row2][col2], [xOff + self.tileWidth, yOff + self.tileHeight])

    def screen_animation(self,screen, data, counter):
        self.sprite = Spritesheet(data[0], data[1], data[2], data[3], data[4])
        self.fpsCounter = 0
        if counter == 0:

            if self.fpsCounter < 12:
                self.sprite.drawsprite(screen, rect, self.fpsCounter//12)
                self.fpsCounter += 1

    def screen_animation2(self, screen):
        self.fpsCounter = 0
        while self.fpsCounter < 60: 
            screen.fill((255,255,255))
            self.fpsCounter += 1
            pygame.display.update()
            screen.fill((0,0,0))
            self.fpsCounter += 1
            



        