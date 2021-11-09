import pygame

from pygame import mixer
#========================================================================================================================
pygame.init()
pygame.display.set_caption("W <it> CH Academy")
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font('sprite/photohunt/2005_iannnnnAMD.ttf', 72)
HeartImg = pygame.image.load('sprite/photohunt/heart.png')
WALKCOUNT = 0

def readvar(file, string):
    """readline variable"""
    f, mylist = open(file, 'r'), []
    while True:
        s = f.readline()
        if s == '':
            break
        d = s.split()
        if d[0].count(string) == 1:
            mylist.append(pygame.image.load(d[0]))
    return mylist

correctImg = readvar('photohunt.txt', 'circle')

def drawcorrect(posx, posy):
    global WALKCOUNT
    if WALKCOUNT > len(correctImg)-1:
        screen.blit(correctImg[len(correctImg)-1], (posx, posy))
    else:
        screen.blit(correctImg[WALKCOUNT], (posx, posy))
    WALKCOUNT += 1

background = pygame.image.load('data/pic/stage 3.png')
bg_sound = pygame.mixer.Sound('data/sounds/main.mp3')
#========================================================================================================================
stage = 0
score_value = 0
health_value = 3
dummy_fluke1 = dummy_fluke2 = dummy_fluke3 = dummy_fluke4 = dummy_fluke5 = dummy_fluke6 = True
#========================================================================================================================
sec = 60 # Timeset <<<<<<<<<<<
while True:
    pygame.time.delay(30)
    bg_sound.play(-1)
    sec -= 0.07
    if sec < 61:
        stage = 1
        screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if stage == 1:
            # screen.blit(background, (0, 0))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                print(health_value)
                if ((578 < mx < 617 and 242 < my < 282) or (1182 < mx < 1217 and 242 < my < 282)) and dummy_fluke1 == True: # หมีบน
                    score_value += 1
                    dummy_fluke1 = False
                elif ((513 < mx < 570 and 324 < my < 381) or (1104 < mx < 1167 and 324 < my < 381)) and dummy_fluke2 == True: # เก้าอี้
                    score_value += 1
                    dummy_fluke2 = False
                elif ((216 < mx < 251 and 549 < my < 582) or (811 < mx < 841 and 549 < my < 582)) and dummy_fluke3 == True: # ไข่มุก
                    score_value += 1
                    WALKCOUNT = 0
                    dummy_fluke3 = False
                elif ((156 < mx < 191 and 237 < my < 302) or (748 < mx < 791 and 237 < my < 302)) and dummy_fluke4 == True: # แก้วบนชั้นวาง ชั้น 2
                    score_value += 1
                    dummy_fluke4 = False
                elif ((259 < mx < 289 and 394 < my < 434) or (849 < mx < 892 and 394 < my < 434)) and dummy_fluke5 == True: # หมีล่าง
                    score_value += 1
                    dummy_fluke5 = False
                elif ((111 < mx < 142 and 185 < my < 229) or (700 < mx < 736 and 185 < my < 229)) and dummy_fluke6 == True: #ขวดแก้วชั้นบน
                    score_value += 1
                    dummy_fluke6 = False
                #wrong click
                if not((578 < mx < 617 and 242 < my < 282) or (1182 < mx < 1217 and 242 < my < 282)) and\
                    not((513 < mx < 570 and 324 < my < 381) or (1104 < mx < 1167 and 324 < my < 381)) and\
                        not((216 < mx < 251 and 549 < my < 582) or (811 < mx < 841 and 549 < my < 582)) and\
                            not((156 < mx < 191 and 237 < my < 302) or (748 < mx < 791 and 237 < my < 302)) and\
                                not((259 < mx < 289 and 394 < my < 434) or (849 < mx < 892 and 394 < my < 434)) and\
                                    not((111 < mx < 142 and 185 < my < 229) or (700 < mx < 736 and 185 < my < 229)):
                # else:
                    if health_value > 0:
                        health_value -= 1

    if dummy_fluke1 == False: # หมีบน
        drawcorrect(551, 213)
        drawcorrect(1150, 213)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (551, 213))
            background.blit(correctImg[16], (1150, 213))
            dummy_fluke1 = True
    if dummy_fluke2 == False: # เก้าอี้
        drawcorrect(486, 297)
        drawcorrect(1086, 297)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (486, 297))
            background.blit(correctImg[16], (1086, 297))
            dummy_fluke2 = True
    if dummy_fluke3 == False: # ไข่มุก
        drawcorrect(180, 515)
        drawcorrect(776, 515)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (180, 515))
            background.blit(correctImg[16], (776, 515))
            dummy_fluke3 = True
    if dummy_fluke4 == False: # แก้วบนชั้นวาง ชั้น 2
        drawcorrect(127, 214)
        drawcorrect(727, 214)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (127, 214))
            background.blit(correctImg[16], (727, 214))
            dummy_fluke4 = True
    if dummy_fluke5 == False: # หมีล่าง
        drawcorrect(223, 365)
        drawcorrect(812, 365)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (223, 365))
            background.blit(correctImg[16], (812, 365))
            dummy_fluke5 = True
    if dummy_fluke6 == False: #ขวดแก้วชั้นบน
        drawcorrect(70, 155)
        drawcorrect(670, 155)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (70, 155))
            background.blit(correctImg[16], (670, 155))
            dummy_fluke6 = True
    if health_value == 3:
        screen.blit(HeartImg, (1050, 0))
        screen.blit(HeartImg, (1115, 0))
        screen.blit(HeartImg, (1180, 0))
    if health_value == 2:
        screen.blit(HeartImg, (1115, 0))
        screen.blit(HeartImg, (1180, 0))
    if health_value == 1:
        screen.blit(HeartImg, (1180, 0))
    score = font.render('Total Left '+str(score_value) + '/6', True, (255, 255, 255))
    screen.blit(score, (35, 10))
    sec_show = font.render('Time Left: ' + str(int(sec)), True, (255, 255, 255))
    screen.blit(sec_show, (525, 10))
    if sec > 61:
        rules = pygame.image.load('data/pic/RULES.png')
        screen.blit(rules,(0,0))
    if score_value == 6:
        win_screen = pygame.image.load('data/pic/U WIN.png')
        screen.blit(win_screen, (0,0))
        bg_sound.stop()
    elif health_value == 0:
        lose_screen = pygame.image.load('data/pic/U lose.png')
        screen.blit(lose_screen, (0,0))
        bg_sound.stop()
    elif sec <= 0:
        lose_screen = pygame.image.load('data/pic/U lose.png')
        screen.blit(lose_screen, (0,0))
        bg_sound.stop()
    pygame.display.update()