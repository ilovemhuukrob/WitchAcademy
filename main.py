import pygame, json
from pygame import mixer

pygame.init()

#---------------------------------------------------------------------------
"""set variable"""
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("W <it> CH AcademY")
bg = pygame.image.load("sprite/entryhall.jpg")
bgfront = pygame.image.load("sprite/front.jpg").convert()
BG_SCROLLING, ANIM = 0, 0
bg_width, bg_height = bg.get_rect().size
#icon = pygame.image.load("sprite/icongame.png")
#pygame.display.set_icon(icon)
PLAYER_RADIUS = 13
PLAYER_POSITION_X = 508
PLAYER_POSITION_Y = 598

start_scrolling_x = (width/2)
stage_wildth = 1280
stage_position_x = 0

start_scrolling_y = height/2
stage_height = 720
stage_position_y = 0

X, Y, vel, WALK_AVI, CHECK = 508, 598, 15, 0, 'UP'

run = True
PLAY_FRONT, PLAY_MAIN, PLAY_PH1, PLAY_PH2, PLAY_PH3 = True, False, False, False, False
LEFT, RIGHT = False, False
DOWN, UP = False, False

gohallway = False
gopath = False
gomeeting = False
gofirstaid = False
gobattle = False
gocanteen = False
goclass_1 = False
goclass_2 = False
goclass_3 = False
gowestgar = False
goeastgar = False
goentry = True
gohalls = False

gowestcor_1 = False
gowestcor_2 = False
goeastcor_1 = False
goeastcor_2 = False

classroom1 = False
classroom2 = False
classroom3 = False

goresearch = False
goteach = False
goapothe = False
gowestfor = False
goeastfor = False
goforest = False


#----------------Sound--------------------------------
bg_hall = pygame.mixer.Sound("sound/178.mp3"); bg_hall.set_volume(0.5)
bg_opendoor = pygame.mixer.Sound("sound\Wood Door - Open_Close.mp3")

#--------------------------------------------
walls = open("walls.txt", 'r').read()
walls = dict(json.loads(walls))
POSX_SHE, POSX_ESME, POSX_AVI, BLACK = 300, -150, -300, 0
logo = pygame.image.load('sprite/logo.png')
press = pygame.image.load('sprite/press.png')

#---------------------------------------------------------------------------
def readvar(file, string):
    """readline variable"""
    f, mylist = open(file, 'r', encoding="utf8"), []
    while True:
        s = f.readline()
        if s == '':
            break
        d = s.split()
        if file == 'dialog.txt':
            mylist.append(s.strip('\n'))
        elif d[0].count(string) == 1:
            mylist.append(pygame.image.load(d[0]))
    return mylist

avilia_walkr, avilia_walkl = readvar('var.txt', 'avilia/walkr'), readvar('var.txt', 'avilia/walkl')
avilia_walkd, avilia_walku = readvar('var.txt', 'avilia/walkd'), readvar('var.txt', 'avilia/walku')
esme_walkr, esme_walkl = readvar('var.txt', 'esme/walkr'), readvar('var.txt', 'esme/walkl')
she_walkr, she_walkl = readvar('var.txt', 'sheree/walkr'), readvar('var.txt', 'sheree/walkl')
she_push = readvar('var.txt', 'sheree/push')
esme_fail = readvar('var.txt', 'esme/fail')
sheree_b = readvar('front.txt', 'sheree')
esme_b = readvar('front.txt', 'esme/broom')
avilia_b = readvar('front.txt', 'avilia/broom')
FRONTANIM = False

book_img = readvar('front.txt', 'map')
book_anim = 0
open_book = False
nextpage = False
backpage = False
closebook = False
book_map = True
book_inven = False
book_menu = False

#---------------------------------------------------------------------------
def frontgame():
    """front game"""
    global BG_SCROLLING
    global BLACK
    global ANIM
    global POSX_SHE
    global POSX_AVI
    global POSX_ESME
    global PLAY_MAIN
    global PLAY_FRONT
    global FRONTANIM
    pygame.time.delay(30)
    BG_SCROLLING -= 1
    win.blit(bgfront, (BG_SCROLLING, 0))
    win.blit(bgfront, (BG_SCROLLING+1280, 0))
    
    pygame.draw.rect(win, (0), [0, 0, 1280, BLACK])
    pygame.draw.rect(win, (0), [0, 722-BLACK, 1280, 100])

    win.blit(logo, ((603/2), 80))
    if ANIM + 1 >= 42:ANIM = 0
    if ANIM <= 22 and FRONTANIM == False:
        win.blit(press, ((1280/2)-(203/2), 500))
    win.blit(sheree_b[ANIM], (POSX_SHE, 400))
    win.blit(avilia_b[ANIM], (POSX_AVI, 390))
    win.blit(esme_b[ANIM], (POSX_ESME, 420))
    if BLACK < 100:BLACK += 2.25
    if POSX_SHE < 750:POSX_SHE += 10
    if POSX_AVI < 160:POSX_AVI += 10
    if POSX_ESME < 300:POSX_ESME += 10
    if BG_SCROLLING <= -1280:BG_SCROLLING = 0
    if FRONTANIM:
        if POSX_SHE < 1280:POSX_SHE += 20
        if POSX_ESME < 1280:POSX_ESME += 20
        if POSX_AVI < 1280:POSX_AVI += 20
        if POSX_AVI == 1280:
            fadeout()
            fadein()
            FRONTANIM = False
            PLAY_MAIN = True
            PLAY_FRONT = False
            BLACK, ANIM = 0, 0
    elif keys[pygame.K_SPACE] and BLACK == 101.25:
        FRONTANIM = True
    ANIM += 1
