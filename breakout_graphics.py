import pygame

# Graphics on the blocks, ball, player-controlled-pad and the background
block_img = pygame.image.load("glowstone.png") 
ball_img = pygame.image.load("fire_charge.png")                
player_img = pygame.image.load("bouncer.png") 
background_img = pygame.image.load("nether.png") 

# Amount of times ball has hit the bricks 
font_name = pygame.font.match_font("arial")
def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0,233,233))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)