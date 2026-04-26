import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

# Холст (ВАЖНО — чтобы рисунок не исчезал)
canvas = pygame.Surface((800, 600))
canvas.fill((255, 255, 255))

drawing = False
shape = "square"
start_pos = (0, 0)

running = True
while running:
    screen.blit(canvas, (0, 0))  # рисуем сохранённый холст

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # выбор фигуры
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                shape = "square"
            if event.key == pygame.K_2:
                shape = "right_triangle"
            if event.key == pygame.K_3:
                shape = "equilateral"
            if event.key == pygame.K_4:
                shape = "rhombus"

        # начало рисования
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos

        # конец рисования
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos

            x1, y1 = start_pos
            x2, y2 = end_pos

            if shape == "square":
                size = abs(x2 - x1)
                pygame.draw.rect(canvas, (0, 0, 0), (x1, y1, size, size), 2)

            elif shape == "right_triangle":
                pygame.draw.polygon(canvas, (0, 0, 0),
                                    [(x1, y1), (x2, y2), (x1, y2)], 2)

            elif shape == "equilateral":
                pygame.draw.polygon(canvas, (0, 0, 0),
                                    [(x1, y1),
                                     (x2, y1),
                                     ((x1 + x2) // 2, y1 - abs(x2 - x1) // 2)], 2)

            elif shape == "rhombus":
                pygame.draw.polygon(canvas, (0, 0, 0),
                                    [(x1, y1),
                                     ((x1 + x2) // 2, y1 - 50),
                                     (x2, y1),
                                     ((x1 + x2) // 2, y1 + 50)], 2)

    pygame.display.update()
    clock.tick(60)