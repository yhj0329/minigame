import pygame

pygame.init()

# 크기 설정
screen_width = 900
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 설정
pygame.display.set_caption("Mini Game")
background = pygame.image.load("./minigame.png")
background = pygame.transform.scale(background, (900, 640))
screen.blit(background, (0, 0))
pygame.display.flip()

# 버튼 이미지 로드
db_image = pygame.image.load("./dragonball.png")
db_image = pygame.transform.scale(db_image, (350, 150))
db_char = pygame.image.load("./dragonball_attack.png")
db_char = pygame.transform.scale(db_char, (80, 60))

eg_image = pygame.image.load("./eating_ground.png")
eg_image = pygame.transform.scale(eg_image, (330, 90))
eg_char = pygame.image.load("./eating_character.png")
eg_char = pygame.transform.scale(eg_char, (70, 70))

# 버튼 이미지 보이기
screen.blit(db_image, (300, 320))
screen.blit(db_char, (240, 377))
screen.blit(eg_image, (320, 460))
screen.blit(eg_char, (245, 470))
pygame.display.flip()

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
                from eating_ground import eating_ground
pygame.quit()
