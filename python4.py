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
