import time
import pygame
import random
import copy

if __name__ == "__main__":
    import os
    os.chdir('..')


def main(next_stage, last_score):
    stage = next_stage
    total_score = last_score

    pygame.init()

    # 게임판 크기 설정
    screen_width = 900
    screen_height = 660
    screen = pygame.display.set_mode((screen_width, screen_height))

    # block 클래스
    class Block(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('./EatGround/block.png')
            self.image = pygame.transform.scale(self.image, (40, 40))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
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
            self.switch_dir = "none"
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

    real_line = []
    temp_line = []
    bfs_check_list = []
    map_coordinate = [[0] * 621 for _ in range(860)]
    for k in range(0, 860, 33):
        map_coordinate[k][0] = 1
        map_coordinate[k][620] = 1
    for k in range(0, 620, 31):
        map_coordinate[0][k] = 1
        map_coordinate[858][k] = 1
    font = pygame.font.SysFont('Tahoma', 25)
    tmp = 0
    direction = "right"
    winning_point = [475 * 0.8, 475 * 0.8, 475 * 0.75, 475 * 0.75, 475 * 0.7, 475 * 0.7, 475 * 0.6]
    enemy = [Enemy(i) for i in range(0, stage)]
    character = Character(0, 0, "in")

    dx = [33, -33, 0, 0]
    dy = [0, 0, 31, -31]
    dex = [33, 33, -33, -33]
    dey = [31, -31, 31, -31]

    def defeat():
        screen.fill((255, 255, 255))
        loser = pygame.image.load('./EatGround/score.png')
        loser = pygame.transform.scale(loser, (640, 650))
        font1 = pygame.font.SysFont('Tahoma', 130)
        score = font1.render(f'{total_score}', True, (0, 0, 0))
        screen.blit(loser, (-50, 60))
        screen.blit(score, (550, 230))
        pygame.display.flip()

    def win():
        screen.fill((255, 255, 255))
        winner = pygame.image.load('./EatGround/clear.png')
        winner = pygame.transform.scale(winner, (640, 650))
        screen.blit(winner, (130, 0))
        pygame.display.flip()

    def bfs(start_node):
        temp_list = [start_node]
        visit = copy.deepcopy(map_coordinate)
        if start_node[0] < 0 or start_node[0] > 860 or start_node[1] < 0 or start_node[1] > 620:
            return
        if visit[start_node[0]][start_node[1]] == 1:
            return
        visit[start_node[0]][start_node[1]] = 1
        queue = [start_node]
        while queue:
            node = queue.pop(0)
            for i in range(0, 4):
                nx = node[0] + dx[i]
                ny = node[1] + dy[i]
                if (33 <= nx < 826) and (31 <= ny < 590):
                    if visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        queue.append((nx, ny))
                        temp_list.append((nx, ny))
        for i in range(0, stage):
            if (enemy[i].rect.x, enemy[i].rect.y) in temp_list:
                return
        for n in temp_list:
            map_coordinate[n[0]][n[1]] = 1
            real_line.append(n)

    # 화면 초기화
    def show_main():
        screen.fill((0, 0, 0))
        block_top = [Block(i, 0) for i in range(0, 860, 33)]
        block_bottom = [Block(i, 620) for i in range(0, 860, 33)]
        block_left = [Block(0, i) for i in range(0, 620, 31)]
        block_right = [Block(858, i) for i in range(0, 620, 31)]
        block_line = [Block(i, j) for i, j in real_line]
        block_temp = [Block(i, j) for i, j in temp_line]
        winning_percent = len(real_line) / winning_point[stage - 1] * 100
        score = font.render(f'stage : {stage} / score : {total_score} / {winning_percent : .1f}%', True, (0, 0, 0))
        screen.blit(score, (40, 0))
        if character.status == "out":
            for i in block_temp:
                for j in range(0, stage):
                    if pygame.sprite.collide_rect(enemy[j], i):
                        defeat()
                        time.sleep(3)
                        pygame.quit()
                        exit()
        else:
            for i, j in bfs_check_list:
                bfs((i, j))
            bfs_check_list.clear()
            temp_line.clear()
        if winning_percent >= 100:
            if stage == 7:
                win()
                time.sleep(3)
                pygame.quit()
                exit()
            else:
                pygame.quit()
                main(stage + 1, total_score + len(real_line))

    # 캐릭터 모션
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
        if map_coordinate[ene.rect.x][ene.rect.y] == 1:
            if stat == 1:
                ene.rect.x = ene.rect.x - 33
            if stat == 2:
                ene.rect.x = ene.rect.x + 33
            if stat == 3:
                ene.rect.y = ene.rect.y - 31
            if stat == 4:
                ene.rect.y = ene.rect.y + 31
        screen.blit(ene.image, ene.rect)

    def char_dir(stat):
        if stat == "right":
            if character.switch_dir == "up" or character.switch_dir == "down":
                for i in range(0, 4):
                    bfs_check_list.append((character.rect.x + dex[i], character.rect.y + dey[i]))
        elif stat == "left":
            if character.switch_dir == "up" or character.switch_dir == "down":
                for i in range(0, 4):
                    bfs_check_list.append((character.rect.x + dex[i], character.rect.y + dey[i]))
        elif stat == "up":
            if character.switch_dir == "right" or character.switch_dir == "left":
                for i in range(0, 4):
                    bfs_check_list.append((character.rect.x + dex[i], character.rect.y + dey[i]))
        elif stat == "down":
            if character.switch_dir == "right" or character.switch_dir == "left":
                for i in range(0, 4):
                    bfs_check_list.append((character.rect.x + dex[i], character.rect.y + dey[i]))

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
                    if not ((character.rect.x, character.rect.y) in real_line):
                        temp_line.append((character.rect.x, character.rect.y))
                        real_line.append((character.rect.x, character.rect.y))
                        map_coordinate[character.rect.x][character.rect.y] = 1
                # 캐릭터 움직임
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                    char_dir(direction)
                    character.switch_dir = direction
                    character.rect.x = character.rect.x + 33
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    char_dir(direction)
                    character.switch_dir = direction
                    character.rect.x = character.rect.x - 33
                if event.key == pygame.K_UP:
                    direction = "up"
                    char_dir(direction)
                    character.switch_dir = direction
                    character.rect.y = character.rect.y - 31
                if event.key == pygame.K_DOWN:
                    direction = "down"
                    char_dir(direction)
                    character.switch_dir = direction
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
                if map_coordinate[character.rect.x][character.rect.y] == 0:
                    if character.status == "in":
                        for i in range(0, 4):
                            bfs_check_list.append((character.rect.x + dex[i], character.rect.y + dey[i]))
                    character.status = "out"
                else:
                    if character.status == "out":
                        for i in range(0, 4):
                            bfs_check_list.append((character.rect.x + dex[i], character.rect.y + dey[i]))
                    character.status = "in"
                pygame.event.clear()
    pygame.quit()
    exit()


main(1, 0)
