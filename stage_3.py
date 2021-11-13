import pygame

from pygame import mixer
#========================================================================================================================
pygame.init()
pygame.display.set_caption("W <it> CH Academy")
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font('sprite/photohunt/2005_iannnnnAMD.ttf', 72)
HeartImg = pygame.image.load('sprite/photohunt/heart.png')
background = pygame.image.load('sprite/photohunt/stage 2.png')
bg_sound = pygame.mixer.Sound('data/sounds/main.mp3')
#========================================================================================================================
stage = 0
score_value = 0
health_value = 3
dummy_fluke1 = dummy_fluke2 = dummy_fluke3 = dummy_fluke4 = dummy_fluke5 = dummy_fluke6 = dummy_fluke7 = dummy_fluke8 = True
#========================================================================================================================
sec = 60 # Timeset <<<<<<<<<<<
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
    # bg_sound.play(-1)
    sec -= 0.07
    if sec < 61:
        stage = 1
        screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if stage == 1:
            # screen.blit(background, (0, 0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                print(health_value)
                if ((545 < mx < 610 and 459 < my < 489) or (1162 < mx < 1225 and 454 < my < 492)) and dummy_fluke1 == True: # แก้ววายด้านขวา
                    score_value += 1
                    dummy_fluke1 = False
                elif ((251 < mx < 281 and 495 < my < 525) or (878 < mx < 915 and 493 < my < 528)) and dummy_fluke2 == True: # สามเหลี่ยม
                    score_value += 1
                    dummy_fluke2 = False
                elif ((555 < mx < 587 and 653 < my < 686) or (1175 < mx < 1210 and 653 < my < 686)) and dummy_fluke3 == True: #ไวโอลิน
                    score_value += 1
                    dummy_fluke3 = False
                elif ((85 < mx < 133 and 521 < my < 562) or (709 < mx < 757 and 523 < my < 560)) and dummy_fluke4 == True: # กระเป๋า
                    score_value += 1
                    dummy_fluke4 = False
                elif ((129 < mx < 170 and 430 < my < 468) or (759 < mx < 793 and 433 < my < 468)) and dummy_fluke5 == True: #ลิ้นชัก
                    score_value += 1
                    dummy_fluke5 = False
                elif ((406 < mx < 486 and 326 < my < 373) or (1037 < mx < 1104 and 326 < my < 376)) and dummy_fluke6 == True: #กระดาษไรไม่รุ
                    score_value += 1
                    dummy_fluke6 = False
                elif ((231 < mx < 277 and 221 < my < 256) or (853 < mx < 911 and 223 < my < 259)) and dummy_fluke7 == True: #ผลไม้?
                    score_value += 1
                    dummy_fluke7 = False
                elif ((355 < mx < 395 and 440 < my < 510) or (970 < mx < 1010 and 440 < my < 510)) and dummy_fluke8 == True:
                    score_value += 1
                    dummy_fluke8 = False
                #wrong click
                if not((545 < mx < 610 and 459 < my < 489) or (1162 < mx < 1225 and 454 < my < 492)) and\
                    not((251 < mx < 281 and 495 < my < 525) or (878 < mx < 915 and 493 < my < 528)) and\
                        not((555 < mx < 587 and 653 < my < 686) or (1175 < mx < 1210 and 653 < my < 686)) and\
                            not((85 < mx < 133 and 521 < my < 562) or (709 < mx < 757 and 523 < my < 560)) and\
                                not((129 < mx < 170 and 430 < my < 468) or (759 < mx < 793 and 433 < my < 468)) and\
                                    not((406 < mx < 486 and 326 < my < 373) or (1037 < mx < 1104 and 326 < my < 376)) and\
                                        not((231 < mx < 277 and 221 < my < 256) or (853 < mx < 911 and 223 < my < 259)) and\
                                            not((355 < mx < 395 and 440 < my < 510) or (970 < mx < 1010 and 440 < my < 510)):
                # else:
                    if health_value > 0:
                        health_value -= 1
    if dummy_fluke1 == False: # แก้ววายด้านขวา
        drawcorrect(536, 425)
        drawcorrect(1158, 425)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (536, 425))
            background.blit(correctImg[16], (1158, 425))
            dummy_fluke1 = True
    if dummy_fluke2 == False: # สามเหลี่ยม
        drawcorrect(226, 461)
        drawcorrect(845, 461)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (226, 461))
            background.blit(correctImg[16], (845, 461))
            dummy_fluke2 = True
    if dummy_fluke3 == False: #ไวโอลีน
        drawcorrect(519, 614)
        drawcorrect(1146, 614)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (519, 614))
            background.blit(correctImg[16], (1146, 614))
            dummy_fluke3 = True
    if dummy_fluke4 == False: #กระเป๋า
        drawcorrect(68, 491)
        drawcorrect(685, 491)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (68, 491))
            background.blit(correctImg[16], (685, 491))
            dummy_fluke4 = True
    if dummy_fluke5 == False: #ลิ้นชัก
        drawcorrect(112, 399)
        drawcorrect(730, 399)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (112, 399))
            background.blit(correctImg[16], (730, 399))
            dummy_fluke5 = True
    if dummy_fluke6 == False: #ม้วนกระดาศ
        drawcorrect(402, 300)
        drawcorrect(1021, 300)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (402, 300))
            background.blit(correctImg[16], (1021, 300))
            dummy_fluke6 = True
    if dummy_fluke7 == False: # ผลไม้?
        drawcorrect(216, 195)
        drawcorrect(835, 195)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (216, 195))
            background.blit(correctImg[16], (835, 195))
            dummy_fluke7 = True
    if dummy_fluke8 == False:
        drawcorrect(945, 420)
        drawcorrect(328, 420)
        if WALKCOUNT > 16:
            WALKCOUNT = 0
            background.blit(correctImg[16], (945, 420))
            background.blit(correctImg[16], (328, 420))
            dummy_fluke8 = True
    if health_value == 3:
        screen.blit(HeartImg, (1050, 0))
        screen.blit(HeartImg, (1115, 0))
        screen.blit(HeartImg, (1180, 0))
    if health_value == 2:
        screen.blit(HeartImg, (1115, 0))
        screen.blit(HeartImg, (1180, 0))
    if health_value == 1:
        screen.blit(HeartImg, (1180, 0))
    score = font.render('Total Left '+str(score_value) + '/8', True, (255, 255, 255))
    screen.blit(score, (35, 10))
    sec_show = font.render('Time Left: ' + str(int(sec)), True, (255, 255, 255))
    screen.blit(sec_show, (525, 10))
    if sec > 61:
        rules = pygame.image.load('data/pic/RULES.png')
        screen.blit(rules,(0,0))
    if score_value == 8:
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
