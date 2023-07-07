import pygame

pygame.init()
size = W, H = 400, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Задание №2')
flag = True

while flag:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 69, 36), (130, 160, 100, 100))
    pygame.draw.rect(screen, (0, 255, 0), (120, 150, 100, 100))
    # =============================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()
    pygame.display.update()
