import pygame
import random

pygame.init()

display_width = 800
display_height = 600



clock = pygame.time.Clock()
marioImg = pygame.image.load('mario.png')
running = True

LBLUE = (176,224,230)
BROWN = (153, 76, 0)
YELLOW = (204,204,0)

SKY = 0
BRICK = 1
QUESTION = 2
textures = {
    SKY : LBLUE,
    BRICK: BROWN,
    QUESTION: YELLOW
}
TILESIZE = 30
MAPWIDTH = 30
MAPHEIGHT = 20
resources = [SKY, BRICK, QUESTION]
tilemap = [[SKY for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
gameDisplay = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
def mario(x,y):
    gameDisplay.blit(marioImg, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.85)
x_change = 0
y_change = 0

for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0, 15)
        if randomNumber == 0:
            tile = QUESTION
        elif randomNumber >= 1 and randomNumber <= 5:
            tile = SKY
        else:
            tile = BRICK
        tilemap[rw][cl] = tile

def jump():
    y_change = 0
    playerGravity = 1.2
    playerIsJumping = True
    playerVelocity = 50
    delta = 5
    if(playerIsJumping):
        playerVelocity -= playerGravity * delta

    y_change += playerVelocity
    mario(x,y_change)
    playerIsJumping = False
    playerVelocity = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print(event)
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            pygame.draw.rect(gameDisplay, textures[tilemap[row][column]],(column*TILESIZE, row*TILESIZE,TILESIZE,TILESIZE))
            #gameDisplay.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
            elif event.key == pygame.K_RIGHT:
                x_change = 10
            elif event.key == pygame.K_SPACE:
                jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x += x_change
    mario(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
