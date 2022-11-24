import pygame
import random
import time

pygame.init()


# 플레이어 클래스 설정
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.gatherCount = 0
        if direction == "left":
            self.image = pygame.image.load('./man.png')
        else:
            self.image = pygame.image.load('./man.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


# 공격 클래스 설정
class Attacker(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        if direction == "left":
            self.image = pygame.image.load('./attack.png')
            self.s_image = pygame.image.load('./specialattack.png')
        else:
            self.image = pygame.image.load('./attack.png')
            self.s_image = pygame.image.load('./specialattack.png')
        self.s_effect = pygame.image.load('./specialeffect.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


# 방어 클래스 설정
class Shielder(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        if direction == "left":
            self.image = pygame.image.load('./attack.png')
        else:
            self.image = pygame.image.load('./attack.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


# 안내문 변화
def show_explain():
    screen.blit(background, (0, 0))
    screen.blit(P1.image, P1.rect)
    screen.blit(com.image, com.rect)
    if P1.gatherCount >= 5:
        explain_text = font.render("A : Gathering / S : Special Attack / D : Shield", False, (0, 0, 0))
    else:
        explain_text = font.render("A : Gathering / S : Attack / D : Shield", False, (0, 0, 0))
    gather_text = font.render(f"GatherCount : {P1.gatherCount}", False, (0, 0, 0))
    com_gather_text = font.render(f"comGatherCount : {com.gatherCount}", False, (0, 0, 0))
    screen.blit(explain_text, (10, 610))
    screen.blit(gather_text, (10, 20))
    screen.blit(com_gather_text, (710, 20))
    pygame.display.flip()


# 게임 종료 안내
def defeat():
    screen.fill((0, 0, 0))
    big_font = pygame.font.SysFont('Tahoma', 50)
    defect_text = big_font.render("Defeat", False, (255, 255, 255))
    screen.blit(defect_text, (370, 280))
    pygame.display.flip()


def win():
    screen.fill((0, 0, 0))
    big_font = pygame.font.SysFont('Tahoma', 50)
    defect_text = big_font.render("Win", False, (255, 255, 255))
    screen.blit(defect_text, (370, 280))
    pygame.display.flip()


# 게임판 세팅
screen_width = 900
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 설정
pygame.display.set_caption("DragoonBall Game")
background = pygame.image.load("./background.png")
screen.blit(background, (0, 0))

# 기모으기 이펙트
gathering = pygame.image.load("./gathering.png")

# 초기 화면 세팅
P1 = Player(150, 430, "left")
A1 = Attacker(P1.rect.centerx + 100, P1.rect.centery, "left")
S1 = Shielder(P1.rect.centerx, P1.rect.centery, "left")
com = Player(750, 430, "right")
font = pygame.font.SysFont('Tahoma', 20)
show_explain()


# 상대 세팅
def com_choice(com_status):
    # com Gathering
    if com_status == 0:
        com.gatherCount = com.gatherCount + 1
    # com attack
    elif com_status == 2:
        if com.gatherCount >= 5:
            com.gatherCount = com.gatherCount - 5
        else:
            com.gatherCount = com.gatherCount - 1


# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # gathering
            if event.key == pygame.K_a:
                '''if com.gatherCount > 0:
                    temp = random.randint(0, 2)
                    com_choice(temp)
                else:
                    temp = random.randint(0, 1)
                    com_choice(temp)'''
                temp = 2
                P1.gatherCount = P1.gatherCount + 1
                if temp == 0:
                    screen.blit(gathering, (77, 410))
                    screen.blit(P1.image, P1.rect)
                    screen.blit(gathering, (677, 410))
                    screen.blit(com.image, com.rect)
                    pygame.display.flip()
                    time.sleep(1)
                    show_explain()
                elif temp == 1:
                    screen.blit(gathering, (77, 410))
                    screen.blit(P1.image, P1.rect)
                    comS = Shielder(com.rect.centerx, com.rect.centery, "right")
                    screen.blit(comS.image, comS.rect)
                    pygame.display.flip()
                    time.sleep(1)
                    show_explain()
                    del comS
                elif temp == 2:
                    screen.blit(gathering, (77, 410))
                    screen.blit(P1.image, P1.rect)
                    comA = Attacker(com.rect.centerx - 100, com.rect.centery, "right")
                    screen.blit(comA.s_image, comA.rect)
                    time.sleep(1)
                    if com.gatherCount >= 5:
                        while not pygame.sprite.collide_rect(P1, comA):
                            comA.rect.centerx = comA.rect.centerx - 100
                            screen.blit(comA.s_image, comA.rect)
                            pygame.display.flip()
                            time.sleep(0.1)
                            show_explain()
                        screen.blit(comA.s_effect, P1.rect)
                        time.sleep(5)
                    else:
                        while not pygame.sprite.collide_rect(P1, comA):
                            comA.rect.centerx = comA.rect.centerx - 50
                            screen.blit(comA.image, comA.rect)
                            pygame.display.flip()
                            time.sleep(0.1)
                            show_explain()
                    defeat()
            # attack
            elif event.key == pygame.K_s:
                if P1.gatherCount > 0:
                    if com.gatherCount > 0:
                        temp = random.randint(0, 2)
                        com_choice(temp)
                    else:
                        temp = random.randint(0, 1)
                        com_choice(temp)
                    if P1.gatherCount >= 5:
                        P1.gatherCount = P1.gatherCount - 5
                        show_explain()
                    else:
                        P1.gatherCount = P1.gatherCount - 1
                else:
                    waringText = font.render("Gathering First", True, (0, 0, 0), (255, 255, 255))
                    screen.blit(waringText, (370, 280))
                    pygame.display.flip()
            # defense
            elif event.key == pygame.K_d:
                if com.gatherCount > 0:
                    temp = random.randint(0, 2)
                    com_choice(temp)
                else:
                    temp = random.randint(0, 1)
                    com_choice(temp)
                screen.blit(S1.image, S1.rect)
                pygame.display.flip()

pygame.quit()
