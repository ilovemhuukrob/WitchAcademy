import pygame

from pygame import mixer
#========================================================================================================================
pygame.init()
pygame.display.set_caption("W <it> CH Academy")
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font('sprite/photohunt/2005_iannnnnAMD.ttf', 72)
HeartImg = pygame.image.load('sprite/photohunt/heart.png')
background = pygame.image.load('sprite/photohunt/stage 1.png')
bg_sound = pygame.mixer.Sound('sprite/photohunt/main.mp3')
#========================================================================================================================
stage = 0
score_value = 0
health_value = 3
dummy_mind1 = dummy_mind2 = dummy_mind3 = dummy_mind4 = dummy_mind5 = dummy_mind6 = dummy_mind7 = True
#========================================================================================================================
sec = 62 # Timeset <<<<<<<<<<<
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
                if ((155 < mx < 195 and 150 < my < 239) or (740 < mx < 780 and 150 < my < 239)) and dummy_mind1 == True:  # เทียน
                    score_value += 1
                    dummy_mind1 = False
                elif ((590 < mx < 634 and 92 < my < 202) or (1183 < mx < 1217 and 92 < my < 202)) and dummy_mind2 == True:  # หนังสือ
                    score_value += 1
                    dummy_mind2 = False
                elif ((265 < mx < 310 and 280 < my < 360) or (840 < mx < 885 and 280 < my < 360)) and dummy_mind3 == True:  # อะไรไม่รุข้างหน้าต่าง
                    score_value += 1
                    dummy_mind3 = False
                elif ((575 < mx < 638 and 312 < my < 373) or (1165 < mx < 1221 and 312 < my < 373)) and dummy_mind4 == True:  # หนังสือชั้น 3
                    score_value += 1
                    dummy_mind4 = False
                elif ((130 < mx < 173 and 492 < my < 527) or (700 < mx < 760 and 492 < my < 527)) and dummy_mind5 == True:  # ไม้ไรสักอย่าง
                    score_value += 1
                    dummy_mind5 = False
                elif ((360 < mx < 436 and 470 < my < 528) or (942 < mx < 1022 and 470 < my < 528)) and dummy_mind6 == True:  # ถ้วย
                    score_value += 1
                    dummy_mind6 = False
                elif ((60 < mx < 134 and 650 < my < 703) or (649 < mx < 727 and 671 < my < 703)) and dummy_mind7 == True:  # ไห้ไรสักอย่าง
                    score_value += 1
                    dummy_mind7 = False
                # wrong click
                if not((155 < mx < 195 and 150 < my < 239) or (740 < mx < 780 and 150 < my < 239)) and \
                    not((590 < mx < 634 and 92 < my < 202) or (1183 < mx < 1217 and 92 < my < 202)) and \
                    not((265 < mx < 310 and 280 < my < 360) or (840 < mx < 885 and 280 < my < 360)) and \
                    not((575 < mx < 638 and 312 < my < 373) or (1165 < mx < 1221 and 312 < my < 373)) and \
                    not((130 < mx < 173 and 492 < my < 527) or (700 < mx < 760 and 492 < my < 527)) and \
                    not((360 < mx < 436 and 470 < my < 528) or (942 < mx < 1022 and 470 < my < 528)) and \
                    not((60 < mx < 134 and 650 < my < 703) or (649 < mx < 727 and 671 < my < 703)):
                    if health_value > 0:
                        health_value -= 1
    if dummy_mind1 == False:
        drawcorrect(125, 157)
        drawcorrect(712, 157)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (125, 157))
            background.blit(correctImg[16], (712, 157))
            dummy_mind1 = True
    if dummy_mind2 == False:
        drawcorrect(550, 100)
        drawcorrect(1140, 100)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (550, 100))
            background.blit(correctImg[16], (1140, 100))
            dummy_mind2 = True
    if dummy_mind3 == False:
        drawcorrect(237, 290)
        drawcorrect(811, 290)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (237, 290))
            background.blit(correctImg[16], (811, 290))
            dummy_mind3 = True
    if dummy_mind4 == False:
        drawcorrect(550, 300)
        drawcorrect(1140, 300)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (550, 300))
            background.blit(correctImg[16], (1140, 300))
            dummy_mind4 = True
    if dummy_mind5 == False:
        drawcorrect(95, 470)
        drawcorrect(688, 470)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (95, 470))
            background.blit(correctImg[16], (688, 470))
            dummy_mind5 = True
    if dummy_mind6 == False:
        drawcorrect(348, 440)
        drawcorrect(937, 440)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (348, 440))
            background.blit(correctImg[16], (937, 440))
            dummy_mind6 = True
    if dummy_mind7 == False:
        drawcorrect(640, 645)
        drawcorrect(52, 645)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (640, 645))
            background.blit(correctImg[16], (52, 645))
            dummy_mind7 = True
    if health_value == 3:
        screen.blit(HeartImg, (1050, 0))
        screen.blit(HeartImg, (1115, 0))
        screen.blit(HeartImg, (1180, 0))
    if health_value == 2:
        screen.blit(HeartImg, (1115, 0))
        screen.blit(HeartImg, (1180, 0))
    if health_value == 1:
        screen.blit(HeartImg, (1180, 0))
    score = font.render('Total Left '+str(score_value) + '/7', True, (255, 255, 255))
    screen.blit(score, (35, 10))
    sec_show = font.render('Time Left: ' + str(int(sec)), True, (255, 255, 255))
    screen.blit(sec_show, (525, 10))
    if sec > 61:
        rules = pygame.image.load('data/pic/RULES.png')
        screen.blit(rules,(0,0))
    if score_value == 7:
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