import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('My game')
flag = True
my_font = pygame.font.Font('font/DancingScript-SemiBold.ttf', 30)
text = my_font.render('Vika', True, 'blue')
# foto = pygame.image.load('image/панда.jpg')
while flag:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, 'orange', (100, 100, 50, 80), 10)
    screen.blit(text, (300, 300))
    # screen.blit(foto, (50, 60))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()
    pygame.display.update()
