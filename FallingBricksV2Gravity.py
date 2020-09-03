import pygame
import time
import random
pygame.init()

pygame.display.set_caption('Falling Bricks v2')
    
screen = pygame.display.set_mode([800, 600])
RED = (255,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

clock = pygame.time.Clock()

timer = 0
score = 0

create_block = 0

block_random = 100

running = True

#Basic Sprite class
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 2
#Creates player
player = Rectangle(RED, 25, 25)
player.rect.x = 375
player.rect.y = 575
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

#Creates initial block
block = Rectangle(YELLOW, 25, 25)
block.rect.x = random.randrange (0, 800)
block.rect.y = 0
block_list = pygame.sprite.Group()
block_list.add(block)


isjump = False
F = 0
v = 5
m = 2

x_changeR = 0
x_changeL = 0

#Main game loop
while running:
    #Event checker
    for event in pygame.event.get():
        #User closes window
        if event.type == pygame.QUIT:
            running = False
        #Movement keys    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_changeR = 5
            if event.key == pygame.K_LEFT:
                x_changeL = -5
            if event.key == pygame.K_UP:
                if isjump == False:
                    isjump = True
            #if event.key == pygame.K_DOWN:
                #print('hi')
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_changeR = 0
            if event.key == pygame.K_LEFT:
                x_changeL = 0
            #if event.key == pygame.K_UP:
                #print('hi')
            #if event.key == pygame.K_DOWN:
                #print('hi')

    if isjump == True:
        F =(1 / 2)*m*(v**2)

        player.rect.y -= F

        v = v-0.5

        if v<0:
            m =-1
        if v ==-7:
            isjump = False

            v = 5
            m = 2
            #player.rect.y = 575
    
    #Calls update function of blocks
    block_list.update()
    
    #keeps track of timer
    if timer == 60:
      score += 1
      timer = 0

    timer += 1

    #Controls block creation speed
    if score > 15 and score < 21:
        block_random = 90
    if score > 20 and score < 26:
        block_random = 70
    if score > 25 and score < 31:
        block_random = 50
    if score > 30 and score < 36:
        block_random = 30
    if score > 35 and score < 41:
        block_random = 15
    if score > 40:
        block_random = 5
    
    #Creates blocks
    create_block = random.randrange(0, block_random)
    if create_block == 0:
        block1 = Rectangle(YELLOW, 25, 25)
        block1.rect.x = random.randrange (0, 800)
        block1.rect.y = 0
        block_list.add(block1)

    #Checks for collision
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)

    for block1 in blocks_hit_list:
        running = False
    for block in blocks_hit_list:
        running = False

    screen.fill((0,255,255))

    all_sprites_list.draw(screen)
    block_list.draw(screen)

    player.rect.x += x_changeR
    player.rect.x += x_changeL

    #Creates borders for player
    if player.rect.x > 775:
        player.rect.x = 775
    if player.rect.x < 0:
        player.rect.x = 0
    if player.rect.y > 575:
        player.rect.y = 575

    clock.tick(60)

    pygame.display.flip()

print('You lasted {} seconds!!!!!'.format(score))  
pygame.quit()
