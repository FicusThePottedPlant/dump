import random
import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.add(balls)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius, 1)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randrange(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        a, *b = (pygame.sprite.spritecollide(self, balls, False))
        if b:
            a.vx, b[0].vx = b[0].vx, a.vx
            a.vy, b[0].vy = b[0].vy, a.vy
            # a.vx, b[0].vx = -a.vx, -b[0].vx
            # a.vy, b[0].vy = -a.vy, -b[0].vy
            b[0].rect = b[0].rect.move(b[0].vx, b[0].vy)
        if pygame.sprite.spritecollide(self, horizontal_borders, False):
            self.vy = -self.vy
        if pygame.sprite.spritecollide(self, vertical_borders, False):
            self.vx = -self.vx

        self.rect = self.rect.move(self.vx, self.vy)


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


if __name__ == '__main__':

    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    fps = 60
    all_sprites = pygame.sprite.Group()
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    balls = pygame.sprite.Group()
    clock = pygame.time.Clock()
    running = True
    C = 0
    Border(C, C, width - C, C)
    Border(C, height - C, width - C, height - C)
    Border(C, C, C, height - C)
    Border(width - C, C, width - C, height - C)
    for i in range(10):
        Ball(20, random.randint(20, 550), random.randint(20, 550))
    while running:

        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Ball(20, *pygame.mouse.get_pos())

        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(fps)