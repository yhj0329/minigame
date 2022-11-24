import pygame

pygame.init()

# 게임판 크기 설정
screen_width = 900
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 루프 시작
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        temp = pygame.mouse.get_pos()
        if 250 < temp[0] < 620:
            if 385 < temp[1] < 430:
                from DragonBall import dragonball
            elif 475 < temp[1] < 525:
                from EatGround import EatGround
pygame.quit()
exit()
