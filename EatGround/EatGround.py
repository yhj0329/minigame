import pygame
import random

if __name__ == "__main__":
    import os
    os.chdir('..')

pygame.init()

# 게임판 크기 설정
screen_width = 900
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))


# block 클래스
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, inout):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./EatGround/block.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.inout = inout
        screen.blit(self.image, self.rect)


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, check):
        pygame.sprite.Sprite.__init__(self)
        self.image_right = [pygame.image.load('./EatGround/character1.png'),
                            pygame.image.load('./EatGround/character2.png')]
        self.image_right = [pygame.transform.scale(self.image_right[i], (40, 40)) for i in range(0, 2)]
        self.image_left = [pygame.transform.flip(self.image_right[i], True, False) for i in range(0, 2)]
        self.image_up = [pygame.transform.rotate(self.image_right[i], 90) for i in range(0, 2)]
        self.image_down = [pygame.transform.rotate(self.image_right[i], 270) for i in range(0, 2)]
        self.rect = self.image_right[0].get_rect()
        self.rect.topleft = (x, y)
        self.status = check
        screen.blit(self.image_right[0], self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, num):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = [pygame.image.load('./EatGround/e1.png'), pygame.image.load('./EatGround/e2.png'),
                           pygame.image.load('./EatGround/e3.png'), pygame.image.load('./EatGround/e4.png'),
                           pygame.image.load('./EatGround/e5.png'), pygame.image.load('./EatGround/e6.png'),
                           pygame.image.load('./EatGround/e7.png')]
        self.image_list = [pygame.transform.scale(self.image_list[i], (40, 38)) for i in range(0, 7)]
        self.image = self.image_list[num]
        self.rect = self.image.get_rect()
        self.rect.topleft = random.choice([(i, j) for i in range(33, 826, 33) for j in range(31, 590, 31)])
        screen.blit(self.image, self.rect)


tmp_coordinate = []
real_line = []
map_coordinate = [[0] * 621 for _ in range(860)] # [(i, j) for i in range(33, 826, 33) for j in range(31, 590, 31)]
for k in range(0, 860, 33):
    map_coordinate[k][0] = 1
    map_coordinate[k][620] = 1
for k in range(0, 620, 31):
    map_coordinate[0][k] = 1
    map_coordinate[858][k] = 1
score = 0
tmp = 0
direction = "right"
stage = 1
enemy = [Enemy(i) for i in range(0, stage)]
character = Character(0, 0, "in")

dx = [33, -33, 0, 0]
dy = [0, 0, 31, -31]
dex = [33, 33, -33, -33]
dey = [31, -31, 31, -31]


def bfs(start_node):
    temp_list = []
    visit = map_coordinate.copy()
    if start_node[0] < 0 or start_node[0] > 860 or start_node[1] < 0 or start_node[1] > 620:
        return []
    visit[start_node[0]][start_node[1]] = 1
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if visit[node[0]][node[1]] == 1:
            continue
        for i in range(0, 4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if (33 <= nx < 826) and (31 <= ny < 590):
                for j in range(0, stage):
                    if (nx, ny) == (enemy[j].rect.x, enemy[j].rect.y):
                        return []
                if visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
                    temp_list.append((nx, ny))
    return temp_list


# 화면 초기화
def show_main(): # tmp_c에서 0 1로 구분한다.
    screen.fill((0, 0, 0))
    block_top = [Block(i, 0, "in") for i in range(0, 860, 33)]
    block_bottom = [Block(i, 620, "in") for i in range(0, 860, 33)]
    block_left = [Block(0, i, "in") for i in range(0, 620, 31)]
    block_right = [Block(858, i, "in") for i in range(0, 620, 31)]
    block_line = [Block(i, j, "in") for i, j in real_line]
    block_tmp = [Block(i, j, "out") for i, j in tmp_coordinate]
    if character.status == "out":
        for i in block_tmp:
            for j in range(0, stage):
                if pygame.sprite.collide_rect(enemy[j], i):
                    pygame.quit()
                    exit()
    else:
        for i, j in tmp_coordinate:
            real_line.append((i, j))
            map_coordinate[i][j] = 1
        for m in range(0, 4):
            for n in bfs((character.rect.x + dex[m], character.rect.y + dey[m])):
                real_line.append(n)
        tmp_coordinate.clear()




# 캐릭터 애니메
def char_motion(stat):
    if stat == "right":
        screen.blit(character.image_right[tmp % 2], character.rect)
    elif stat == "left":
        screen.blit(character.image_left[tmp % 2], character.rect)
    elif stat == "up":
        screen.blit(character.image_up[tmp % 2], character.rect)
    elif stat == "down":
        screen.blit(character.image_down[tmp % 2], character.rect)


# 적 움직임
def enemy_move(ene, stat):
    if stat == 1:
        ene.rect.x = ene.rect.x + 33
    if stat == 2:
        ene.rect.x = ene.rect.x - 33
    if stat == 3:
        ene.rect.y = ene.rect.y + 31
    if stat == 4:
        ene.rect.y = ene.rect.y - 31
    if ene.rect.left < 33:
        ene.rect.left = 33
    if ene.rect.right > 825:
        ene.rect.right = 825
    if ene.rect.top < 31:
        ene.rect.top = 31
    if ene.rect.bottom > 589:
        ene.rect.bottom = 589
    screen.blit(ene.image, ene.rect)


# 루프 시작
running = True
while running:
    if tmp != 0:
        tmp = 0
    else:
        tmp = 1
    show_main()
    char_motion(direction)
    for i in range(0, stage):
        enemy_move(enemy[i], random.randint(1, 4))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if 32 < character.rect.x < 826 and 30 < character.rect.y < 590:
                if not ((character.rect.x, character.rect.y) in tmp_coordinate):
                    tmp_coordinate.append((character.rect.x, character.rect.y))
            # 캐릭터 움직임
            if event.key == pygame.K_RIGHT:
                direction = "right"
                character.rect.x = character.rect.x + 33
            if event.key == pygame.K_LEFT:
                direction = "left"
                character.rect.x = character.rect.x - 33
            if event.key == pygame.K_UP:
                direction = "up"
                character.rect.y = character.rect.y - 31
            if event.key == pygame.K_DOWN:
                direction = "down"
                character.rect.y = character.rect.y + 31
            if character.rect.left < 0:
                character.rect.left = 0
            if character.rect.right > screen.get_width():
                character.rect.right = screen.get_width() - 2
            if character.rect.top < 0:
                character.rect.top = 0
            if character.rect.bottom > screen.get_height():
                character.rect.bottom = screen.get_height()
                # 캐릭터 지나간 자리에 블럭 놓기
            if 32 < character.rect.x < 826 and 30 < character.rect.y < 590:
                character.status = "out"
            else:
                character.status = "in"
            pygame.event.clear()

pygame.quit()
exit()
