import pygame


pygame.init()
width, height = (200,300)
screen = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)
FONT = pygame.font.Font("freesansbold.ttf", 50)


def loop():
    clock = pygame.time.Clock()
    number = 0
    # The button is just a rect.
    buttonn = pygame.Rect(0, 100, 200, 200)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # This block is executed once for each MOUSEBUTTONDOWN event.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    # `event.pos` is the mouse position.
                    if buttonn.collidepoint(event.pos):
                        # Increment the number.
                        number += 1

        screen.fill(WHITE)
        pygame.draw.rect(screen, GRAY, buttonn)
        text_surf = FONT.render(str(number), True, BLACK)
        # You can pass the center directly to the `get_rect` method.
        text_rect = text_surf.get_rect(center=(width/2, 30))
        screen.blit(text_surf, text_rect)
        pygame.display.update()

        clock.tick(30)


loop()
pygame.quit()