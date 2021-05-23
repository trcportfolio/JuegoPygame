import pygame 
from spritesheets import Spritesheet 
from settings import Settings
import characters
from backgrounds import Background



class mainChar:
    
    def __init__(self, screen, main): 
        self.settings = Settings()
        self.standing = True
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.fpsCounter = 0
        self.x = self.settings.positions[0][0]
        self.y = self.settings.positions[0][1]
        self.yUp_vel = 0
        self.yDown_vel = 0 
        self.xLeft_vel = 0
        self.xRight_vel = 0
        self.background = Background(screen)
        self.data = main 
       
       
        self.draw = Spritesheet(main[0], main[1], main[2], main[3], main[5])
        self.charRect = pygame.Rect(self.settings.positions[main[4]][0], self.settings.positions[main[4]][1],
                                    self.settings.charHeight, self.settings.charWidth)

        

    def walk_animation(self, screen, charRect, left, right, up, down, standing):

        if standing: 
            self.draw.drawsprite(screen, charRect, 16)
            self.fpsCounter = 0 

        if left:
            self.draw.drawsprite(screen, charRect, self.fpsCounter//3)
            self.fpsCounter += 1
            
            
        elif right:
            self.draw.drawsprite(screen, charRect,4*3 + self.fpsCounter//3)
            self.fpsCounter += 1
        
        elif up: 
            self.draw.drawsprite(screen, charRect, 4*5 + self.fpsCounter//3)
            self.fpsCounter += 1
        
        elif down: 
            self.draw.drawsprite(screen, charRect, 4*4 + self.fpsCounter//3)
            self.fpsCounter += 1
            
        
        if self.fpsCounter == 12:
            self.fpsCounter = 0
        
    def battle_state(self, battle):
        if battle == 0:
            self.charRect = pygame.Rect(self.settings.positions[self.data[4]][0], self.settings.positions[self.data[4]][1],
                                    self.settings.charHeight, self.settings.charWidth)
            self.x = self.settings.positions[self.data[4]][0]
            self.y = self.settings.positions[self.data[4]][1]

    def movement(self, keys, win, event, bg_limits, battle): 
        x_lim_left = bg_limits[0][0]
        x_lim_right = bg_limits[0][1]
        y_lim_up = bg_limits[1][0]
        y_lim_down = bg_limits[1][1]  
        self.hitbox = pygame.Rect(self.x + 9, self.y, 54, 64)
        pygame.draw.rect(win, (0,255,0),self.hitbox, 2)

        

        if event == pygame.KEYUP and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.xLeft_vel = 0
            self.xRight_vel = 0
            self.yDown_vel = 0
            self.yUp_vel = 0 
            self.standing = True
            self.left = False
            self.right = False
            self.up = False
            self.down = False
            self.walk_animation(win, self.charRect, self.left, self.right, self.up, self.down, self.standing) 

            
        elif keys[pygame.K_LEFT] and self.x > x_lim_left:
            self.xLeft_vel = -4
            self.yDown_vel = 0
            self.yUp_vel = 0  
            self.xRight_vel = 0 
            self.charRect.move_ip(self.xLeft_vel,0) 
            self.left = True 
            self.right = False
            self.down = False
            self.up = False
            self.standing = False
            
            self.walk_animation(win, self.charRect, self.left, self.right, self.up, self.down, self.standing)
            
        
        elif keys[pygame.K_LEFT] and self.x <= x_lim_left:
            self.xLeft_vel = 0
            self.yDown_vel = 0
            self.yUp_vel = 0
            self.left = False 
            self.right = False
            self.down = False
            self.up = False
            self.standing = True
            self.walk_animation(win, self.charRect, self.left, self.right, self.up, self.down, self.standing)
            
        elif keys[pygame.K_RIGHT] and self.x < x_lim_right:
            self.xRight_vel = 4
            self.xLeft_vel = 0
            self.yDown_vel = 0
            self.yUp_vel = 0
            self.charRect.move_ip(self.xRight_vel,0)
            self.left = False
            self.right = True
            self.down = False
            self.up = False
            self.standing = False
            
            self.walk_animation(win, self.charRect, self.left, self.right, self.up, self.down, self.standing)
        
        elif keys[pygame.K_RIGHT] and self.x >= x_lim_right:
            self.xRight_vel = 0  
            self.yDown_vel = 0
            self.yUp_vel = 0       
            self.left = False
            self.right = False
            self.down = False
            self.up = False
            self.standing = True
            self.walk_animation(win, self.charRect, self.left, self.right, self.up, self.down, self.standing)
                
        elif keys[pygame.K_UP] and self.y > y_lim_up:
            self.yUp_vel = -4
            self.yDown_vel = 0
            self.xLeft_vel = 0
            self.xRight_vel = 0
            self.charRect.move_ip(0, self.yUp_vel)
            self.up = True
            self.down = False
            self.left = False 
            self.right = False
            self.standing = False
            
            self.walk_animation(win, self.charRect, self.left, self.right, self.up, self.down, self.standing)

        elif keys[pygame.K_UP] and self.y <= y_lim_up:
            self.yUp_vel = 0
            self.xLeft_vel = 0
            self.xRight_vel = 0
            self.up = False
            self.down = False
            self.left = False
            self.rigth = False
            self.standing = True            
            self.walk_animation(win, self.charRect, self.left, self.right, self.up, self.down, self.standing)  

        elif keys[pygame.K_DOWN] and self.y < y_lim_down:
            self.yDown_vel = 4
            self.yUp_vel = 0
            self.xLeft_vel = 0
            self.xRight_vel = 0
            self.charRect.move_ip(0, self.yDown_vel)
            self.up = False
            self.down = True
            self.left = False
            self.right = False
            self.standing = False            
            self.walk_animation(win, self.charRect, self.left, self.right, self.up, self.down, self.standing)

        elif keys[pygame.K_DOWN] and self.y >= y_lim_down:
            self.yDown_vel = 0
            self.xLeft_vel = 0
            self.xRight_vel = 0
            self.up = False
            self.down = False
            self.left = False
            self.right = False
            self.standing = True            
            self.walk_animation(win, self.charRect, self.left, self.right, self.up, self.down, self.standing)
  
                
        if self.xLeft_vel == 0 and self.xRight_vel == 0 and self.yDown_vel == 0 and self.yUp_vel == 0:
            self.up = False
            self.down = False
            self.left = False
            self.right = False 
            self.standing = True
            self.walk_animation(win, self.charRect, self.left, self.right, self.up, self.down, self.standing)


        self.x = self.x + self.xRight_vel + self.xLeft_vel
        self.y = self.y + self.yUp_vel + self.yDown_vel  
        
        
        
        
                    

 
        
        
            
        
        

                                
          
        