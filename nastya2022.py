import pygame

pygame.init()
size = W, H = 600, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Задание №1')
flag = True
pi = 3.14
my_font = pygame.font.Font('font/DancingScript-SemiBold.ttf', 30)
text = my_font.render('Lesson 3. Snowman', True, (25, 255, 50))
# text = my_font.render('Lesson 3. Snowman', True, (70, 255, 100))
# text = my_font.render('Lesson 3. Snowman', True, 'blue')
# text = my_font.render('Lesson 3. Snowman', True, 'black')
while flag:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'black', (W // 2, 500), 110, 3)
    pygame.draw.circle(screen, 'black', (W // 2, 313), 80, 3)
    pygame.draw.line(screen, 'black', [100, 350], [198, 458], 3)
    pygame.draw.line(screen, 'black', [400, 458], [500, 350], 3)
    pygame.draw.circle(screen, 'black', (330, 300), 4)
    pygame.draw.circle(screen, 'black', (275, 300), 4)
    pygame.draw.polygon(screen, 'orange', ((300, 325), (292, 330), (308, 330)))
    pygame.draw.arc(screen, 'black', (290, 340, 20, 10), pi, 2 * pi, 3)
    screen.blit(text, (200, 100))
    # =============================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()
    pygame.display.update()




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



import pygame

pygame.init()
num = list(map(int, input().split()))
size = num[0]
coll_kletka = num[1]
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption('Задание №4')
flag = True
if size % coll_kletka != 0 or int(size) != size or int(coll_kletka) != coll_kletka:
    print('Неправильный формат ввода')
else:
    sz = size // coll_kletka
    while flag:
        for i in range(size // coll_kletka):
            pygame.draw.rect(screen, (0, 0, 0), (i * sz, i * sz, sz, sz))
        for i in range(size // coll_kletka):
            pygame.draw.rect(screen, (255, 255, 255), (i * sz + sz, i * sz, sz, sz))
        for i in range(size // coll_kletka):
            pygame.draw.rect(screen, (255, 255, 255), (i * sz - sz, i * sz, sz, sz))
        for i in range(size // coll_kletka):
            pygame.draw.rect(screen, (0, 0, 0), (i * sz + 2 * sz, i * sz, sz, sz))
        for i in range(size // coll_kletka):
            pygame.draw.rect(screen, (255, 255, 255), (i * sz + 3 * sz, i * sz, sz, sz))
        for i in range(size // coll_kletka):
            pygame.draw.rect(screen, (0, 0, 0), (i * sz + 4 * sz, i * sz, sz, sz))
        for i in range(size // coll_kletka):
            pygame.draw.rect(screen, (0, 0, 0), (i * sz - 2 * sz, i * sz, sz, sz))
        for i in range(size // coll_kletka):
            pygame.draw.rect(screen, (255, 255, 255), (i * sz - 3 * sz, i * sz, sz, sz))
        for i in range(size // coll_kletka):
            pygame.draw.rect(screen, (0, 0, 0), (i * sz - 4 * sz, i * sz, sz, sz))
        # =============================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()
        pygame.display.update()
