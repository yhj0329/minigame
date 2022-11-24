import pygame
import random
import time

if __name__ == "__main__":
    import os
    os.chdir('..')

pygame.init()


# 플레이어 클래스 설정
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.gatherCount = 0
        self.image = pygame.image.load('./DragonBall/player.png')
        self.image = pygame.transform.scale(self.image, (200, 180))
        self.gimage = [pygame.image.load('./DragonBall/g1.png'), pygame.image.load('./DragonBall/g2.png'),
                       pygame.image.load('./DragonBall/g3.png'), pygame.image.load('./DragonBall/g4.png'),
                       pygame.image.load('./DragonBall/g5.png')]
        for i in range(0, 5):
            self.gimage[i] = pygame.transform.scale(self.gimage[i], (100, 200))
        if direction == "right":
            self.image = pygame.image.load('./DragonBall/com.png')
            self.image = pygame.transform.scale(self.image, (200, 180))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


# 공격 클래스 설정
class Attacker(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./DragonBall/attack.png')
        self.image = pygame.transform.scale(self.image, (157, 100))
        self.s_image = pygame.image.load('./DragonBall/special_attack.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x + 50
        if direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.centerx = x - 50
        self.s_effect = pygame.image.load('./DragonBall/special_effect.png')
        self.rect.centery = y


# 방어 클래스 설정
class Shielder(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./DragonBall/barrier.png')
        self.image = pygame.transform.scale(self.image, (106, 173))
        self.rect = self.image.get_rect()
        self.rect.centerx = x - 50
        if direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.centerx = x + 50
        self.rect.centery = y


# 안내문 변화
def show_explain(shield):
    screen.blit(background, (0, 0))
    if P1.gatherCount >= 5:
        screen.blit(P1.gimage[4], (60, 320))
    if com.gatherCount >= 5:
        screen.blit(P1.gimage[4], (740, 320))
    for i in range(1, 5):
        if P1.gatherCount == i:
            screen.blit(com.gimage[i-1], (60, 320))
        if com.gatherCount == i:
            screen.blit(com.gimage[i - 1], (740, 320))
        screen.blit(P1.image, P1.rect)
        screen.blit(com.image, com.rect)
    if shield == 'com':
        screen.blit(comS.image, comS.rect)
    elif shield == 'player':
        screen.blit(S1.image, S1.rect)
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
    screen.fill((255, 255, 255))
    loser = pygame.image.load('./DragonBall/loser.png')
    loser = pygame.transform.scale(loser, (640, 650))
    screen.blit(loser, (110, 0))
    pygame.display.flip()


def win():
    screen.fill((255, 255, 255))
    winner = pygame.image.load('./DragonBall/winner.png')
    winner = pygame.transform.scale(winner, (640, 650))
    screen.blit(winner, (130, 0))
    pygame.display.flip()


# 게임판 세팅
screen_width = 900
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 설정
pygame.display.set_caption("DragoonBall Game")
background = pygame.image.load("./DragonBall/background.png")
screen.blit(background, (0, 0))

# 기모으기 이펙트
gathering = pygame.image.load("./DragonBall/gathering.png")

# 초기 화면 세팅
P1 = Player(120, 420, "left")
com = Player(770, 420, "right")
font = pygame.font.SysFont('Tahoma', 20)
show_explain(False)


# 상대 세팅
def com_random():
    if com.gatherCount == 0:
        tmp = random.randint(0, 9) % 2
        com_choice(tmp)
    elif com.gatherCount >= 5:
        tmp = 2
    else:
        tmp = random.randint(2, 9) % 3
        com_choice(tmp)
    print(check_com_status[tmp])
    return tmp


def com_choice(com_status):
    # com Gathering
    if com_status == 0:
        com.gatherCount = com.gatherCount + 1


# special attack 이펙트
def com_special_attack_effect():
    comA.rect.centerx = 290
    screen.blit(comA.s_image, comA.rect)
    pygame.display.flip()
    time.sleep(0.7)
    for _ in range(0, 3):
        screen.blit(comA.s_effect, (0, 250))
        pygame.display.flip()
        time.sleep(0.3)
        show_explain('')
        time.sleep(0.4)


def player_special_attack_effect():
    A1.rect.centerx = 290
    screen.blit(A1.s_image, A1.rect)
    pygame.display.flip()
    time.sleep(0.7)
    for _ in range(0, 3):
        screen.blit(A1.s_effect, (600, 250))
        pygame.display.flip()
        time.sleep(0.3)
        show_explain('')
        time.sleep(0.4)


check_com_status = {0: 'gathering', 1: 'shield', 2: 'attack'}

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # gathering
            if event.key == pygame.K_a:
                if com.gatherCount == 0:
                    temp = 0
                    com_choice(temp)
                elif com.gatherCount >= 5:
                    temp = 2
                else:
                    temp = random.randint(2, 9) % 3
                    com_choice(temp)
                print(check_com_status[temp])
                P1.gatherCount = P1.gatherCount + 1
                if temp == 0:
                    screen.blit(P1.image, P1.rect)
                    screen.blit(gathering, (77, 410))
                    screen.blit(com.image, com.rect)
                    screen.blit(gathering, (677, 410))
                    pygame.display.flip()
                    time.sleep(1)
                    show_explain('')
                elif temp == 1:
                    screen.blit(P1.image, P1.rect)
                    screen.blit(gathering, (77, 410))
                    comS = Shielder(com.rect.centerx, com.rect.centery, "right")
                    screen.blit(comS.image, comS.rect)
                    pygame.display.flip()
                    time.sleep(1)
                    show_explain('')
                    del comS
                elif temp == 2:
                    screen.blit(P1.image, P1.rect)
                    screen.blit(gathering, (77, 410))
                    comA = Attacker(com.rect.centerx, com.rect.centery, "right")
                    if com.gatherCount >= 5:
                        com.gatherCount = com.gatherCount - 5
                        show_explain('')
                        com_special_attack_effect()
                    else:
                        com.gatherCount = com.gatherCount - 1
                        screen.blit(comA.image, comA.rect)
                        pygame.display.flip()
                        time.sleep(0.5)
                        while not pygame.sprite.collide_rect(P1, comA):
                            show_explain('')
                            comA.rect.centerx = comA.rect.centerx - 50
                            screen.blit(comA.image, comA.rect)
                            pygame.display.flip()
                            time.sleep(0.2)
                    del comA
                    defeat()
                    time.sleep(3)
                    running = False
            # attack
            elif event.key == pygame.K_s:
                if P1.gatherCount > 0:
                    temp = com_random()
                    if temp == 0:
                        screen.blit(com.image, com.rect)
                        screen.blit(gathering, (677, 410))
                        A1 = Attacker(P1.rect.centerx, P1.rect.centery, "left")
                        if P1.gatherCount >= 5:
                            P1.gatherCount = P1.gatherCount - 5
                            show_explain('')
                            player_special_attack_effect()
                        else:
                            P1.gatherCount = P1.gatherCount - 1
                            pygame.display.flip()
                            time.sleep(0.5)
                            while not pygame.sprite.collide_rect(A1, com):
                                show_explain('')
                                A1.rect.centerx = A1.rect.centerx + 50
                                screen.blit(A1.image, A1.rect)
                                pygame.display.flip()
                                time.sleep(0.2)
                        del A1
                        win()
                        time.sleep(3)
                        running = False
                    elif temp == 1:
                        comS = Shielder(com.rect.centerx, com.rect.centery, "right")
                        A1 = Attacker(P1.rect.centerx, P1.rect.centery, "left")
                        if P1.gatherCount >= 5:
                            P1.gatherCount = P1.gatherCount - 5
                            show_explain('com')
                            player_special_attack_effect()
                            del A1, comS
                            win()
                            time.sleep(3)
                            running = False
                        else:
                            P1.gatherCount = P1.gatherCount - 1
                            while not pygame.sprite.collide_rect(A1, comS):
                                show_explain('com')
                                A1.rect.centerx = A1.rect.centerx + 50
                                screen.blit(A1.image, A1.rect)
                                pygame.display.flip()
                                time.sleep(0.2)
                            del A1, comS
                            show_explain('')
                    elif temp == 2:
                        A1 = Attacker(P1.rect.centerx, P1.rect.centery, "left")
                        comA = Attacker(com.rect.centerx, P1.rect.centery, "right")
                        if P1.gatherCount >= 5:
                            if com.gatherCount >= 5:
                                P1.gatherCount = P1.gatherCount - 5
                                com.gatherCount = com.gatherCount - 5
                                show_explain('')
                                A1.rect.centerx = 290
                                screen.blit(A1.s_image, A1.rect)
                                pygame.display.flip()
                                time.sleep(0.7)
                                for _ in range(0, 3):
                                    screen.blit(A1.s_effect, (310, 250))
                                    pygame.display.flip()
                                    time.sleep(0.3)
                                    show_explain('')
                                    time.sleep(0.4)
                                del A1, comA
                            else:
                                P1.gatherCount = P1.gatherCount - 5
                                com.gatherCount = com.gatherCount - 1
                                show_explain('')
                                for _ in range(0, 3):
                                    show_explain('')
                                    comA.rect.centerx = comA.rect.centerx - 50
                                    screen.blit(comA.image, comA.rect)
                                    pygame.display.flip()
                                    time.sleep(0.2)
                                A1.rect.centerx = 290
                                A1.rect.centery = A1.rect.centery + 50
                                screen.blit(A1.s_image, A1.rect)
                                pygame.display.flip()
                                time.sleep(0.7)
                                for _ in range(0, 3):
                                    screen.blit(A1.s_effect, (600, 250))
                                    pygame.display.flip()
                                    time.sleep(0.3)
                                    show_explain('')
                                    time.sleep(0.4)
                                del A1, comA
                                win()
                                time.sleep(3)
                                running = False
                        else:
                            if com.gatherCount >= 5:
                                P1.gatherCount = P1.gatherCount - 1
                                com.gatherCount = com.gatherCount - 5
                                show_explain('')
                                for _ in range(0, 3):
                                    show_explain('')
                                    A1.rect.centerx = A1.rect.centerx + 50
                                    screen.blit(A1.image, A1.rect)
                                    pygame.display.flip()
                                    time.sleep(0.2)
                                comA.rect.centerx = 290
                                comA.rect.centery = comA.rect.centery + 50
                                screen.blit(comA.s_image, comA.rect)
                                pygame.display.flip()
                                time.sleep(0.7)
                                for _ in range(0, 3):
                                    screen.blit(comA.s_effect, (0, 250))
                                    pygame.display.flip()
                                    time.sleep(0.3)
                                    show_explain('')
                                    time.sleep(0.4)
                                del A1, comA
                                defeat()
                                time.sleep(3)
                                running = False
                            else:
                                P1.gatherCount = P1.gatherCount - 1
                                com.gatherCount = com.gatherCount - 1
                                while not pygame.sprite.collide_rect(A1, comA):
                                    show_explain('')
                                    A1.rect.centerx = A1.rect.centerx + 50
                                    comA.rect.centerx = comA.rect.centerx - 50
                                    screen.blit(A1.image, A1.rect)
                                    screen.blit(comA.image, comA.rect)
                                    pygame.display.flip()
                                    time.sleep(0.2)
                                del A1, comA
                                show_explain('')
                else:
                    waringText = font.render("Gathering First", True, (0, 0, 0), (255, 255, 255))
                    screen.blit(waringText, (370, 280))
                    pygame.display.flip()
                    time.sleep(1)
                    show_explain('')
            # defense
            elif event.key == pygame.K_d:
                temp = com_random()
                if temp == 0:
                    screen.blit(com.image, com.rect)
                    screen.blit(gathering, (677, 410))
                    S1 = Shielder(P1.rect.centerx, P1.rect.centery, "left")
                    screen.blit(S1.image, S1.rect)
                    pygame.display.flip()
                    time.sleep(1)
                    show_explain('')
                    del S1
                elif temp == 1:
                    comS = Shielder(com.rect.centerx, com.rect.centery, "right")
                    S1 = Shielder(P1.rect.centerx, P1.rect.centery, "left")
                    screen.blit(comS.image, comS.rect)
                    screen.blit(S1.image, S1.rect)
                    pygame.display.flip()
                    time.sleep(1)
                    show_explain('')
                    del S1, comS
                elif temp == 2:
                    S1 = Shielder(P1.rect.centerx, P1.rect.centery, "left")
                    comA = Attacker(com.rect.centerx, com.rect.centery, "right")
                    if com.gatherCount >= 5:
                        com.gatherCount = com.gatherCount - 5
                        show_explain('player')
                        com_special_attack_effect()
                        del S1, comA
                        defeat()
                        time.sleep(3)
                        running = False
                    else:
                        com.gatherCount = com.gatherCount - 1
                        while not pygame.sprite.collide_rect(S1, comA):
                            show_explain('player')
                            comA.rect.centerx = comA.rect.centerx - 50
                            screen.blit(comA.image, comA.rect)
                            pygame.display.flip()
                            time.sleep(0.2)
                        del S1, comA
                        show_explain('')
            pygame.event.clear()
pygame.quit()
exit()
