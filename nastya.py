import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption('My Game')
flag = True
foto_new = pygame.image.load('image/nAST_page-0001.jpg')
foto = pygame.transform.scale(foto_new, (800, 450))
walk_right = [pygame.image.load('image/человек_правая/чел1_правая.png'),
              pygame.image.load('image/человек_правая/чел2_правая.png'),
              pygame.image.load('image/человек_правая/чел3_правая.png'),
              pygame.image.load('image/человек_правая/чел4_правая.png')]
walk_left = [pygame.image.load('image/человек_левая/чел1_лев (2).png'),
             pygame.image.load('image/человек_левая/чел4_лев (2).png'),
             pygame.image.load('image/человек_левая/чел3_лев.png'),
             pygame.image.load('image/человек_левая/чел2_лев.png')]
chet = 0
x_pos = 0
sound = pygame.mixer.Sound('sound/river-night_gkhvj8e_-1.mp3')
sound.play()
x = 100
player_speed = 5
jump = 7
flag_jump = False
while flag:
    screen.blit(foto, (x_pos, 0))
    screen.blit(foto, (x_pos + 800, 0))
    # =======================================
    if chet == 3:
        chet = 0
    else:
        chet += 1
    if x_pos == -800:
        x_pos = 0
    else:
        x_pos -= 10
    # =======================================
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 10:
        x -= player_speed
    elif keys[pygame.K_RIGHT] and x < 710:
        x += player_speed

    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[chet], (x, 290))
    else:
        screen.blit(walk_right[chet], (x, 290))

    # if not flag_jump:
    #     if keys[pygame.K_SPACE]:
    #         flag_jump = True
    # else:
    #
    #




    # =======================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()
    pygame.display.update()
    clock.tick(12)
