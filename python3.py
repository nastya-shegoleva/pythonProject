import pygame
import random

if __name__ == '__main__':
    pygame.init()
    size = W, H = 400, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Задание №3')
    for _ in range(150):
        screen.fill((255, 255, 255), (random.random() * W, random.random() * H, 3, 2))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

