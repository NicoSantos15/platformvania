import pygame

pygame.init()

win = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Platformvania")

walkRight = [pygame.image.load('Media/frame_0.png'),
             pygame.image.load('Media/frame_1.png'),
             pygame.image.load('Media/frame_2.png'),
             pygame.image.load('Media/frame_3.png'),
             pygame.image.load('Media/frame_4.png'),
             pygame.image.load('Media/frame_5.png'),
             pygame.image.load('Media/frame_6.png'),
             pygame.image.load('Media/frame_7.png'),
             pygame.image.load('Media/frame_0.png')]

walkLeft = [pygame.image.load('Media/frame_0.png'),
             pygame.image.load('Media/frame_1.png'),
             pygame.image.load('Media/frame_2.png'),
             pygame.image.load('Media/frame_3.png'),
             pygame.image.load('Media/frame_4.png'),
             pygame.image.load('Media/frame_5.png'),
             pygame.image.load('Media/frame_6.png'),
             pygame.image.load('Media/frame_7.png'),
             pygame.image.load('Media/frame_0.png')]

bg = pygame.image.load('Media/Reference (1).png')
bg = pygame.transform.scale(bg, (700,500))
char = [pygame.image.load('Media/idle1.png'),
        pygame.image.load('Media/idle2.png'),
        pygame.image.load('Media/idle3.png'),
        pygame.image.load('Media/idle4.png')]

x = 50
y = 340 # Y-Position of the character. Lower value = higher position in screen
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char[1], (x, y))
        walkCount = 0

    pygame.display.update()


run = True

while run:
    clock.tick(42)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

pygame.quit()