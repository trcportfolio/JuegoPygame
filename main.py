import pygame
from spritesheets import Spritesheet
from main_char import mainChar
from settings import Settings
import characters
from backgrounds import Background
from enemy1 import Enemy
from enemy2 import Enemy2
pygame.init()
main = characters.character1
data = characters.enemy1
data2 = characters.enemy2
bg_limits = characters.bg1_limits


class Game: 
    def __init__(self):

        self.settings = Settings()
        self.win = pygame.display.set_mode((self.settings.winWidth, self.settings.winHeight))
        self.clock = pygame.time.Clock()
        
    

    def run(self):
        event = 0
        run = True
        enemy1 = Enemy(self.win, data)
        enemy1_2 = Enemy2(self.win, data2)
        self.win.fill((255, 255, 255))
        battle_state = False
        main_char = mainChar(self.win, main)
        main_char.background.loadBackground("background1.png")
        main_char2 = mainChar(self.win, main)
        battle_start = 0

        
      

        while run:
            self.clock.tick(60)
            
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                event = event.type
                keys = pygame.key.get_pressed()
            
            if not battle_state:
                main_char.background.blitbg()
                main_char.movement(keys, self.win, event, bg_limits, battle_state)    
                enemy1.animation()
                enemy1.collision(main_char)
                if enemy1.battle:
                    battle_state = True
                
                pygame.display.update()          
            
            elif battle_state: 
                main_char.battle_state(battle_start)
                battle_start = 1   
                main_char.background.loadBackground("background2.png")
                main_char.background.blitbg()
                main_char.movement(keys, self.win, event, bg_limits, battle_state)
                enemy1_2.animation()
                
                pygame.display.update()


            
           
                    

           
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()