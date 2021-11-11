#!/usr/bin/env python3

# Import all the necessary 
import math 
import pygame 

from breakout_variables import *
from breakout_graphics import *

# Creates surface and background and initializes all pygame modules
screen = pygame.display.set_mode([1280, 720], 0, 32)
background = pygame.Surface(screen.get_size())    
pygame.init()

class Block(pygame.sprite.Sprite):
    """ The objective to destroy in the game"""

    def __init__(self, x, y):
        """ The blocks consists of a position on coord (x,y)"""
        
        super().__init__()

        # Assigns the block attributes of custom graphics and location on screen
        self.image = pygame.Surface([64, 64])
        self.image = block_img
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

class Ball(pygame.sprite.Sprite):
    """ The object used for destroying the blocks""" 
    
    # Properties of ball, valuables saved externally for simpler edits
    x = ballX
    y = ballY
    velocity = ballVelocity
    direction = ballDirection
    radius = ballRadius
    
    def __init__(self):
        
        super().__init__()
        
        # Assigns the ball attributes with custom graphics
        # and get display values for boundingbox
        self.image = pygame.Surface([self.radius, self.radius])
        self.image = ball_img
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

    
    def bounce(self, diff):
        """ Updates the ball if it hits an object vertically """ 

        self.direction = (180 - self.direction) % 360
        self.direction -= diff
    
    
    def update(self):
        """ Update the ball if it hits the boundaries horisontally and vertically """
        
        direction_radians = math.radians(self.direction)

        self.x += self.velocity *math.sin(direction_radians)
        self.y -= self.velocity *math.cos(direction_radians)

        self.rect.x = self.x
        self.rect.y = self.y 
        
        top_wall = self.y <= 0
        left_wall = self.x <= 0
        right_wall = self.x > self.screenwidth - self.radius
        bottom = self.y > 720

        
        if top_wall: 
            self.bounce(0)
            self.y = 1
        
        if left_wall:
            self.direction = (360 - self.direction) % 360
            self.x = 1
        
        if right_wall:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.radius - 1
        
        if bottom:
            return True
        else:
            return False 

class Player(pygame.sprite.Sprite):
    """ This class represents the platform at the bottom half that the player controls. """ 

    def __init__(self): 
       
        super().__init__()

        self.width = pad_width
        self.height = pad_height

        self.image = pygame.Surface([self.width, self.height])
        self.image = player_img
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

        self.rect.x = 0 
        self.rect.y = self.screenheight - self.height

    def update(self):
        """ Update the player position. """
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += 13 
            if self.rect.x > self.screenwidth - self.width: 
                self.rect.x = self.screenwidth - self.width
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= 13 
            if self.rect.x < 0:
                self.rect.x = 0
        # Let the player exit the game by pressing escape
        if key_pressed[pygame.K_ESCAPE]:
            print("Game closed manually by ESCAPE")
            exit()
        

# Initialise ready for game loop
# Hide cursor
pygame.mouse.set_visible(0) 
# Import clock for frames per second configuration
clock = pygame.time.Clock()
# Name the game window
pygame.display.set_caption('Breakout made by "bro041"') 
# Make font ready for loss/win scenario
font = pygame.font.Font("./assets/arcade.ttf", 72) 

# Assigns the different sprite classes their group classes
blocks = pygame.sprite.Group()
ball = pygame.sprite.Group()
player = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

user = Player()
allsprites.add(user) 
player.add(user)
firecharge = Ball()
allsprites.add(firecharge)
ball.add(firecharge)

# Loop for creating the blocks
for row in range(3):
    
    for column in range(0, blockcount): 
        
        glowstone = Block(column * (64 + 16), block_top)                                          
        blocks.add(glowstone)
        allsprites.add(glowstone)
    
    block_top += 70

# Defeat is false
Defeat = False



# Main game loop
while True:

    # 60 frames per second
    clock.tick(60)                                                                
    
    # Quit program if program is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("GAME PROPERLY CLOSED")
            exit()

    # As long as game is not lost or won
    if not Defeat and len(blocks) > 0:
        user.update()
        Defeat = firecharge.update()

    # If lost, print message
    if Defeat:
        text = font.render("You lost", True, (255, 0, 0))
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 300
        screen.blit(text, textpos)
    
    # If won, print message
    if len(blocks) == 0:
        text = font.render("You won", True, (0, 255, 0))
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 300
        screen.blit(text, textpos)

    # Bounce ball if collides with platform, dont remove object
    if pygame.sprite.spritecollide(user, ball, False):
        
        diff = (user.rect.x + user.width/2) - (firecharge.rect.x + firecharge.radius/2)
 
        firecharge.rect.y = screen.get_height() - user.rect.height - firecharge.rect.height - 1
        firecharge.bounce(diff)

    # Remove block if ball hits, add one to score
    block_hit = pygame.sprite.spritecollide(firecharge, blocks, True)
    if block_hit:
        score += 1
    
    # if block_hit, prevent ball from going to the next block without bouncing back first
    if len(block_hit) > 0:
        firecharge.bounce(0)

    # Draw everything 
    allsprites.draw(screen)
    draw_text(screen, str(score), 36, 1250, 650)
    pygame.display.flip()
    screen.blit(background_img, [0, 0])

# Uninitializes all pygame modules
pygame.quit()