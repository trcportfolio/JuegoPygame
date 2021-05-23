import pygame


import characters

class Spritesheet:
    def __init__(self, filename, columns, rows, colorkey, scaling):
        self.sheet = pygame.image.load(f"Assets/Images/Spritesheet/{filename}").convert()
        self.sheet.set_colorkey(colorkey)
        self.sheet = pygame.transform.scale(self.sheet, (scaling))
        self.columns = columns
        self.rows = rows
        self.totalCellCount = columns*rows
        self.rect = self.sheet.get_rect()
        self.cellWidth = int(self.rect.width/columns)
        self.cellHeight = int(self.rect.height/rows)
    

        self.cellList = []
       
        for index in range(self.totalCellCount):
            self.cellList.append(pygame.Rect(index%columns*self.cellWidth, int(index/columns)*self.cellHeight,
                                  self.cellWidth, self.cellHeight))

    def drawsprite(self, win, rect, spriteIndex):
       win.blit(self.sheet, rect, self.cellList[spriteIndex])