#---------------------------------------------------------------------------
def redrawGameWindow():
    """blit the main character"""
    global WALK_AVI

    if WALK_AVI + 1 >= 9: #กัน out of range
        WALK_AVI = 0
    if RIGHT:
        win.blit(avilia_walkr[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALK_AVI += 1
    elif LEFT:
        win.blit(avilia_walkl[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALK_AVI += 1
    elif DOWN:
        win.blit(avilia_walkd[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALK_AVI += 1
    elif UP:
        win.blit(avilia_walku[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALK_AVI += 1
    elif RIGHT == False and LEFT == False and DOWN == False and UP == False:
        if CHECK == 'RIGHT':
            win.blit(avilia_walkr[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'LEFT':
            win.blit(avilia_walkl[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'DOWN':
            win.blit(avilia_walkd[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'UP':
            win.blit(avilia_walku[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
#---------------------------------------------------------------------------
def fadeout():
    """ fade out screen """
    fade = pygame.Surface((1280, 720))
    fade.fill((0,0,0))
    for alpha in range(0, 150):
        fade.set_alpha(alpha)
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
#---------------------------------------------------------------------------
def fadein():
    """ fade in screen """
    fade = pygame.Surface((1280, 720))
    fade.fill((0,0,0))
    for alpha in range(150, 0, -1):
        fade.set_alpha(alpha)
        win.blit(bg, (-508, -272))
        redrawGameWindow()
        win.blit(fade, (0,0))
        pygame.display.update()
#---------------------------------------------------------------------------
dialogbox = readvar('var.txt', 'dialogbox')
nabox = readvar('var.txt', 'nabox')
lstdialog = readvar('dialog.txt', '')
apple = pygame.image.load('sprite/apple.png')
dia_she = pygame.image.load('sprite/sheree/sheree.png')
dia_esme = pygame.image.load('sprite/esme/esme.png')
dia_avi = pygame.image.load('sprite/avilia/avilia.png')
font = pygame.font.Font('sprite/alagard.ttf', 21)
bubble = readvar('var.txt', 'bubble')
sad = readvar('var.txt', 'sad')
sad = bubble+sad
ANIMB = 0

play_dialog = False
nextdia = False
posx_txt = 200
posy_txt = 80
counttxt = 0
countd = 0
CHECKB = False

play_cutscene = False
STORY1 = True

WALK_ESME, WALK_SHE = 0, 0

def redrawdialog(countd):
    """ blit dialog """
    global ANIM, counttxt
    global posx_txt, posy_txt
    if ANIM >= 10:
        ANIM = 9
    win.blit(dialogbox[ANIM], ((1280/2)-(dialogbox[ANIM].get_rect().size[0]/2), 450))
    if ANIM == 9:
        if lstdialog[countd].split()[0] == 'Sheree':
            win.blit(dia_she, (141.5, 450))
        if lstdialog[countd].split()[0] == 'Esme':
            win.blit(dia_esme, (141.5, 450))
        if lstdialog[countd].split()[0] == 'Avilia':
            win.blit(dia_avi, (141.5, 450))
        if counttxt <= len(lstdialog[countd].split(':')[1])-1:
            message = font.render(lstdialog[countd].split(':')[1][counttxt], True, (0, 0, 0))
            dialogbox[9].blit(message, (posx_txt, posy_txt))
            posx_txt += message.get_rect().size[0]+0.5
        if posx_txt >= 950:
            posx_txt, posy_txt = 202, 120
        counttxt += 1
    ANIM += 1

def shepush():
    global WALK_SHE, POSX_SHE, POSY_SHE
    if WALK_SHE+1 >= 12:
        WALK_SHE = 11
    win.blit(she_push[WALK_SHE], (POSX_SHE, POSY_SHE))
    WALK_SHE += 1

def esmefail(way):
    global WALK_ESME, POSX_ESME, POSY_ESME
    win.blit(esme_fail[WALK_ESME], (POSX_ESME, POSY_ESME))
    if way == 'down':
        WALK_ESME += 1
        if WALK_ESME > 9:
            WALK_ESME = 9
    if way == 'up':
        WALK_ESME -= 1
        if WALK_ESME < 0:
            WALK_ESME = 0

def aviwalkl(stop):
    global WALK_AVI, POSX_AVI, POSY_AVI
    if WALK_AVI+1 >= 9:
        WALK_AVI = 0
    if POSX_AVI != stop:
        POSX_AVI -= 5
        WALK_AVI += 1
    win.blit(avilia_walkl[WALK_AVI], (POSX_AVI, POSY_AVI))

def shewalkr(stop):
    global WALK_SHE, POSX_SHE, POSY_SHE
    if WALK_SHE+1 >= 9:
        WALK_SHE = 0
    if POSX_SHE != stop:
        POSX_SHE += 5
        WALK_SHE += 1
    win.blit(she_walkr[WALK_SHE], (POSX_SHE, POSY_SHE))

def shewalkl(stop):
    global WALK_SHE, POSX_SHE, POSY_SHE
    if WALK_SHE+1 >= 9:
        WALK_SHE = 0
    if POSX_SHE != stop:
        POSX_SHE -= 5
        WALK_SHE += 1
    win.blit(she_walkl[WALK_SHE], (POSX_SHE, POSY_SHE))

def esmewalkr(stop):
    global WALK_ESME, POSX_ESME, POSY_ESME
    if WALK_ESME+1 >= 9:
        WALK_ESME = 0
    if POSX_ESME != stop:
        POSX_ESME += 5
        WALK_ESME += 1
    win.blit(esme_walkr[WALK_ESME], (POSX_ESME, POSY_ESME))

def esmewalkl(stop):
    global WALK_ESME, POSX_ESME, POSY_ESME
    if WALK_ESME+1 >= 9:
        WALK_ESME = 0
    if POSX_ESME != stop:
        POSX_ESME -= 5
        WALK_ESME += 1
    win.blit(esme_walkl[WALK_ESME], (POSX_ESME, POSY_ESME))

def shebroom(way, stop):
    global WALK_SHE, POSX_SHE, POSY_SHE
    if WALK_SHE+1 >= 17:
        WALK_SHE = 0
    she_copy = sheree_b[WALK_SHE].copy()
    she_copy = pygame.transform.scale(she_copy, (130, 130))
    if way == 'left':
        win.blit(pygame.transform.flip(she_copy, True, False), (POSX_SHE-50, POSY_SHE))
        if POSX_SHE != stop:
            POSX_SHE -= 10
    WALK_SHE += 1

def redrawbubble(emo, posx, posy):
    """ blit bubble emo """
    global ANIMB, CHECKB
    if CHECKB:
        if emo == 'sad':
            win.blit(sad[ANIMB], (posx, posy))
        if ANIMB >= 11:
            ANIMB = 0
            CHECKB = False
        ANIMB += 1

def cutscene():
    """ blit cutscene """
    global STORY1, play_dialog, play_cutscene
    global BLACK, ANIM, ANIMB, CHECKB
    global countd, counttxt, posx_txt, posy_txt, nextdia
    global POSX_ESME, POSY_ESME, WALK_ESME
    global POSX_SHE, POSY_SHE, WALK_SHE
    pygame.draw.rect(win, (0), [0, 0, 1280, BLACK])
    pygame.draw.rect(win, (0), [0, 722-BLACK, 1280, 100])
    if BLACK < 100:
        BLACK += 4
    if play_dialog:
        redrawdialog(countd)
    if STORY1:
        if lstdialog[countd].split()[0] == 'End':
            play_dialog, play_cutscene, STORY1 = False, False, False
        if countd in [0, 1, 2, 3, 4, 5, 6]:
            aviwalkl(1150)
        if countd in [0, 1]:
            esmewalkr(750)
            shewalkr(600)
            if POSX_ESME == 750:
                play_dialog = True
        if countd in [2]:
            esmewalkl(750)
            shewalkr(600)
        if countd in [3]:
            if counttxt in range(41, 53):
                CHECKB = True
                redrawbubble('sad', POSX_ESME+2, POSY_ESME-40)
                if not CHECKB:
                    ANIMB = 0
            if POSX_SHE == 680:
                shepush()
                if counttxt >= 80:
                    posx_apple, posy_apple = POSX_ESME-25, POSY_ESME+60
                    win.blit(apple, (posx_apple, posy_apple))
                    esmefail('down')
                else:
                    esmewalkl(750)
            elif counttxt >= 59:
                esmewalkl(750)
                shewalkr(680)
            else:
                esmewalkl(750)
                shewalkr(600)
        if countd in [4, 5, 6, 7, 8, 9, 10]:
            if counttxt in range(0, 20) and countd in [4]:
                win.blit(apple, (POSX_ESME-25-(counttxt*2), POSY_ESME+60-counttxt))
            shewalkr(680)
            esmefail('down')
        if countd in range(7, 70):
            aviwalkl(810)
            esmefail('up')
        if countd in [11]:
            shewalkl(650)
        if countd in range(12, 16):
            shewalkr(650)
        if countd in [16]:
            if counttxt >= 32:
                shebroom('left', -100)
                POSY_SHE -= 2.5
            else:
                shewalkr(650)
    if keys[pygame.K_SPACE] and play_dialog and counttxt >= len(lstdialog[countd].split(':')[1])-1:
        if countd in [3] and counttxt >= 90:
            nextdia = True
        if countd in [7] and counttxt >= 65:
            nextdia = True
        elif countd not in [3, 7]:
            nextdia = True
    elif nextdia:
        if not keys[pygame.K_SPACE]:
            countd += 1
            if lstdialog[countd-1].split()[0] != lstdialog[countd].split()[0]:
                ANIM = 0
            counttxt, posx_txt, posy_txt = 0, 200, 80
            dialogbox[9] = pygame.image.load('sprite/dialogbox10.png')
            nextdia = False

#---------------------------------------------------------------------------
def scrolling():
    """scrolling background_ph"""
    global X
    global Y
    global PLAYER_RADIUS
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    
    #แกนX
    if X > stage_wildth-PLAYER_RADIUS:
        X = stage_wildth-PLAYER_RADIUS
    if X < PLAYER_RADIUS:
        X = PLAYER_RADIUS
    if X < start_scrolling_x:
        PLAYER_POSITION_X = X
    elif X > stage_wildth-start_scrolling_x:
        PLAYER_POSITION_X = X-stage_wildth+width
#     else:
#         PLAYER_POSITION_Y = start_scrolling_y
#         stage_position_y += -vel

    #แกนY
    if Y > stage_height-PLAYER_RADIUS:
        Y = stage_height-PLAYER_RADIUS
    if Y < PLAYER_RADIUS:
        Y = PLAYER_RADIUS
    if Y < start_scrolling_y:
        PLAYER_POSITION_Y = Y
    elif Y > stage_height-start_scrolling_y:
        PLAYER_POSITION_Y = Y-stage_height+height
#     else:
#         PLAYER_POSITION_Y = start_scrolling_y
#         stage_position_y += -vel
#---------------------------------------------------------------------------
def wall(wall=[(0,0,0,0)]):
    """wall"""
    global X
    global Y
    global BOOK
    global CHECK
    global RIGHT
    global LEFT
    global DOWN
    global UP
    global PLAYER_RADIUS
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    if keys[pygame.K_a] and X > vel and open_book == False and safe < 1 and not play_cutscene:
        for i,j,k,l in wall:
            if i < X < j and k < Y < l-15:
                adam = 0
                break
            else:
                adam = vel
        X -= adam
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
    elif keys[pygame.K_d] and open_book == False and safe < 1 and not play_cutscene:
        for i,j,k,l in wall:
            if i-15 < X < j-15 and k < Y < l-15:
                adam = 0
                break
            else:
                adam = vel
        X += adam
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
    elif keys[pygame.K_s] and open_book == False and safe < 1 and not play_cutscene:
        for i,j,k,l in wall:
            if i < X < j-15 and k-15 < Y < l-15:
                adam = 0
                break
            else:
                adam = vel
        Y += adam
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
    elif keys[pygame.K_w] and open_book == False and safe < 1 and not play_cutscene:
        for i,j,k,l in wall:
            if i < X < j-15 and k < Y < l:
                adam = 0
                break
            else:
                adam = vel
        Y -= adam
        RIGHT = False
        LEFT = False
        UP = True
        DOWN = False
        CHECK = 'UP'
    else:
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = False

    scrolling()
#------------------Photohunt--------------------------------------
font_ph = pygame.font.Font('sprite/photohunt/2005_iannnnnAMD.ttf', 72)
HeartImg = pygame.image.load('sprite/photohunt/heart.png')
bg_ph_1 = pygame.image.load('sprite/photohunt/stage 1.png')
bg_sound_ph1 = pygame.mixer.Sound('sprite/photohunt/main.mp3'); bg_sound_ph1.set_volume(0.3)
bg_ph_2 = pygame.image.load('sprite/photohunt/stage 2.png')
bg_sound_ph2 = pygame.mixer.Sound('sound/tech_rom.mp3'); bg_sound_ph2.set_volume(0.3)
bg_ph_3 = pygame.image.load('sprite/photohunt/stage 3.png')
bg_sound_ph3 = pygame.mixer.Sound('sound/research_roon.mp3'); bg_sound_ph3.set_volume(0.3)
c_sound = pygame.mixer.Sound("sprite\magic\magicsound.mp3"); c_sound.set_volume(0.5)
w_sound = pygame.mixer.Sound("sound\Swoosh.mp3"); w_sound.set_volume(0.5)

stage = 0
score_value = 0
health_value = 3
foundph1_1 = foundph1_2 = foundph1_3 = foundph1_4 = foundph1_5 = foundph1_6 = foundph1_7 = 1
foundph2_1 = foundph2_2 = foundph2_3 = foundph2_4 = foundph2_5 = foundph2_6 = foundph2_7 = foundph2_8 = 1
foundph3_1 = foundph3_2 = foundph3_3 = foundph3_4 = foundph3_5 = foundph3_6 = 1
sec = 62 # Timeset <<<<<<<<<<<
WALK_AVI = 0

correctImg = readvar('photohunt.txt', 'circle')

def drawcorrect(posx, posy):
    global WALK_AVI
    if WALK_AVI > len(correctImg)-1:
        win.blit(correctImg[len(correctImg)-1], (posx, posy))
    else:
        win.blit(correctImg[WALK_AVI], (posx, posy))
    WALK_AVI += 1

#----------Puzzle--------------------
safe, cd_pz, down_pz, up_pz = 0, 0, 5, 5
safe_img, bar, arrow = pygame.image.load("sprite/puzzle/lock.png"), pygame.image.load("sprite/puzzle/bar.png"), pygame.image.load("sprite/puzzle/arrow.png")
bat, bone, candle = pygame.image.load("sprite/puzzle/bat.png"), pygame.image.load("sprite/puzzle/bone.png"), pygame.image.load("sprite/puzzle/candle.png")
candy, hat, poison = pygame.image.load("sprite/puzzle/candy.png"), pygame.image.load("sprite/puzzle/hat.png"), pygame.image.load("sprite/puzzle/poison.png")
pot, pumpkin, rip = pygame.image.load("sprite/puzzle/pot.png"), pygame.image.load("sprite/puzzle/pumpkin.png"), pygame.image.load("sprite/puzzle/rip.png")
spider, web = pygame.image.load("sprite/puzzle/spider.png"), pygame.image.load("sprite/puzzle/web.png")
col_up = {10 : hat, 0 : bat, 1 : candy, 2 : candle, 3 : poison, 4 : web, 5 : rip, 6 : pumpkin, 7 : spider, 8 : bone, 9 : pot}
col_mid = {0 : hat, 1 : bat, 2 : candy, 3 : candle, 4 : poison, 5 : web, 6 : rip, 7 : pumpkin, 8 : spider, 9 : bone, 10 : pot}
col_down = {1 : hat, 2 : bat, 3 : candy, 4 : candle, 5 : poison, 6 : web, 7 : rip, 8 : pumpkin, 9 : spider, 10 : bone, 0 : pot}
row1, row2, row3, row4 = 0, 0 ,0 ,0
row = {1 : row1, 2 : row2, 3 : row3, 4 : row4}
rowza = 1
arrow_pos = {1:540 , 2:610, 3:677, 4:740}
yrow = {1:410, 2:410, 3:410, 4:410}

def col(row, xrow, yrow):
    win.blit(col_down[row], (xrow, yrow))
    win.blit(col_mid[row], (xrow, yrow+90))
    win.blit(col_up[row], (xrow, yrow+180))
#---------------------------------------------------------------------------
"""mainloop"""
while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False
        if keys[pygame.K_e] and PLAY_MAIN:
            open_book = True

    if PLAY_MAIN:
        pygame.time.delay(45)
    #--------------hallway---------------
        if gohallway == True: #HALLWAY
            # redrawsup()
            # bg_hall.play(-1,fade_ms=5000)
            wall(walls["hallway"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if X == 13 and Y >= 328 and Y <= 388:
                bg = pygame.image.load("sprite/Path.jpg")
                X = 1123
                Y = 343
                gohallway = False
                gopath = True
                gofirstaid = False
                gocanteen = False
            elif Y >= 598:
                bg_hall.stop()
                bg = pygame.image.load("sprite/entryhall.jpg")
                X = 508
                Y = 43
                gohallway = False
                goentry = True
            elif Y <= 13:
                bg = pygame.image.load("sprite/firstaidroom.jpg")
                Y = 583
                gohallway = False
                gopath = False
                gofirstaid = True
                gocanteen = False
            elif X >= 1198:
                bg = pygame.image.load("sprite/canteen.jpg")
                X = 33
                Y = 163
                gohallway = False
                gopath = False
                gofirstaid = False
                gocanteen = True
            elif X >= 628:
                win.blit(bg ,(-628, rel_y-bg_height))
            elif Y >= 358:
                win.blit(bg ,(rel_x-bg_width, -358))
            else:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
    #--------------canteen---------------
        elif gocanteen == True: #CANTEEN
            wall(walls["canteen"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height
            bg_hall.stop()
            
            if X >= 1203:
                X = 28
                Y = 463
                stage_height = 720
                bg = pygame.image.load("sprite/eastcorridor_1.jpg")
                gocanteen = False
                goeastcor_1 = True
            elif Y >= 778 and Y <= 838 and X >= 828:
                X = 28
                Y = 223
                stage_height = 720
                bg = pygame.image.load("sprite/eastgarden.jpg")
                gocanteen = False
                goeastgar = True
            elif X <= 13 and Y >= 148 and Y <= 163:
                X = 1168
                Y = 238
                stage_height = 720
                bg = pygame.image.load("sprite/hallway.jpg")
                gohallway = True
                gocanteen = False
            elif X >= 798 and Y >= 283 and Y <= 598:
                stage_height = 720
                win.blit(bg ,(-453, -283))
            elif X >= 453:
                stage_height = 950
                win.blit(bg ,(-453, rel_y-bg_height))
            else:
                stage_height = 950
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
            if 918 <= X <= 1098 and 88 <= Y <= 118:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    safe += 1
    #--------------eastcor1--------------
        elif goeastcor_1 == True:
            wall(walls["eastcor1"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if X <= 13:
                bg = pygame.image.load("sprite/canteen.jpg")
                X = 1108
                Y = 478
                goeastcor_1 = False
                gocanteen = True
            elif Y <= 13:
                bg = pygame.image.load("sprite/eastcorridor_2.jpg")
                Y = 583
                goeastcor_1 = False
                goeastcor_2 = True
            elif Y >= 628:
                bg = pygame.image.load("sprite/eastgarden.jpg")
                X = 388
                Y = 28
                goeastcor_1 = False
                goeastgar = True
            elif Y >= 178:
                win.blit(bg ,(-28, -178))
            else:
                win.blit(bg ,(-28, rel_y-bg_height))
            if 1128 <= X <= 1198 and 463 <= Y < 523:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_hall.stop()
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/classroom.jpg")
                    X = 58
                    Y = 268
                    goeastcor_1 = False
                    classroom1 = True
                    CHECK = "RIGHT"
            if 1128 <= X <= 1198 and 103 <= Y < 148:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_hall.stop()
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/classroom.jpg")
                    X = 58
                    Y = 268
                    goeastcor_1 = False
                    classroom2 = True
                    CHECK = "RIGHT"
    #--------------eastcor2--------------
        elif goeastcor_2 == True:
            wall(walls["eastcor2"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if Y >= 632:
                bg = pygame.image.load("sprite/eastcorridor_1.jpg")
                Y = 28
                goeastcor_2 = False
                goeastcor_1 = True
            elif X <= 13:
                bg = pygame.image.load("sprite/battleroom.jpg")
                X = 1198
                Y = 343
                goeastcor_2 = False
                gobattle = True
            elif Y <= 13:
                bg = pygame.image.load("sprite/eastforest.jpg")
                X = 1123
                Y = 613
                goeastcor_2 = False
                goeastfor = True
            else:
                win.blit(bg ,(-28, -13))
            if 1128 <= X <= 1198 and 328 <= Y < 373:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_hall.stop()
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/classroom.jpg")
                    X = 58
                    Y = 268
                    goeastcor_2 = False
                    classroom3 = True
                    CHECK = "RIGHT"
    #--------------classroom-------------
        elif classroom1 == True:
            wall(walls["classroom"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            win.blit(bg ,(-238, -118))
            if 13 <= X <= 28 and 253 <= Y < 283:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/eastcorridor_1.jpg")
                    X = 1093
                    Y = 493
                    goeastcor_1 = True
                    classroom1 = False
                    CHECK = "LEFT"
                    bg_hall.play(-1,fade_ms=5000)
    #--------------classroom2--------------
        elif classroom2 == True:
            wall(walls["classroom"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            win.blit(bg ,(-238, -118))
            if 13 <= X <= 28 and 253 <= Y < 283:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/eastcorridor_1.jpg")
                    X = 1093
                    Y = 133
                    goeastcor_1 = True
                    classroom2 = False
                    CHECK = "LEFT"
                    bg_hall.play(-1,fade_ms=5000)
    #--------------classroom3--------------
        elif classroom3 == True:
            wall(walls["classroom"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            win.blit(bg ,(-238, -118))
            if 13 <= X <= 28 and 253 <= Y < 283:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/eastcorridor_2.jpg")
                    X = 1093
                    Y = 358
                    goeastcor_2 = True
                    classroom3 = False
                    CHECK = "LEFT"
                    bg_hall.play(-1,fade_ms=5000)
    #--------------eastgarden------------
        elif goeastgar == True:
            wall(walls["eastgar"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if X <= 13:
                bg = pygame.image.load("sprite/canteen.jpg")
                stage_height = 950
                X = 813
                Y = 823
                goeastgar = False
                gocanteen = True
            elif Y <= 13:
                bg = pygame.image.load("sprite/eastcorridor_1.jpg")
                X = 433
                Y = 613
                goeastgar = False
                goeastcor_1 = True
            else:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
    #--------------firstaid--------------
        elif gofirstaid == True: #FIRSTAID ROOM
            wall(walls["firstaid"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if Y >= 613:
                bg = pygame.image.load("sprite/hallway.jpg")
                X = 253
                Y = 43
                gohallway = True
                gofirstaid = False
                gobattle = False
            elif X >= 1207:
                bg = pygame.image.load("sprite/battleroom.jpg")
                X = 28
                Y = 373
                gohallway = False
                gofirstaid = False
                gobattle = True
            elif Y >= 13 and X >= 703:
                win.blit(bg ,(-703, -13))
            elif Y >= 13:
                win.blit(bg ,(rel_x-bg_width, -13))
            elif X >= 703:
                win.blit(bg ,(-703, rel_y-bg_height))
            else:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
    #---------------battle---------------
        elif gobattle == True: #BATTLE ROOM
            wall(walls["battle"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height
            
            if X <= 13:
                bg = pygame.image.load("sprite/firstaidroom.jpg")
                X = 1168
                Y = 493
                gobattle = False
                gofirstaid = True
            elif X >= 1222:
                bg = pygame.image.load("sprite/eastcorridor_2.jpg")
                X = 28
                Y = 373
                gobattle = False
                goeastcor_2 = True
            elif X >= 523 and Y >= 103:
                win.blit(bg ,(-523, -103))
            elif Y >= 103:
                win.blit(bg ,(rel_x-bg_width, -103))
            elif X >= 523:
                win.blit(bg ,(-523, -103))
            else:
                win.blit(bg ,(rel_x-bg_width, -103))
    #----------------path----------------
        elif gopath == True:
            wall(walls["path"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height
            if X >= 1168:
                bg = pygame.image.load("sprite/hallway.jpg")
                X = 28
                Y = 358
                gohallway = True
                gopath = False
            elif X <= 13:
                bg = pygame.image.load("sprite/westcorridor_1.jpg")
                X = 1183
                Y = 373
                gopath = False
                gowestcor_1 = True
            elif Y <= 13:
                bg = pygame.image.load("sprite/meetingroom.jpg")
                X = 433
                Y = 553
                gopath = False
                gomeeting = True
            elif (X <= 598 and Y >= 313) or (X <= 598 and Y < 313):
                win.blit(bg ,(-598, -313))
            elif X >= 1108:
                win.blit(bg ,(-1108, -313))
            elif Y < 313 or Y >= 313:
                win.blit(bg ,(rel_x-bg_width, -313))
            if STORY1:
                if not play_cutscene:
                    POSX_ESME, POSY_ESME = 300, 343
                    POSX_SHE, POSY_SHE = 150, 343
                    POSX_AVI, POSY_AVI = 1150, 343
                    play_cutscene = True
                cutscene()
    #--------------meeting---------------
        elif gomeeting == True: #MEETING ROOM
            wall(walls["meeting"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if X >= 403 and X <= 448 and Y > 553:
                bg = pygame.image.load("sprite/path.jpg")
                gomeeting = False
                gopath = True
                X = 733
                Y = 28
            elif X >= 523 and Y >= 418:
                win.blit(bg ,(-523, -418))
            elif X >= 523:
                win.blit(bg ,(-523, rel_y-bg_height))
            elif Y >= 418:
                win.blit(bg ,(rel_x-bg_width, -418))
            else:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
    #--------------entryhall-------------
        elif goentry == True:
            wall(walls["entryhall"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if X <= 13:
                bg = pygame.image.load("sprite/halls.jpg")
                X = 1153
                Y = 178
                goentry = False
                gohalls = True
            elif Y <= 13:
                bg = pygame.image.load("sprite/hallway.jpg")
                X = 463
                Y = 583
                bg_hall.play(-1,fade_ms=5000)
                goentry = False
                gohallway = True
            elif X >= 763 and Y >= 272:
                win.blit(bg ,(-763, -272))
            elif X >= 763:
                win.blit(bg ,(-763, rel_y-bg_height))
            elif Y >= 272:
                win.blit(bg ,(rel_x-bg_width, -272))
            else:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
    #----------------hall----------------
        elif gohalls == True:
            wall(walls["hall"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if X <= 13:
                bg = pygame.image.load("sprite/westgarden.jpg")
                X = 1123
                gohalls = False
                gowestgar = True
            elif X >= 1207:
                X = 28
                Y = 133
                bg = pygame.image.load("sprite/entryhall.jpg")
                gohalls = False
                goentry = True
            elif X >= 160 and Y >= 287:
                win.blit(bg ,(-160, -287))
            elif X >= 160:
                win.blit(bg ,(-160, rel_y-bg_height))
            elif Y >= 287:
                win.blit(bg ,(rel_x-bg_width, -287))
            else:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
    #-------------westgarden-------------
        elif gowestgar == True:
            wall(walls["westgar"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if X >= 1207:
                bg = pygame.image.load("sprite/halls.jpg")
                X = 73
                gowestgar = False
                gohalls = True
            elif Y <= 13:
                bg = pygame.image.load("sprite/westcorridor_1.jpg")
                X = 748
                Y = 613
                gowestgar = False
                gowestcor_1 = True
            else:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
    #--------------westcor1--------------
        elif gowestcor_1 == True:
            wall(walls["westcor1"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if Y >= 628:
                bg = pygame.image.load("sprite/westgarden.jpg")
                X = 832
                Y = 28
                gowestcor_1 = False
                gowestgar = True
            elif Y <= 13:
                bg = pygame.image.load("sprite/westcorridor_2.jpg")
                Y = 508
                gowestcor_1 = False
                gowestcor_2 = True
            elif X >= 1198:
                bg = pygame.image.load("sprite/path.jpg")
                X = 28
                Y = 343
                gowestcor_1 = False
                gopath = True
            elif Y >= 365:
                win.blit(bg ,(-28, -365))
            else:
                win.blit(bg ,(-28, rel_y-bg_height))
            if 13 <= X <= 28 and 313 <= Y < 388 and gopath == False:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_hall.stop()
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/apothecaryroom.jpg")
                    X = 973
                    Y = 433
                    gowestcor_1 = False
                    goapothe = True
                    CHECK = "LEFT"
            if 13 <= X <= 28 and 103 <= Y < 163:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_hall.stop()
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/teacherroom.jpg")
                    X = 958
                    Y = 373
                    gowestcor_1 = False
                    goteach = True
                    CHECK = "LEFT"
    #--------------westcor2--------------
        elif gowestcor_2 == True:
            wall(walls["westcor2"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if Y >= 613:
                bg = pygame.image.load("sprite/westcorridor_1.jpg")
                Y = 103
                gowestcor_2 = False
                gowestcor_1 = True
            elif Y <= 13:
                bg = pygame.image.load("sprite/westforest.jpg")
                X = 43
                Y = 598
                gowestcor_2 = False
                gowestfor = True
            elif Y >= 73:
                win.blit(bg ,(-28, -73))
            else:
                win.blit(bg ,(-28, rel_y-bg_height))
            if 13 <= X <= 28 and 208 <= Y < 358:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_hall.stop()
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/researchroom.jpg")
                    X = 973
                    Y = 433
                    gowestcor_2 = False
                    goresearch = True
                    CHECK = "LEFT"
    #-------------westforest-------------
        elif gowestfor == True:
            wall(walls["westfor"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if Y >= 628:
                bg = pygame.image.load("sprite/westcorridor_2.jpg")
                gowestfor = False
                gowestcor_2 = True
                X = 598
                Y = 28
            elif X >= 1213:
                bg = pygame.image.load("sprite/forest.jpg")
                X = 28
                Y = 418
                gowestfor = False
                goforest = True
            elif X >= 583:
                win.blit(bg ,(-583, -58))
            else:
                win.blit(bg ,(rel_x-bg_width, -58))
    #--------------forest----------------
        elif goforest == True:
            wall(walls["forest"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if X <= 13:
                bg = pygame.image.load("sprite/westforest.jpg")
                X = 1198
                goforest = False
                gowestfor = True
            elif X >= 1213:
                bg = pygame.image.load("sprite/eastforest.jpg")
                X = 28
                goforest = False
                goeastfor = True
            elif X >= 523 and Y >= 425:
                win.blit(bg ,(-523, -425))
            elif X >= 523:
                win.blit(bg ,(-523, rel_y-bg_height))
            elif Y >= 425:
                win.blit(bg ,(rel_x-bg_width, -425))
            else:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
    #-------------eastforest--------------
        elif goeastfor == True:
            wall(walls["eastfor"])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            if X <= 13:
                bg = pygame.image.load("sprite/forest.jpg")
                X = 1198
                Y = 418
                goeastfor = False
                goforest = True
            elif Y >= 628:
                bg = pygame.image.load("sprite/eastcorridor_2.jpg")
                X = 598
                Y = 28
                goeastfor = False
                goeastcor_2 = True
            elif X >= 583:
                win.blit(bg ,(-583, -58))
            else:
                win.blit(bg ,(rel_x-bg_width, -58))
    #------------apothecaryroom-----------
        elif goapothe == True:
            wall(walls['apothecaryroom'])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            win.blit(bg ,(-238, -58))
            if 1168 <= X <= 1280 and 358 <= Y < 493:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/westcorridor_1.jpg")
                    X = 58
                    Y = 343
                    gowestcor_1 = True
                    goapothe = False
                    CHECK = "RIGHT"
                    bg_hall.play(-1,fade_ms=5000)
            win.fill((0,0,255), rect=[403,580,50,50])
            if 328 <= X <= 448 and 493 <= Y <= 523:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    PLAY_PH1 = True
                    PLAY_MAIN = False
    #------------teacherroom--------------
        elif goteach == True:
            wall(walls['teacherroom'])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            win.blit(bg ,(-238, -58))
            if 1168 <= X <= 1630 and 358 <= Y < 493:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/westcorridor_1.jpg")
                    X = 58
                    Y = 133
                    gowestcor_1 = True
                    goteach = False
                    CHECK = "RIGHT"
                    bg_hall.play(-1,fade_ms=5000)
            win.fill((0,0,255), rect=[800,433,50,50])
            if 763 <= X <= 808 and 343 <= Y <= 418:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    PLAY_PH3 = True
                    PLAY_MAIN = False
    #------------researchroom-------------
        elif goresearch == True:
            wall(walls['researchroom'])
            rel_x = -X % bg_width
            rel_y = -Y % bg_height

            win.blit(bg ,(-238, -58))
            if 1168 <= X <= 1630 and 358 <= Y < 493:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/westcorridor_2.jpg")
                    X = 58
                    Y = 298
                    gowestcor_2 = True
                    goteach = False
                    CHECK = "RIGHT"
                    bg_hall.play(-1,fade_ms=5000)
            win.fill((0,0,255), rect=[223,450,50,50])
            if 118 <= X <= 283 and 373 <= Y <= 388:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    PLAY_PH2 = True
                    PLAY_MAIN = False

        if not play_cutscene:
            redrawGameWindow()

#-----------------Photohunt--------------------
    elif PLAY_PH1:
        pygame.time.delay(30)
        sec -= 0.05
        if stage == 0:
            bg_sound_ph1.play(-1)
            stage = 1
        if sec < 61:
            stage = 1
            win.blit(bg_ph_1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if stage == 1:
                # screen.blit(background, (0, 0))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    #print(mx, my)
                    #print(health_value)
                    if ((153 < mx < 195 and 150 < my < 239) or (740 < mx < 780 and 150 < my < 239)) and foundph1_1 == 1:  # เทียน
                        c_sound.play()
                        score_value += 1
                        foundph1_1 = 2
                    elif ((569 < mx < 616 and 92 < my < 202) or (1183 < mx < 1217 and 92 < my < 202)) and foundph1_2 == 1:  # หนังสือ
                        c_sound.play()
                        score_value += 1
                        foundph1_2 = 2
                    elif ((245 < mx < 326 and 280 < my < 360) or (840 < mx < 885 and 280 < my < 360)) and foundph1_3 == 1:  # อะไรไม่รุข้างหน้าต่าง
                        c_sound.play()
                        score_value += 1
                        foundph1_3 = 2
                    elif ((563 < mx < 616 and 312 < my < 373) or (1165 < mx < 1221 and 312 < my < 373)) and foundph1_4 == 1:  # หนังสือชั้น 3
                        c_sound.play()
                        score_value += 1
                        foundph1_4 = 2
                    elif ((125 < mx < 173 and 492 < my < 527) or (700 < mx < 760 and 492 < my < 527)) and foundph1_5 == 1:  # ไม้ไรสักอย่าง
                        c_sound.play()
                        score_value += 1
                        foundph1_5 = 2
                    elif ((350 < mx < 425 and 470 < my < 528) or (942 < mx < 1022 and 470 < my < 528)) and foundph1_6 == 1:  # ถ้วย
                        c_sound.play()
                        score_value += 1
                        foundph1_6 = 2
                    elif ((60 < mx < 134 and 650 < my < 703) or (649 < mx < 727 and 671 < my < 703)) and foundph1_7 == 1:  # ไห้ไรสักอย่าง
                        c_sound.play()
                        score_value += 1
                        foundph1_7 = 2
                    # wrong click
                    if not((153 < mx < 195 and 150 < my < 239) or (740 < mx < 780 and 150 < my < 239)) and \
                        not((569 < mx < 616 and 92 < my < 202) or (1183 < mx < 1217 and 92 < my < 202)) and \
                        not((245 < mx < 326 and 280 < my < 360) or (840 < mx < 885 and 280 < my < 360)) and \
                        not((563 < mx < 616 and 312 < my < 373) or (1165 < mx < 1221 and 312 < my < 373)) and \
                        not((125 < mx < 173 and 492 < my < 527) or (700 < mx < 760 and 492 < my < 527)) and \
                        not((350 < mx < 425 and 470 < my < 528) or (942 < mx < 1022 and 470 < my < 528)) and \
                        not((60 < mx < 134 and 650 < my < 703) or (649 < mx < 727 and 671 < my < 703)):
                        if health_value > 0:
                            w_sound.play()
                            health_value -= 1
        if foundph1_1 == 2: # เทียน
            drawcorrect(112, 157)
            drawcorrect(712, 157)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_1.blit(correctImg[16], (112, 157))
                bg_ph_1.blit(correctImg[16], (712, 157))
                foundph1_1 = 3
        if foundph1_2 == 2: # หนังสือ
            drawcorrect(550, 100)
            drawcorrect(1140, 100)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_1.blit(correctImg[16], (550, 100))
                bg_ph_1.blit(correctImg[16], (1140, 100))
                foundph1_2 = 3
        if foundph1_3 == 2: # อะไรไม่รุข้างหน้าต่าง
            drawcorrect(221, 275)
            drawcorrect(811, 275)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_1.blit(correctImg[16], (221, 275))
                bg_ph_1.blit(correctImg[16], (811, 275))
                foundph1_3 = 3
        if foundph1_4 == 2: # หนังสือชั้น 3
            drawcorrect(550, 285)
            drawcorrect(1140, 285)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_1.blit(correctImg[16], (550, 285))
                bg_ph_1.blit(correctImg[16], (1140, 285))
                foundph1_4 = 3
        if foundph1_5 == 2: # ไม้ไรสักอย่าง
            drawcorrect(95, 450)
            drawcorrect(688, 450)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_1.blit(correctImg[16], (95, 450))
                bg_ph_1.blit(correctImg[16], (688, 450))
                foundph1_5 = 3
        if foundph1_6 == 2: # ถ้วย
            drawcorrect(348, 440)
            drawcorrect(937, 440)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_1.blit(correctImg[16], (348, 440))
                bg_ph_1.blit(correctImg[16], (937, 440))
                foundph1_6 = 3
        if foundph1_7 == 2: # ไห้ไรสักอย่าง
            drawcorrect(640,617)
            drawcorrect(52,617)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_1.blit(correctImg[16], (640, 617))
                bg_ph_1.blit(correctImg[16], (52, 617))
                foundph1_7 = 3
        if health_value == 3:
            win.blit(HeartImg, (1050, 0))
            win.blit(HeartImg, (1115, 0))
            win.blit(HeartImg, (1180, 0))
        if health_value == 2:
            win.blit(HeartImg, (1115, 0))
            win.blit(HeartImg, (1180, 0))
        if health_value == 1:
            win.blit(HeartImg, (1180, 0))
        score = font_ph.render('Total Left '+str(score_value) + '/7', True, (255, 255, 255))
        win.blit(score, (35, 10))
        sec_show = font_ph.render('Time Left: ' + str(int(sec)), True, (255, 255, 255))
        win.blit(sec_show, (525, 10))
        if sec > 61:
            rules = pygame.image.load('sprite/photohunt/RULES.png')
            win.blit(rules,(0,0))
        if score_value == 7:
            win_screen = pygame.image.load('sprite/photohunt/U WIN.png')
            win.blit(win_screen, (0,0))
            bg_sound_ph1.stop()
            PLAY_PH1 = False ;PLAY_MAIN = True
            score_value, sec, health_value, stage = 0, 62, 3, 0
        elif health_value == 0 or sec <= 0:
            lose_screen = pygame.image.load('sprite/photohunt/U lose.png')
            win.blit(lose_screen, (0,0))
            bg_sound_ph1.stop()
            PLAY_PH1 = False ;PLAY_MAIN = True
            score_value, sec, health_value, stage = 0, 62, 3, 0

    elif PLAY_PH2:
        pygame.time.delay(30)
        sec -= 0.05
        if stage == 0:
            bg_sound_ph2.play(-1)
            stage = 1
        if sec < 61:
            stage = 1
            win.blit(bg_ph_2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if stage == 1:
                # screen.blit(background, (0, 0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    #print(mx, my)
                    #print(health_value)
                    if ((545 < mx < 610 and 459 < my < 489) or (1162 < mx < 1225 and 454 < my < 492)) and foundph2_1 == 1: # แก้ววายด้านขวา
                        c_sound.play()
                        score_value += 1
                        foundph2_1 = 2
                    elif ((251 < mx < 281 and 495 < my < 525) or (878 < mx < 915 and 493 < my < 528)) and foundph2_2 == 1: # สามเหลี่ยม
                        c_sound.play()
                        score_value += 1
                        foundph2_2 = 2
                    elif ((555 < mx < 587 and 653 < my < 686) or (1175 < mx < 1210 and 653 < my < 686)) and foundph2_3 == 1: #ไวโอลิน
                        c_sound.play()
                        score_value += 1
                        foundph2_3 = 2
                    elif ((85 < mx < 133 and 521 < my < 562) or (709 < mx < 757 and 523 < my < 560)) and foundph2_4 == 1: # กระเป๋า
                        c_sound.play()
                        score_value += 1
                        foundph2_4 = 2
                    elif ((129 < mx < 170 and 430 < my < 468) or (759 < mx < 793 and 433 < my < 468)) and foundph2_5 == 1: #ลิ้นชัก
                        c_sound.play()
                        score_value += 1
                        foundph2_5 = 2
                    elif ((406 < mx < 486 and 326 < my < 373) or (1037 < mx < 1104 and 326 < my < 376)) and foundph2_6 == 1: #กระดาษไรไม่รุ
                        c_sound.play()
                        score_value += 1
                        foundph2_6 = 2
                    elif ((231 < mx < 277 and 221 < my < 256) or (853 < mx < 911 and 223 < my < 259)) and foundph2_7 == 1: #ผลไม้?
                        c_sound.play()
                        score_value += 1
                        foundph2_7 = 2
                    elif ((355 < mx < 395 and 440 < my < 510) or (970 < mx < 1010 and 440 < my < 510)) and foundph2_8 == 1:
                        c_sound.play()
                        score_value += 1
                        foundph2_8 = 2
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
                            w_sound.play()
                            health_value -= 1
        if foundph2_1 == 2: # แก้ววายด้านขวา
            drawcorrect(536, 425)
            drawcorrect(1158, 425)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_2.blit(correctImg[16], (536, 425))
                bg_ph_2.blit(correctImg[16], (1158, 425))
                foundph2_1 = 3
        if foundph2_2 == 2: # สามเหลี่ยม
            drawcorrect(226, 461)
            drawcorrect(845, 461)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_2.blit(correctImg[16], (226, 461))
                bg_ph_2.blit(correctImg[16], (845, 461))
                foundph2_2 = 3
        if foundph2_3 == 2: #ไวโอลีน
            drawcorrect(519, 614)
            drawcorrect(1146, 614)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_2.blit(correctImg[16], (519, 614))
                bg_ph_2.blit(correctImg[16], (1146, 614))
                foundph2_3 = 3
        if foundph2_4 == 2: #กระเป๋า
            drawcorrect(68, 491)
            drawcorrect(685, 491)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_2.blit(correctImg[16], (68, 491))
                bg_ph_2.blit(correctImg[16], (685, 491))
                foundph2_4 = 3
        if foundph2_5 == 2: #ลิ้นชัก
            drawcorrect(112, 399)
            drawcorrect(730, 399)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_2.blit(correctImg[16], (112, 399))
                bg_ph_2.blit(correctImg[16], (730, 399))
                foundph2_5 = 3
        if foundph2_6 == 2: #ม้วนกระดาศ
            drawcorrect(402, 300)
            drawcorrect(1021, 300)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_2.blit(correctImg[16], (402, 300))
                bg_ph_2.blit(correctImg[16], (1021, 300))
                foundph2_6 = 3
        if foundph2_7 == 2: # ผลไม้?
            drawcorrect(216, 195)
            drawcorrect(835, 195)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_2.blit(correctImg[16], (216, 195))
                bg_ph_2.blit(correctImg[16], (835, 195))
                foundph2_7 = 3
        if foundph2_8 == 2:
            drawcorrect(945, 420)
            drawcorrect(328, 420)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_2.blit(correctImg[16], (945, 420))
                bg_ph_2.blit(correctImg[16], (328, 420))
                foundph2_8 = 3
        if health_value == 3:
            win.blit(HeartImg, (1050, 0))
            win.blit(HeartImg, (1115, 0))
            win.blit(HeartImg, (1180, 0))
        if health_value == 2:
            win.blit(HeartImg, (1115, 0))
            win.blit(HeartImg, (1180, 0))
        if health_value == 1:
            win.blit(HeartImg, (1180, 0))
        score = font_ph.render('Total Left '+str(score_value) + '/8', True, (255, 255, 255))
        win.blit(score, (35, 10))
        sec_show = font_ph.render('Time Left: ' + str(int(sec)), True, (255, 255, 255))
        win.blit(sec_show, (525, 10))
        if sec > 61:
            rules = pygame.image.load('sprite/photohunt/RULES.png')
            win.blit(rules,(0,0))
        if score_value == 8:
            win_screen = pygame.image.load('sprite/photohunt/U WIN.png')
            win.blit(win_screen, (0,0))
            bg_sound_ph2.stop()
            PLAY_PH2 = False ;PLAY_MAIN = True
            score_value, sec, health_value, stage = 0, 62, 3, 0
        elif health_value <= 0 or sec <= 0:
            lose_screen = pygame.image.load('sprite/photohunt/U lose.png')
            win.blit(lose_screen, (0,0))
            bg_sound_ph2.stop()
            PLAY_PH2 = False ;PLAY_MAIN = True
            score_value, sec, health_value, stage = 0, 62, 3, 0

    elif PLAY_PH3:
        pygame.time.delay(30)
        sec -= 0.05
        if stage == 0:
            bg_sound_ph3.play(-1)
            stage = 1
        if sec < 61:
            stage = 1
            win.blit(bg_ph_3, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if stage == 1:
                # win.blit(bg_ph_3, (0, 0))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    #print(mx, my)
                    #print(health_value)
                    if ((578 < mx < 617 and 242 < my < 282) or (1182 < mx < 1217 and 242 < my < 282)) and foundph3_1 == 1: # หมีบน
                        c_sound.play()
                        score_value += 1
                        foundph3_1 = 2
                    elif ((513 < mx < 570 and 324 < my < 381) or (1104 < mx < 1167 and 324 < my < 381)) and foundph3_2 == 1: # เก้าอี้
                        c_sound.play()
                        score_value += 1
                        foundph3_2 = 2
                    elif ((216 < mx < 251 and 549 < my < 582) or (811 < mx < 841 and 549 < my < 582)) and foundph3_3 == 1: # ไข่มุก
                        c_sound.play()
                        score_value += 1
                        WALK_AVI = 0
                        foundph3_3 = 2
                    elif ((156 < mx < 191 and 237 < my < 302) or (748 < mx < 791 and 237 < my < 302)) and foundph3_4 == 1: # แก้วบนชั้นวาง ชั้น 2
                        c_sound.play()
                        score_value += 1
                        foundph3_4 = 2
                    elif ((259 < mx < 289 and 394 < my < 434) or (849 < mx < 892 and 394 < my < 434)) and foundph3_5 == 1: # หมีล่าง
                        c_sound.play()
                        score_value += 1
                        foundph3_5 = 2
                    elif ((111 < mx < 142 and 185 < my < 229) or (700 < mx < 736 and 185 < my < 229)) and foundph3_6 == 1: #ขวดแก้วชั้นบน
                        c_sound.play()
                        score_value += 1
                        foundph3_6 = 2
                    #wrong click
                    if not((578 < mx < 617 and 242 < my < 282) or (1182 < mx < 1217 and 242 < my < 282)) and\
                        not((513 < mx < 570 and 324 < my < 381) or (1104 < mx < 1167 and 324 < my < 381)) and\
                            not((216 < mx < 251 and 549 < my < 582) or (811 < mx < 841 and 549 < my < 582)) and\
                                not((156 < mx < 191 and 237 < my < 302) or (748 < mx < 791 and 237 < my < 302)) and\
                                    not((259 < mx < 289 and 394 < my < 434) or (849 < mx < 892 and 394 < my < 434)) and\
                                        not((111 < mx < 142 and 185 < my < 229) or (700 < mx < 736 and 185 < my < 229)):
                    # else:
                        if health_value > 0:
                            w_sound.play()
                            health_value -= 1

        if foundph3_1 == 2: # หมีบน
            drawcorrect(551, 213)
            drawcorrect(1150, 213)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_3.blit(correctImg[16], (551, 213))
                bg_ph_3.blit(correctImg[16], (1150, 213))
                foundph3_1 = 3
        if foundph3_2 == 2: # เก้าอี้
            drawcorrect(486, 297)
            drawcorrect(1086, 297)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_3.blit(correctImg[16], (486, 297))
                bg_ph_3.blit(correctImg[16], (1086, 297))
                foundph3_2 = 3
        if foundph3_3 == 2: # ไข่มุก
            drawcorrect(180, 515)
            drawcorrect(776, 515)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_3.blit(correctImg[16], (180, 515))
                bg_ph_3.blit(correctImg[16], (776, 515))
                foundph3_3 = 3
        if foundph3_4 == 2: # แก้วบนชั้นวาง ชั้น 2
            drawcorrect(127, 214)
            drawcorrect(727, 214)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_3.blit(correctImg[16], (127, 214))
                bg_ph_3.blit(correctImg[16], (727, 214))
                foundph3_4 = 3
        if foundph3_5 == 2: # หมีล่าง
            drawcorrect(223, 365)
            drawcorrect(812, 365)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_3.blit(correctImg[16], (223, 365))
                bg_ph_3.blit(correctImg[16], (812, 365))
                foundph3_5 = 3
        if foundph3_6 == 2: #ขวดแก้วชั้นบน
            drawcorrect(70, 155)
            drawcorrect(670, 155)
            if WALK_AVI > 16:
                WALK_AVI = 0
                bg_ph_3.blit(correctImg[16], (70, 155))
                bg_ph_3.blit(correctImg[16], (670, 155))
                foundph3_6 = 3
        if health_value == 3:
            win.blit(HeartImg, (1050, 0))
            win.blit(HeartImg, (1115, 0))
            win.blit(HeartImg, (1180, 0))
        if health_value == 2:
            win.blit(HeartImg, (1115, 0))
            win.blit(HeartImg, (1180, 0))
        if health_value == 1:
            win.blit(HeartImg, (1180, 0))
        score = font_ph.render('Total Left '+str(score_value) + '/6', True, (255, 255, 255))
        win.blit(score, (35, 10))
        sec_show = font_ph.render('Time Left: ' + str(int(sec)), True, (255, 255, 255))
        win.blit(sec_show, (525, 10))
        if sec > 61:
            rules = pygame.image.load('sprite/photohunt/RULES.png')
            win.blit(rules,(0,0))
        if score_value == 6:
            win_screen = pygame.image.load('sprite/photohunt/U WIN.png')
            win.blit(win_screen, (0,0))
            bg_sound_ph3.stop()
            PLAY_PH3 = False ;PLAY_MAIN = True
            score_value, sec, health_value, stage = 0, 62, 3, 0
        elif health_value <= 0 or sec <= 0:
            lose_screen = pygame.image.load('sprite/photohunt/U lose.png')
            win.blit(lose_screen, (0,0))
            bg_sound_ph3.stop()
            PLAY_PH3 = False ;PLAY_MAIN = True
            score_value, sec, health_value, stage = 0, 62, 3, 0

#-----------------MAIN GAME-----------------------------------------------

    if open_book and PLAY_MAIN:

        if book_map:
            book_anim += 1
            if book_anim+1 >= 9:
                book_anim = 9
            if keys[pygame.K_d]:
                nextpage, book_inven, book_map = True, True, False

        if nextpage and book_inven:
            if book_anim != 19:
                book_anim += 1
            if book_anim == 19:
                nextpage = False

        elif book_inven:
            if keys[pygame.K_d]:
                nextpage, book_menu, book_inven = True, True, False
            if keys[pygame.K_a]:
                backpage = True
            if backpage:
                if book_anim != 9:book_anim -= 1
                if book_anim == 9:book_map, book_inven, backpage = True, False, False

        if nextpage and book_menu:
            if book_anim != 29:book_anim += 1
            if book_anim == 29:nextpage = False
            
        elif book_menu:
            if keys[pygame.K_a]:
                backpage = True
            if backpage:
                if book_anim != 19:
                    book_anim -= 1
                if book_anim == 19:
                    book_inven, book_menu, backpage = True, False, False
                    
        if keys[pygame.K_e] and (book_anim == 9 or book_anim == 19 or book_anim == 29):
            backpage, book_map, book_inven, book_menu = True, False, False, False
            
        if backpage and not book_map and not book_inven and not book_menu:
            book_anim -= 1
            if book_anim == 0:
                backpage, open_book, book_map = False, False, True

        #print(nextpage, book_anim)
        win.blit(book_img[book_anim], (0, 0))

    if safe >= 1:
        if keys[pygame.K_f] and safe > 5:
            safe = -2
        win.blit(bar, (533, 455))

        # win.blit(colum[row1], (548, yrow))
        # win.blit(colum[row2], (618, yrow))
        # win.blit(colum[row3], (685, yrow))
        # win.blit(colum[row4], (748, yrow))

        if keys[pygame.K_d] and cd_pz > 5 and up_pz > 5 and down_pz > 5:
            rowza += 1
            cd_pz = -2
        if keys[pygame.K_a] and cd_pz > 5 and up_pz > 5 and down_pz > 5:
            rowza -= 1
            cd_pz = -2
        if rowza < 1:
            rowza = 4
        elif rowza > 4:
            rowza = 1

        if keys[pygame.K_w] and up_pz > 5 and cd_pz > 5:
            row[rowza] += 1
            cd_pz = -2
            up_pz = -5
            yrow[rowza] = 510
            if row[rowza] < 0:
                row[rowza] = 10
            elif row[rowza] > 10:
                row[rowza] = 0
            row1 = row[1]
            row2 = row[2]
            row3 = row[3]
            row4 = row[4]
        if keys[pygame.K_s] and down_pz > 5 and cd_pz > 5:
            row[rowza] -= 1
            cd_pz = -2
            down_pz = -5
            yrow[rowza] = 310
            if row[rowza] < 0:
                row[rowza] = 10
            elif row[rowza] > 10:
                row[rowza] = 0
            row1 = row[1]
            row2 = row[2]
            row3 = row[3]
            row4 = row[4]
        col(row1, 548, yrow[1])
        col(row2, 615, yrow[2])
        col(row3, 682, yrow[3])
        col(row4, 748, yrow[4])
        if up_pz < 5:
            yrow[rowza] -= 10
        if down_pz < 5:
            yrow[rowza] += 10

        win.blit(safe_img, (450,50))
        win.blit(arrow, (arrow_pos[rowza], 400))
        safe += 1
        cd_pz += 1
        up_pz += 1
        down_pz += 1
        # print(row)
        #print("row1", row1, "row2", row2, "row3", row3, "row4", row4)

    if PLAY_FRONT == True:
        frontgame()
    pygame.display.update()
    
    #print(X, Y)

pygame.quit()
