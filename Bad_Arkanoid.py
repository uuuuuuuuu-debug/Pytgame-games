import pygame
timer = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Bounce")

def hit(cx, vx, cy, pady, r, vy, padx, lengh):
    if cy <= r or cy + r >= 800:
        vy = -vy
    if cy + r >= pady + 13 and cx <= padx + lengh // 2 and cx >= padx - lengh // 2:
        vy = -vy
    if cx <= r or cx + r >= 800:
        vx = -vx
    return (vx, vy)

k = True
cx = 100
cy = 400
vx = 5
vy = -5
radius = 50
Green = (20, 200, 16)
pady = 700
padh = 13
lengh = 200
while k:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            k = False

    padx = pygame.mouse.get_pos()[0] - lengh // 2
    (vx, vy) = hit(cx, vx, cy, pady, radius, vy, padx, lengh)
    cx += int(vx)
    cy += int(vy)
    pygame.draw.rect(screen, (255, 255, 255), (int(padx), pady, lengh, padh))
    pygame.draw.circle(screen, Green, (cx, cy), radius)
    pygame.display.update()
    timer.tick(120)
    screen.fill((0, 0, 0))

    if cy > pady + radius:
        k = False
        print("You Lost")
pygame.quit()
