import pygame, random

pygame.init()

gatherCount = 0

screen_width = 900
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("DagronBall Game")
background = pygame.image.load("./DagronBall/background.png")
screen.blit(background, (0, 0))

font = pygame.font.SysFont('Tahoma', 20)
ExplainText = font.render("A : Gathering / S : Attack / D : Defense", True, (0,0,0))
screen.blit(ExplainText,(10,610))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./DagronBall/man.png')

class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load()

P1 = Player()
P2 = Player()
screen.blit(P1.image, (50, 300))
screen.blit(P2.image, (650, 300))

# game_over = font.render("GG", True, BLACK)

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        while(event.type == pygame.KEYDOWN): # 키를 누르기 전까지 멈추기
            if event.key == pygame.K_a:

            if event.key == pygame.K_s:

            if event.key == pygame.K_d:


pygame.quit()