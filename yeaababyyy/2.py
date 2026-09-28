import pygame

pygame.init()
screen2 = pygame.Surface((800,800))
screen = pygame.display.set_mode((800,800))
running = True
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
clock = pygame.time.Clock()
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 20)

    keys = pygame.key.get_pressed()
    nokeys = pygame.key.get_just_released()

    if keys[pygame.K_UP]:
        player_pos.y -= 300*dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300*dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300*dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300*dt
    if keys[pygame.K_SPACE]:
        pp2 = player_pos
        pygame.draw.circle(screen2, "black", pp2, 20)
    if nokeys[pygame.K_SPACE]:
        pp2 = 0

    pygame.display.flip()
    dt = clock.tick(60)/1000

pygame.quit()
