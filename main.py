import pygame, json
from pygame import mixer
from pygame import display
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

pygame.init()

#---------------------------------------------------------------------------
"""set variable"""
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("W <it> CH AcademY")
# bg = pygame.image.load("sprite/entryhall.jpg")

mapping = open("map.txt", "r").read()
mapping = dict(json.loads(mapping))
idmap = "20"
bg = pygame.image.load(mapping[idmap])
bg2 = pygame.image.load(mapping[idmap])
bgblood = pygame.image.load('sprite/forestblood.jpg')
bgfirstaid = pygame.image.load('sprite/firstaidroom.jpg')
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

X, Y, vel, WALK_AVI, CHECK = 508-70, 598-45-30, 15, 0, 'UP'

inventory = []
applescrap = pygame.image.load('sprite/map/applescrap.png')
applescrap_s = pygame.image.load('sprite/map/applescrap_s.png')
magicpowder = pygame.image.load('sprite/map/magicpowder.png')
magicpowder_s = pygame.image.load('sprite/map/magicpowder_s.png')
puzzlepaper = pygame.image.load('sprite/map/puzzlepaper.png')
puzzlepaper_s = pygame.image.load('sprite/map/puzzlepaper_s.png')
potion = pygame.image.load('sprite/map/potion.png')
potion_s = pygame.image.load('sprite/map/potion_s.png')

mainClock = pygame.time.Clock()

run = True
PLAY_FRONT, PLAY_MAIN, PLAY_PH1, PLAY_PH2, PLAY_PH3 = False, True, False, False, False
PLAY_BROOM = False
LEFT, RIGHT = False, False
DOWN, UP = False, False
RULE = False

#----------------Sound--------------------------------
bg_hall = pygame.mixer.Sound("sound/178.mp3"); bg_hall.set_volume(0.0)
bg_opendoor = pygame.mixer.Sound("sound\Wood Door - Open_Close.mp3")

#--------------------------------------------
walls = open("walls.txt", 'r').read()
walls = dict(json.loads(walls))
BLACK = 0
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
ven_walkr, ven_walkl = readvar('var.txt', 'veneno/walkr'), readvar('var.txt', 'veneno/walkl')

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

POSX_AVI, POSY_AVI = -300, 0
POSX_ESME, POSY_ESME = -150, 0
POSX_SHE, POSY_SHE = 300, 0
POSX_VEN, POSY_VEN = 0, 0

# #---------------------------------------------------------------------------
def fadescreen(): 
    fade = pygame.Surface((1280, 720))
    fade.fill((0,0,0))
    for alpha in range(0, 150):
        fade.set_alpha(alpha)
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
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
    pygame.draw.rect(win, (0), [0, 720-BLACK, 1280, 100])

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
            PLAY_MAIN = True
            fadein(bg, -508, -272)
            FRONTANIM = False
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
scrollpaper = readvar('var.txt', 'scrollpaper')
fontrule = pygame.font.Font('sprite/Tangerine-Bold.ttf', 72)
fontpaper = pygame.font.Font('sprite/Tangerine-Bold.ttf', 48)
ruleph = ['You have 60 seconds to find different items', 'and you can miss 3 time.']
posx = 0
def redrawrule(game):
    """ blit rule """
    global ANIM, counttxt, countd, posx
    if ANIM+1 >= 15:
        ANIM = 14
    win.blit(scrollpaper[ANIM], (640-(scrollpaper[ANIM].get_rect().size[0]/2), 0))
    message = fontrule.render('Rule', True, (0, 0, 0))
    if game == 'Photohunt' and 'photohunt' not in inventory and ANIM == 14:
        if counttxt <= 3:
            txt = fontrule.render('Rule'[counttxt], True, (0, 0, 0))
            posx += txt.get_rect().size[0]
            scrollpaper[14].blit(txt, (posx, 150))
            counttxt += 1
    else:
        posx = 640-(message.get_rect().size[0]/2)
    ANIM += 1
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
def fadein(backg, posx, posy):
    """ fade in screen """
    global PLAY_MAIN, play_cutscene
    fade = pygame.Surface((1280, 720))
    fade.fill((0,0,0))
    for alpha in range(150, 0, -1):
        fade.set_alpha(alpha)
        win.blit(backg, (posx, posy))
        if PLAY_MAIN and not play_cutscene:
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
dia_ven = pygame.image.load('sprite/veneno/veneno.png')
esme_sleep = pygame.image.load('sprite/esme/sleep.png')
font = pygame.font.Font('sprite/alagard.ttf', 21)
bubble = readvar('var.txt', 'bubble')
explosion = readvar('var.txt', 'explosion')
sad, upset, shock = readvar('var.txt', 'sad'), readvar('var.txt', 'upset'), readvar('var.txt', 'shock')
sad, upset, shock = bubble+sad+sad, bubble+upset+upset, bubble+shock+shock
ANIMB = 0

play_dialog = False
nextdia = False
posx_txt = 205
posy_txt = 80
counttxt = 0
countd = 0
checkpoint = 1

play_cutscene = False
STORY1, STORY2, STORY3 = True, False, False

WALK_ESME, WALK_SHE, WALK_VEN = 0, 0, 0

def redrawdialog(countd):
    """ blit dialog """
    global ANIM, counttxt
    global posx_txt, posy_txt
    if ANIM >= 10:
        ANIM = 9
    win.blit(dialogbox[ANIM], ((1280/2)-(dialogbox[ANIM].get_rect().size[0]/2), 450))
    if ANIM == 9:
        if lstdialog[countd].split()[0] == 'Veneno':
            win.blit(dia_ven, (141.5, 450))
        if lstdialog[countd].split()[0] == 'Sheree':
            win.blit(dia_she, (141.5, 450))
        if lstdialog[countd].split()[0] == 'Esme':
            win.blit(dia_esme, (141.5, 450))
        if lstdialog[countd].split()[0] == 'Avilia':
            win.blit(dia_avi, (141.5, 450))
        if counttxt <= len(lstdialog[countd].split(' : ')[1])-1:
            message = font.render(lstdialog[countd].split(' : ')[1][counttxt], True, (0, 0, 0))
            dialogbox[9].blit(message, (posx_txt, posy_txt))
            posx_txt += message.get_rect().size[0]+0.5
        if posx_txt >= 950:
            posx_txt, posy_txt = 205, 120
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

def aviwalk(way, stop):
    global WALK_AVI, POSX_AVI, POSY_AVI
    if WALK_AVI+1 >= 9:
        WALK_AVI = 0
    if way == 'right':
        if POSX_AVI != stop:
            POSX_AVI += 5
            WALK_AVI += 1
        win.blit(avilia_walkr[WALK_AVI], (POSX_AVI, POSY_AVI))
    if way == 'left':
        if POSX_AVI != stop:
            POSX_AVI -= 5
            WALK_AVI += 1
        win.blit(avilia_walkl[WALK_AVI], (POSX_AVI, POSY_AVI))
    if way == 'up':
        if POSY_AVI != stop:
            POSY_AVI -= 5
            WALK_AVI += 1
        win.blit(avilia_walku[WALK_AVI], (POSX_AVI, POSY_AVI))

def shewalk(way, stop):
    global WALK_SHE, POSX_SHE, POSY_SHE
    if WALK_SHE+1 >= 9:
        WALK_SHE = 0
    if way == 'right':
        if POSX_SHE != stop:
            POSX_SHE += 5
            WALK_SHE += 1
        win.blit(she_walkr[WALK_SHE], (POSX_SHE, POSY_SHE))
    if way == 'left':
        if POSX_SHE != stop:
            POSX_SHE -= 5
            WALK_SHE += 1
        win.blit(she_walkl[WALK_SHE], (POSX_SHE, POSY_SHE))

def esmewalk(way, stop):
    global WALK_ESME, POSX_ESME, POSY_ESME
    if WALK_ESME+1 >= 9:
        WALK_ESME = 0
    if way == 'right':
        if POSX_ESME != stop:
            POSX_ESME += 5
            WALK_ESME += 1
        win.blit(esme_walkr[WALK_ESME], (POSX_ESME, POSY_ESME))
    if way == 'left':
        if POSX_ESME != stop:
            POSX_ESME -= 5
            WALK_ESME += 1
        win.blit(esme_walkl[WALK_ESME], (POSX_ESME, POSY_ESME))

def venwalk(way, stop):
    global WALK_VEN, POSX_VEN, POSY_VEN
    if WALK_VEN+1 >= 9:
        WALK_VEN = 0
    if way == 'right':
        if POSX_VEN != stop:
            POSX_VEN += 5
            WALK_VEN += 1
        win.blit(ven_walkr[WALK_VEN], (POSX_VEN, POSY_VEN))
    if way == 'left':
        if POSX_VEN != stop:
            POSX_VEN -= 5
            WALK_VEN += 1
        win.blit(ven_walkr[WALK_VEN], (POSX_VEN, POSY_VEN))

def shebroom(way, stop):
    global WALK_SHE, POSX_SHE, POSY_SHE
    if WALK_SHE+1 >= 17: WALK_SHE = 0
    she_copy = sheree_b[WALK_SHE].copy()
    she_copy = pygame.transform.scale(she_copy, (135, 135))
    if way == 'left':
        win.blit(pygame.transform.flip(she_copy, True, False), (POSX_SHE-50, POSY_SHE))
        if POSX_SHE != stop:
            POSX_SHE -= 10
    WALK_SHE += 1

def avibroom(way, stop):
    global WALK_AVI, POSX_AVI, POSY_AVI, countd
    if WALK_AVI+1 >= 17: WALK_AVI = 0
    avi_copy = avilia_b[WALK_AVI].copy()
    avi_copy = pygame.transform.scale(avi_copy, (135, 135))
    if way == 'left':
        win.blit(pygame.transform.flip(avi_copy, True, False), (POSX_AVI-50, POSY_AVI))
        if POSX_AVI != stop:
            POSX_AVI -= 10
    if way == 'right':
        win.blit(avi_copy, (POSX_AVI-50, POSY_AVI))
        if POSX_AVI != stop:
            POSX_AVI += 10
            if countd in [36]:
                POSY_AVI += 11
    WALK_AVI += 1
    
def esmebroom(way, stop):
    global WALK_ESME, POSX_ESME, POSY_ESME
    if WALK_ESME+1 >= 17: WALK_ESME = 0
    esme_copy = esme_b[WALK_ESME].copy()
    esme_copy = pygame.transform.scale(esme_copy, (135, 135))
    if way == 'left':
        win.blit(pygame.transform.flip(esme_copy, True, False), (POSX_ESME-50, POSY_ESME))
        if POSX_ESME != stop:
            POSX_ESME -= 10
    if way == 'right':
        win.blit(esme_copy, (POSX_ESME-50, POSY_ESME))
        if POSX_ESME != stop:
            POSX_ESME += 10
    WALK_ESME += 1

def redrawbubble(emo, posx, posy):
    """ blit bubble emo """
    global ANIMB
    if emo == 'sad':
        win.blit(sad[ANIMB], (posx, posy))
    if emo == 'upset':
        win.blit(upset[ANIMB], (posx, posy))
    if emo == 'shock':
        win.blit(shock[ANIMB], (posx, posy))
    ANIMB += 1

def redrawblack():
    """ blit black """
    global BLACK
    pygame.draw.rect(win, (0), [0, 0, 1280, BLACK])
    pygame.draw.rect(win, (0), [0, 722-BLACK, 1280, 100])

def cutscene():
    """ blit cutscene """
    global STORY1, STORY2, STORY3, play_dialog, play_cutscene
    global ANIM, ANIMB, checkpoint
    global countd, counttxt, posx_txt, posy_txt, nextdia
    global POSX_ESME, POSY_ESME, WALK_ESME
    global POSX_SHE, POSY_SHE, WALK_SHE
    global POSX_AVI, POSY_AVI, WALK_AVI
    if STORY1:
        if lstdialog[countd].split()[0] == 'End':
            play_dialog, STORY1 = False, False
        if countd in [0, 1, 2, 3, 4, 5, 6]: aviwalk('left', 1095)
        if countd in [0, 1]:
            esmewalk('right', 750)
            shewalk('right', 600)
            if POSX_ESME == 750: play_dialog = True
        if countd in [2]:
            esmewalk('left', 750)
            shewalk('right', 600)
        if countd in [3]:
            if counttxt in range(40, 60):
                redrawbubble('sad', POSX_ESME+2, POSY_ESME-40)
            else: ANIMB = 0
            if POSX_SHE == 680:
                shepush()
                if counttxt >= 80:
                    posx_apple, posy_apple = POSX_ESME-25, POSY_ESME+60
                    win.blit(apple, (posx_apple, posy_apple))
                    esmefail('down')
                else: esmewalk('left', 750)
            elif counttxt >= 59:
                esmewalk('left', 750)
                shewalk('right', 680)
            else:
                esmewalk('left', 750)
                shewalk('right', 600)
        if countd in [4, 5, 6, 7, 8, 9, 10]:
            if counttxt in range(0, 20) and countd in [4]:
                win.blit(apple, (POSX_ESME-25-(counttxt*2), POSY_ESME+60-counttxt))
            shewalk('right', 680)
            esmefail('down')
        if countd in range(7, 27):
            aviwalk('left', 810)
            esmefail('up')
        if countd in [11]:
            if counttxt in range(0, 20):
                redrawbubble('upset', POSX_SHE+2, POSY_SHE-40)
            else: ANIMB = 0
            shewalk('left', 630)
        if countd in range(12, 16):
            shewalk('right', 630)
        if countd in [16]:
            if counttxt in range(33, 44):
                redrawbubble('shock', POSX_ESME+2, POSY_ESME-40)
                redrawbubble('shock', POSX_AVI+20, POSY_AVI-40)
            if counttxt >= 32:
                shebroom('left', -100)
                POSY_SHE -= 2.5
            else:
                ANIMB = 0
                shewalk('right', 630)
    elif STORY2:
        if lstdialog[countd].split()[0] == 'End':
            play_dialog, STORY2 = False, False
        if countd in [28] and POSX_AVI == 200: play_dialog = True
        if countd in range(28, 35):
            avibroom('right', 200)
            shewalk('left', 750)
            esmewalk('right', 500)
        else: ANIMB = 0
        if countd in [32] and counttxt in range(50, 70) and ANIMB < 32:
            redrawbubble('shock', POSX_ESME+2, POSY_ESME-40)
            redrawbubble('shock', POSX_AVI+2, POSY_AVI-40)
        if countd in [35]:
            if counttxt in range(0, 20):
                shewalk('left', 750)
                esmewalk('right', 500)
                win.blit(apple, (POSX_SHE-25+(counttxt), POSY_SHE+30))
            if counttxt in range(20, 47):
                win.blit(explosion[counttxt-20], (POSX_SHE-180, POSY_SHE-150))
            if counttxt >= 20:
                esmefail('down')
            avibroom('right', 200)
        if countd in range(36, 45):
            esmefail('down')
            if countd >= 38:
                aviwalk('right', 400)
                POSY_AVI = 380
            else: avibroom('right', 400)
            if countd >= 39: venwalk('right', 350)
    elif STORY3:
        if lstdialog[countd].split()[0] == 'End':
            play_dialo, STORY3, countd = False, False, 0
        win.blit(esme_sleep, (106, 218))
        if countd >= 45 and POSX_AVI == 150 and POSY_AVI == 220:
            aviwalk('left', 150)
            play_dialog = True
        elif countd == 45 and not play_dialog and POSX_AVI == 150:
            aviwalk('up', 220)
        elif countd == 45 and not play_dialog and POSY_AVI == 325:
            aviwalk('left', 150)
        elif countd == 45 and not play_dialog and POSX_AVI == 270:
            aviwalk('up', 325)
        elif countd == 45 and not play_dialog and POSY_AVI == 460:
            aviwalk('left', 270)
        elif countd == 45 and not play_dialog:
            aviwalk('up', 460)
    if play_dialog:
        redrawdialog(countd)
    if keys[pygame.K_SPACE] and play_dialog and counttxt >= len(lstdialog[countd].split(':')[1])-1:
        if countd in [3] and counttxt >= 90:
            nextdia = True
        if countd in [7] and counttxt >= 50:
            nextdia = True
        if countd in [11] and counttxt >= 25:
            nextdia = True
        if countd in [16] and counttxt >= 105:
            nextdia = True
        if countd in [35] and counttxt >= 50:
            nextdia = True
        elif countd not in [3, 7, 11, 16, 35]:
            nextdia = True
    elif nextdia:
        if not keys[pygame.K_SPACE]:
            countd += 1
            if lstdialog[countd-1].split()[0] != lstdialog[countd].split()[0]: ANIM = 0
            counttxt, posx_txt, posy_txt = 0, 205, 80
            dialogbox[9] = pygame.image.load('sprite/dialogbox10.png')
            nextdia = False
    print('counttxt', counttxt, countd)
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
#----------------------------------------------------------------------------
def wall(wall=[(0,0,0,0)]):
    """wall"""
    global rel_x
    global rel_y
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
        print(i,j,k,l)
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
        print(i,j,k,l)
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
        print(i,j,k,l)
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
        print(i,j,k,l)
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
    rel_x = -X % bg_width
    rel_y = -Y % bg_height

#-----------------------------------------------------------------------
change = False

def changemap(l, r, u, d, nx, ny, idmapold, idmapnew, change):
    global X
    global Y
    global bg
    global bg2
    if change:
        return idmapold, change
    change = False
    if l <= X <= r and u <= Y <= d:
        bg = pygame.image.load(mapping[str(idmapnew)])
        bg2 = pygame.image.load(mapping[str(idmapnew)])
        X = nx
        Y = ny
        change = True
        return idmapnew, change
    return idmapold, change
        

class sup:
    def __init__(self, name, posx, posy):
        self.name = readvar('support.txt', name)
        self.count = 0
        self.sub_l = True
        self.sub_r = False
        self.sub_u = True
        self.sub_d = False
        self.posx = posx
        self.posy = posy

    def standr(self):
        bg.blit(self.name[0], (self.posx, self.posy))

    def standl(self):
        bg.blit(self.name[1], (self.posx, self.posy))
    
    def standu(self):
        bg.blit(self.name[2], (self.posx, self.posy))
    
    def standd(self):
        bg.blit(self.name[3], (self.posx, self.posy))

    def walkrl(self, turnl, turnr):
        if self.sub_l:
            if self.count+1 >= 9:
                self.count = 0
            self.posx -= 7.5
            bg.blit(self.name[self.count], (self.posx, self.posy))
        if self.posx <= turnl:
            self.count = 9
            self.sub_l = False
            self.sub_r = True
        if self.sub_r:
            if self.count+1 >= 19:
                self.count = 9
            self.posx += 7.5
            bg.blit(self.name[self.count], (self.posx, self.posy))
        if self.posx >= turnr:
            self.sub_l = True
            self.sub_r = False
        self.count += 1

    def walkud(self, turnu, turnd):
        if self.sub_u:
            if self.count+1 >= 9:
                self.count = 0
            self.posy -= 7.5
            bg.blit(self.name[self.count], (self.posx, self.posy))
        if self.posy <= turnu:
            self.count = 9
            self.sub_u = False
            self.sub_d = True
        if self.sub_d:
            if self.count+1 >= 19:
                self.count = 9
            self.posx += 7.5
            bg.blit(self.name[self.count], (self.posx, self.posy))
        if self.posy >= turnd:
            self.sub_u = True
            self.sub_d = False
        self.count += 1

#---------------------------sup----------------------------------------------

# sup07 = sup("sub07", 958, 237)

#---------------------------------------------------------------------------
# sup07 = readvar('support.txt', 'sub07')

# SUP_POS_X = 958
# SUP_POS_Y = 237
# SUPCOUNT = 0

# SUP_L = True
# SUP_R = False
# def redrawsup():
#     """blit support character"""
#     global bg
#     global SUP_POS_X
#     global SUP_POS_Y
#     global SUPCOUNT
#     global SUP_L
#     global SUP_R

#     if SUP_L:
#         if SUPCOUNT + 1 >= 9:
#             SUPCOUNT = 0
#         SUP_POS_X -= 7.5
#         bg.blit(sup07[SUPCOUNT], (SUP_POS_X, SUP_POS_Y))
#     if SUP_POS_X == 58.0:
#         SUPCOUNT = 9
#         SUP_L = False
#         SUP_R = True
#     if SUP_R:
#         if SUPCOUNT + 1 >= 19:
#             SUPCOUNT = 9
#         SUP_POS_X += 7.5
#         bg.blit(sup07[SUPCOUNT], (SUP_POS_X, SUP_POS_Y))
#     if SUP_POS_X == 965.5:
#         SUP_R = False
#         SUP_L = True
#     SUPCOUNT += 1
#---------------------------------------------------------------------------


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
WALKCOUNT = 0

correctImg = readvar('photohunt.txt', 'circle')

def drawcorrect(posx, posy):
    global WALKCOUNT
    if WALKCOUNT > len(correctImg)-1:
        win.blit(correctImg[len(correctImg)-1], (posx, posy))
    else:
        win.blit(correctImg[WALKCOUNT], (posx, posy))
    WALKCOUNT += 1

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

#------------Broom Game-------------
bg_b1 = pygame.image.load("sprite/racing/bg/mountain.png").convert()
bg_b2 = pygame.image.load("sprite/racing/bg/forest1.jpg").convert()
bg_b3 = pygame.image.load("sprite/racing/bg/library.jpg").convert()
bg_b4 = pygame.image.load("sprite/racing/bg/forest1.jpg").convert()

bg_scrolling_b = 0

def redrawbroomGameWindow():
    global broomcount
    
    if broomcount + 1 >= 44: #กัน out of range
        broomcount = 0

    if rightb:
        win.blit(broomright[broomcount], (xb, yb))
        broomcount += 1

    else:
        win.blit(nobroom[broomcount], (xb, yb))
        broomcount += 1
    pygame.display.update()

class mon:
    def __init__(self, posx, posy, monster):
        self.posx = posx
        self.posy = posy
        self.monster = monster
        self.moncount = 0
        self.crash = 0
        self.pas = False

    def spawn(self, sec, speedx, speedy, bounce=False):
        global xb
        global yb
        global heartb
        global cooldownb
        global hplay
        global wplay

        if timeb >= sec:

            if self.moncount + 1 >= len(self.monster):
                self.moncount = 0
            wmon, hmon = self.monster[self.moncount].get_rect().size
            # print(wmon, hmon)
            if yb < self.posy < yb+hplay-80 and xb < self.posx < xb+wplay-80 and cooldownb > 2:
                heartb -= 1
                cooldownb = 0
            # if self.posy-180 < y < self.posy-10 and self.posx-100 < x < self.posx-50 and cooldown > 2:
            #     heart -= 1
            #     cooldown = 0

            win.blit(self.monster[self.moncount], (self.posx, self.posy))
            self.moncount += 1

            if bounce:
                if self.posy <= 0:
                    self.pas = True
                elif self.posy > 720:
                    self.pas = False
                if self.posy < 0 or self.pas:
                    self.posy += speedy
                else:
                    self.posy -= speedy
                self.posx -= speedx
            else:
                self.posx -= speedx
                self.posy += speedy

broomright, nobroom = readvar('broomgame.txt', 'racing/broom'), readvar('broomgame.txt', 'racing/broom')

heartimg = pygame.image.load('sprite/racing/broom/heart.png')

clock = readvar('broomgame.txt', 'clocktower/clock')
bird = readvar('broomgame.txt', 'bird')
bluebook, purbook, redbook = readvar('broomgame.txt', 'bluebook'), readvar('broomgame.txt', 'purbook'), readvar('broomgame.txt', 'redbook')

#----------------------------------------------------------- stage 1 ----------------------------------------------------------------
bird1 = mon(1280,320,bird); bird8 = mon(1280,190,bird); bird15 = mon(1280,90,bird); bird22 = mon(1280,290,bird)
bird2 = mon(1280,100,bird); bird9 = mon(1280,290,bird); bird16 = mon(1280,450,bird)
bird3 = mon(1280,500,bird); bird10 = mon(1280,480,bird); bird17 = mon(1280,310,bird)
bird4 = mon(1280,450,bird); bird11 = mon(1280,310,bird); bird18 = mon(1280,70,bird)
bird5 = mon(1280,350,bird); bird12 = mon(1280,310,bird); bird19 = mon(1280,150,bird)
bird6 = mon(1280,100,bird); bird13 = mon(1280,310,bird); bird20 = mon(1280,500,bird)
bird7 = mon(1280,400,bird); bird14 = mon(1280,20,bird); bird21 = mon(1280,70,bird)
#--------------------------------------------------------- bounce ------------------------------------------------------------
bird_1b = mon(1280,0,bird)
bird_2b = mon(1280,720,bird)
bird_3b = mon(1280,0,bird)
bird_4b = mon(1280,720,bird)
bird_5b = mon(1280,0,bird)
#--------------------------------------------------------- disco ------------------------------------------------------------
bird01 = mon(1280,10,bird)
bird02 = mon(1280,610,bird)
bird03 = mon(1280,310,bird)
bird04 = mon(1280,90,bird)
bird05 = mon(1280,10,bird)
bird06 = mon(1280,10,bird)
bird07 = mon(1280,80,bird)
bird08 = mon(1280,610,bird)
bird09 = mon(1280,90,bird)
#----------------------------------------------------------- stage 2 ----------------------------------------------------------------
clock1 = mon(1280,310,clock)
clock2 = mon(1280,220,clock)
clock3 = mon(1280,70,clock)
clock4 = mon(1280,160,clock)
clock5 = mon(1280,370,clock)
clock6 = mon(1280,600,clock)
clock7 = mon(1280,130,clock)
clock8 = mon(1280,130,clock)
clock9 = mon(1280,340,clock)
clock10 = mon(1280,250,clock)
clock11 = mon(1280,438,clock)
clock12 = mon(1280,50,clock)
clock13 = mon(1280,150,clock)

clock14 = mon(1280,310,clock)
clock15 = mon(1280,600,clock)
clock16 = mon(1280,510,clock)
clock17 = mon(1280,84,clock)
clock18 = mon(1280,182,clock)

clock19 = mon(70,720,clock)
clock20 = mon(1190,0,clock)
clock21 = mon(70,720,clock)
clock22 = mon(1190,0,clock)
clock23 = mon(70,720,clock)
clock24 = mon(1190,0,clock)
clock25 = mon(70,720,clock)
clock26 = mon(1190,0,clock)

clock27 = mon(1280,26,clock)
clock28 = mon(1280,639,clock)
clock29 = mon(1280,0,clock)
#--------------------------------------------------------- bounce ------------------------------------------------------------
clock1b = mon(1280,0,clock)
clock2b = mon(1280,720,clock)
clock3b = mon(1280,0,clock)
clock4b = mon(1280,720,clock)
clock5b = mon(1280,0,clock)
clock6b = mon(1280,720,clock)
clock7b = mon(1280,0,clock)
clock8b = mon(1280,720,clock)
clock9b = mon(1280,0,clock)
clock10b = mon(1280,720,clock)

clock11b = mon(1280,0,clock)
clock12b = mon(0,207,clock)
clock13b = mon(1280,234,clock)
clock14b = mon(0,452,clock)
clock15b = mon(1280,310,clock)
clock16b = mon(0,100,clock)
clock17b = mon(1280,720,clock)
clock18b = mon(0,0,clock)
# #--------------------------------------------------------- disco ------------------------------------------------------------
clock01 = mon(1280,386,clock)
clock02 = mon(1280,50,clock)
clock03 = mon(1280,310,clock)
clock04 = mon(1280,40,clock)
clock05 = mon(1280,611,clock)
# ----------------------------------------------------------- stage 3 ----------------------------------------------------------------
bluebook1 = mon(1280, 260, bluebook); bluebook2 = mon(1280, 260, bluebook); bluebook3 = mon(1280, 260, bluebook)
bluebook4 = mon(1280, 260, bluebook); bluebook5 = mon(1280, 260, bluebook); bluebook6 = mon(1280, 260, bluebook)
bluebook7 = mon(1280, 260, bluebook); bluebook8 = mon(1280, 100, bluebook); bluebook9 = mon(1280, 100, bluebook)
bluebook10 = mon(1280, 100, bluebook); bluebook11 = mon(1280, 100, bluebook); bluebook12 = mon(1280, 100, bluebook)
bluebook13 = mon(1280, 100, bluebook); bluebook14 = mon(1280, 100, bluebook); bluebook15 = mon(1280, 180, bluebook)
bluebook16 = mon(1280, 180, bluebook); bluebook17 = mon(1280, 180, bluebook); bluebook18 = mon(1280, 180, bluebook)
redbook1 = mon(1280, 400, redbook); redbook2 = mon(1280, 400, redbook); redbook3 = mon(1280, 400, redbook)
redbook4 = mon(1280, 480, redbook); redbook5 = mon(1280, 480, redbook); redbook6 = mon(1280, 480, redbook)
redbook7 = mon(1280, 480, redbook); redbook8 = mon(1280, 480, redbook); redbook9 = mon(1280, 560, redbook)
redbook10 = mon(1280, 560, redbook); redbook11 = mon(1280, 560, redbook); redbook12 = mon(1280, 560, redbook)
redbook13 = mon(1280, 560, redbook); redbook14 = mon(1280, 640, redbook); redbook15 = mon(1280, 640, redbook); redbook16 = mon(1280, 640, redbook)
purbook1 = mon(-10, 360, purbook); purbook2 = mon(-10, 360, purbook)
# #--------------------------------------------------------- bounce ------------------------------------------------------------
bluebook_1b = mon(1280,0,bluebook)
bluebook_2b = mon(1280,720,bluebook)
bluebook_3b = mon(1280,0,bluebook)
bluebook_4b = mon(1280,720,bluebook)
bluebook_5b = mon(1280,0,bluebook)
bluebook_6b = mon(1280,720,bluebook)
bluebook_7b = mon(1280,0,bluebook)
bluebook_8b = mon(1280,720,bluebook)
bluebook_9b = mon(1280,0,bluebook)
bluebook_10b = mon(1280,720,bluebook)
bluebook_11b = mon(1280,0,bluebook)
bluebook_12b = mon(1280,720,bluebook)
bluebook_13b = mon(1280,0,bluebook)
bluebook_14b = mon(1280,720,bluebook)
bluebook_15b = mon(1280,0,bluebook)
bluebook_16b = mon(1280,720,bluebook)
bluebook_17b = mon(1280,0,bluebook)
bluebook_18b = mon(1280,720,bluebook)
# #--------------------------------------------------------- disco -------------------------------------------------------------
bluebook01 = mon(1280,50,bluebook)
bluebook02 = mon(1280,50,bluebook)
bluebook03 = mon(1280,550,bluebook)
bluebook04 = mon(1280,100,bluebook)

#-----------------music-------------------------------


#-----------------------------------------------------------------
xb = 50
yb = 355
velb = 30
leftb = False
rightb = False
broomcount = 0
check = ''
timeb = 0
heartb = 5
cooldownb = 0

hplay, wplay = broomright[broomcount].get_rect().size

fadebg2 = False
fadebg3 = False
#---------------------------------------------------------------------------
"""mainloop"""
while run:
    # pygame.time.delay(30)
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
    #--------------hallway-01--------------
        if idmap == "01": #HALLWAY
            # redrawsup()
            bg_hall.play(-1,fade_ms=5000)
            wall(walls["hallway"])
            # sup07.walkrl(58, 965)
            idmap, change = changemap(0, 1280, 598, 720, 508, 43, idmap, "00", change)
            idmap, change = changemap(0, 13, 328, 388, 1123, 343, idmap, "11", change)
            idmap, change = changemap(0, 1280, 0, 13, X, 583, idmap, "09", change)
            idmap, change = changemap(1198, 1280, 0, 720, 33, 163, idmap, "02", change)

            if not change:
                if X >= 628:
                    win.blit(bg ,(-628, rel_y-bg_height))
                elif Y >= 358:
                    win.blit(bg ,(rel_x-bg_width, -358))
                else:
                    win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
                bg.blit(bg2 ,(0, 0))
            change = False
    #--------------canteen-02--------------
        elif idmap == "02": #CANTEEN
            wall(walls["canteen"])
            bg_hall.stop()
            if X >= 1203:
                X = 28
                Y = 463
                stage_height = 720
                bg = pygame.image.load("sprite/eastcorridor_1.jpg")
                bg2 = pygame.image.load("sprite/eastcorridor_1.jpg")
                idmap = "03"
            elif Y >= 778 and Y <= 838 and X >= 828:
                X = 28
                Y = 223
                stage_height = 720
                bg = pygame.image.load("sprite/eastgarden.jpg")
                bg2 = pygame.image.load("sprite/eastgarden.jpg")
                idmap = "08"
            elif X <= 13 and Y >= 148 and Y <= 163:
                X = 1168
                Y = 238
                stage_height = 720
                bg = pygame.image.load("sprite/hallway.jpg")
                bg2 = pygame.image.load("sprite/hallway.jpg")
                idmap = "01"
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
    #--------------eastcor1-03-------------
        elif idmap == "03":
            wall(walls["eastcor1"])
            idmap, change = changemap(0,13,0,720,1108,478,idmap,"02", change)
            idmap, change = changemap(0,1280,0,13,X,583,idmap,"04", change)
            idmap, change = changemap(0,1280,628,1280,388,28,idmap,"08", change)
            if not change:
                if Y >= 178:
                    win.blit(bg ,(-28, -178))
                else:
                    win.blit(bg ,(-28, rel_y-bg_height))
            if 1138 <= X <= 1198 and 463 <= Y < 523:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_hall.stop()
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/classroom.jpg")
                    X = 58
                    Y = 268
                    idmap = "05"
                    CHECK = "RIGHT"
            if 1138 <= X <= 1198 and 103 <= Y < 148:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_hall.stop()
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/classroom.jpg")
                    X = 58
                    Y = 268
                    idmap = "06"
                    CHECK = "RIGHT"
            change = False
    #--------------eastcor2-04-------------
        elif idmap == "04":
            wall(walls["eastcor2"])
            idmap, change = changemap(0,1280,632,1280,X,28,idmap,"03", change)
            idmap, change = changemap(0,13,0,720,1123,343,idmap,"10", change)
            idmap, change = changemap(0,1280,0,13,1123,613,idmap,"19", change)
            if not change:
                win.blit(bg ,(-28, -13))
            if 1138 <= X <= 1198 and 328 <= Y <= 373:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_hall.stop()
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/classroom.jpg")
                    X = 58
                    Y = 268
                    idmap = "07"
                    CHECK = "RIGHT"
            change = False
    #--------------classroom-05------------
        elif idmap == "05":
            wall(walls["classroom"])

            win.blit(bg ,(-238, -118))
            if 13 <= X <= 28 and 253 <= Y < 283:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/eastcorridor_1.jpg")
                    X = 1093
                    Y = 493
                    idmap = "03"
                    CHECK = "LEFT"
                    bg_hall.play(-1,fade_ms=5000)
    #--------------classroom2-06-------------
        elif idmap == "06":
            wall(walls["classroom"])

            win.blit(bg ,(-238, -118))
            if 13 <= X <= 28 and 253 <= Y < 283:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/eastcorridor_1.jpg")
                    X = 1093
                    Y = 133
                    idmap = "03"
                    CHECK = "LEFT"
                    bg_hall.play(-1,fade_ms=5000)
    #--------------classroom3-07-------------
        elif idmap == '07':
            wall(walls["classroom"])

            win.blit(bg ,(-238, -118))
            if 13 <= X <= 28 and 253 <= Y < 283:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/eastcorridor_2.jpg")
                    X = 1093
                    Y = 358
                    idmap = "04"
                    CHECK = "LEFT"
                    bg_hall.play(-1,fade_ms=5000)
    #--------------eastgarden-08-----------
        elif idmap == "08":
            wall(walls["eastgar"])
            if X <= 13:
                bg = pygame.image.load("sprite/canteen.jpg")
                stage_height = 950
                X = 813
                Y = 823
                idmap = "02"
            elif Y <= 13:
                bg = pygame.image.load("sprite/eastcorridor_1.jpg")
                X = 433
                Y = 613
                idmap = "03"
            else:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
    #--------------firstaid-09-------------
        elif idmap == "09": #FIRSTAID ROOM
            wall(walls["firstaid"])
            idmap,change = changemap(0,1280,613,1280,253,43,idmap,"01", change)
            idmap,change = changemap(1207,1280,0,720,28,373,idmap,"10", change)
            if not change:
                if play_cutscene:
                    win.blit(bg, (-13, -13))
                elif Y >= 13 and X >= 703:
                    win.blit(bg ,(-703, -13))
                elif Y >= 13:
                    win.blit(bg ,(rel_x-bg_width, -13))
                elif X >= 703:
                    win.blit(bg ,(-703, rel_y-bg_height))
                else:
                    win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
            change = False
            if not STORY3:
                if BLACK > 0:
                    BLACK -= 4
                if BLACK <= 0 and checkpoint == 3:
                    checkpoint, CHECK = 4, 'DOWN'
                    fadeout()
                    fadein(bg, -28, -13)
                    play_cutscene = False
                    X, Y = 28, 343
                redrawblack()
            if STORY3:
                if BLACK < 100:
                    BLACK += 4
                redrawblack()
                cutscene()
    #---------------battle-10--------------
        elif idmap == "10": #BATTLE ROOM
            wall(walls["battle"])
            idmap, change = changemap(0,13,0,720,1168,493,idmap,"09", change)
            idmap,change = changemap(1222,1280,0,720,28,373,idmap,"04", change)
            if not change:
                if X >= 523 and Y >= 103:
                    win.blit(bg ,(-523, -103))
                elif Y >= 103:
                    win.blit(bg ,(rel_x-bg_width, -103))
                elif X >= 523:
                    win.blit(bg ,(-523, -103))
                else:
                    win.blit(bg ,(rel_x-bg_width, -103))
            change = False
    #----------------path-11---------------
        elif idmap == "11":
            wall(walls["path"])
            idmap, change = changemap(1168,1280,0,720,28,358,idmap,"01", change)
            idmap, change = changemap(0,13,0,720,1183,373,idmap,"15", change)
            idmap, change = changemap(0,1280,0,13,433,553,idmap,"12", change)
            if not STORY1:
                if BLACK > 0:
                    BLACK -= 4
                    win.blit(bg ,(-1108, -313))
                    avibroom('left', -100)
                    esmebroom('right', 1380)
                    POSY_AVI -= 2.5
                    POSY_ESME -= 2.5
                if BLACK <= 0 and checkpoint == 1:
                    PLAY_MAIN, PLAY_BROOM, checkpoint = False, True, 2
                    fadeout()
                    fadein(bg_b1, 0, 0)
                redrawblack()
            if STORY1:
                if not play_cutscene:
                    POSX_ESME, POSY_ESME = 300, 343
                    POSX_SHE, POSY_SHE = 150, 343
                    POSX_AVI, POSY_AVI = 1280, 343
                    play_cutscene = True
                    fadeout()
                    fadein(bg, -1108, -313)
                if BLACK < 100:
                    BLACK += 4
                win.blit(bg ,(-1108, -313))
                redrawblack()
                cutscene()
            if not change and not play_cutscene:
                if (X <= 598 and Y >= 313) or (X <= 598 and Y < 313):
                    win.blit(bg ,(-598, -313))
                elif X >= 1108:
                    win.blit(bg ,(-1108, -313))
                elif Y < 313 or Y >= 313:
                    win.blit(bg ,(rel_x-bg_width, -313))
            change = False
    #--------------meeting-12--------------
        elif idmap == "12": #MEETING ROOM
            wall(walls["meeting"])
            idmap, change = changemap(403,448,553,720,733,28,idmap,"11", change)
            if not change:
                if X >= 523 and Y >= 418:
                    win.blit(bg ,(-523, -418))
                elif X >= 523:
                    win.blit(bg ,(-523, rel_y-bg_height))
                elif Y >= 418:
                    win.blit(bg ,(rel_x-bg_width, -418))
                else:
                    win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
            change = False
    #--------------entryhall-00------------
        elif idmap == "00":
            wall(walls["entryhall"])
            idmap, change = changemap(0, 1280, 0, 13, 463, 583, idmap, "01", change)
            idmap, change = changemap(0, 13, 0, 720, 1153, 178, idmap, "13", change)
            if not change:
                if X >= 763 and Y >= 272:
                    win.blit(bg ,(-763, -272))
                elif X >= 763:
                    win.blit(bg ,(-763, rel_y-bg_height))
                elif Y >= 272:
                    win.blit(bg ,(rel_x-bg_width, -272))
                else:
                    win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
            change = False
    #----------------hall-13---------------
        elif idmap == "13":
            wall(walls["hall"])
            idmap, change = changemap(0,13,0,720,1123,223,idmap, "14", change)
            idmap, change = changemap(1207, 1280, 0, 720, 28, 133, idmap, "00", change)
            if not change:
                if X >= 160 and Y >= 287:
                    win.blit(bg ,(-160, -287))
                elif X >= 160:
                    win.blit(bg ,(-160, rel_y-bg_height))
                elif Y >= 287:
                    win.blit(bg ,(rel_x-bg_width, -287))
                else:
                    win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
            change = False
    #-------------westgarden-14------------
        elif idmap == "14":
            wall(walls["westgar"])
            idmap, change = changemap(1207,1280,0,720,73,Y,idmap,"13", change)
            idmap, change = changemap(0,1280,0,13,748,613,idmap,"15", change)
            if not change:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
            change = False
    #--------------westcor1-15-------------
        elif idmap == "15":
            wall(walls["westcor1"])
            idmap, change = changemap(0,1280,628,720,832,28,idmap,"14", change)
            idmap, change = changemap(0,1280,0,13,X,502,idmap,"16", change)
            idmap,change = changemap(1198,1280,0,720,28,343,idmap,"11", change)
            if not change:
                if Y >= 365:
                    win.blit(bg ,(-28, -365))
                else:
                    win.blit(bg ,(-28, rel_y-bg_height))
                if 13 <= X <= 28 and 313 <= Y < 388:
                    win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                    if keys[pygame.K_f]:
                        bg_hall.stop()
                        bg_opendoor.play(maxtime=1400)
                        bg = pygame.image.load("sprite/apothecaryroom.jpg")
                        X = 973
                        Y = 433
                        idmap = "20"
                        CHECK = "LEFT"
                if 13 <= X <= 28 and 103 <= Y < 163:
                    win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                    if keys[pygame.K_f]:
                        bg_hall.stop()
                        bg_opendoor.play(maxtime=1400)
                        bg = pygame.image.load("sprite/teacherroom.jpg")
                        X = 958
                        Y = 373
                        idmap = "21"
                        CHECK = "LEFT"
            change = False
    #--------------westcor2-16-------------
        elif idmap == "16":
            wall(walls["westcor2"])
            idmap ,change = changemap(0,1280,613,720,X,103,idmap,"15", change)
            idmap , change = changemap(0,1280,0,13,43,598,idmap,"17", change)

            if not change:
                if Y >= 73:
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
                        idmap = "22"
                        CHECK = "LEFT"
            change = False
    #-------------westforest-17------------
        elif idmap == "17":
            wall(walls["westfor"])
            idmap ,change = changemap(0,1280,628,720,598,28,idmap,"16", change)
            idmap, change = changemap(1213,1280,0,720,28,418,idmap,"18", change)
            if not change:
                if X >= 583:
                    win.blit(bg ,(-583, -58))
                else:
                    win.blit(bg ,(rel_x-bg_width, -58))
            change = False
    #--------------forest-18---------------
        elif idmap == "18":
            wall(walls["forest"])
            idmap, change = changemap(0,13,0,720,1198,Y,idmap,"17", change)
            idmap, change = changemap(1213,1280,0,720,28,Y,idmap,"19", change)
            if not change:
                if play_cutscene:
                    if countd == 35 and counttxt >= 20:
                        bg = bgblood
                    win.blit(bg, (-283, -358))
                elif X >= 523 and Y >= 425:
                    win.blit(bg ,(-523, -425))
                elif X >= 523:
                    win.blit(bg ,(-523, rel_y-bg_height))
                elif Y >= 425:
                    win.blit(bg ,(rel_x-bg_width, -425))
                else:
                    win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
            change = False
            if not STORY2:
                if BLACK > 0:
                    BLACK -= 4
                    aviwalk('right', 400)
                    venwalk('right', 350)
                    esmefail('down')
                if BLACK <= 0 and checkpoint == 2:
                    fadeout()
                    bg = bgfirstaid
                    STORY3, checkpoint = True, 3
                    idmap, countd, POSX_AVI, POSY_AVI = "09", 45, 530, 620
                    fadein(bg, -13, -13)
                redrawblack()
            if STORY2:
                if BLACK < 100:
                    BLACK += 4
                redrawblack()
                cutscene()
    #-------------eastforest-19-------------
        elif idmap == "19":
            wall(walls["eastfor"])
            idmap ,change = changemap(0,13,0,720,1198,418,idmap,"18", change)
            idmap,change = changemap(0,1280,628,720,598,28,idmap,"04", change)

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
                idmap = "04"
            if not change:
                if X >= 583:
                    win.blit(bg ,(-583, -58))
                else:
                    win.blit(bg ,(rel_x-bg_width, -58))
            change = False
    #------------apothecaryroom-20----------
        elif idmap == "20":
            wall(walls['apothecaryroom'])
            win.blit(bg ,(-238, -58))
            if 1168 <= X <= 1280 and 358 <= Y < 493:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/westcorridor_1.jpg")
                    X = 58
                    Y = 343
                    idmap = "15"
                    CHECK = "RIGHT"
                    bg_hall.play(-1,fade_ms=5000)
            win.fill((0,0,255), rect=[403,580,50,50])
            if 328 <= X <= 448 and 493 <= Y <= 523:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    RULE = True
            if RULE:
                redrawrule('Photohunt')
#                     PLAY_PH1 = True
#                     PLAY_MAIN = False
    #------------teacherroom-21-------------
        elif idmap == "21":
            wall(walls['teacherroom'])
            win.blit(bg ,(-238, -58))
            if 1168 <= X <= 1630 and 358 <= Y < 493:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/westcorridor_1.jpg")
                    X = 58
                    Y = 133
                    idmap = "15"
                    CHECK = "RIGHT"
                    bg_hall.play(-1,fade_ms=5000)
            win.fill((0,0,255), rect=[800,433,50,50])
            if 763 <= X <= 808 and 343 <= Y <= 418:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    PLAY_PH3 = True
                    PLAY_MAIN = False
    #------------researchroom-22------------
        elif idmap == "22":
            wall(walls['researchroom'])

            win.blit(bg ,(-238, -58))
            if 1168 <= X <= 1630 and 358 <= Y < 493:
                win.fill((255,0,0), rect=[X+20,Y-50,50,50])
                if keys[pygame.K_f]:
                    bg_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/westcorridor_2.jpg")
                    X = 58
                    Y = 298
                    idmap = "16"
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
                    print(mx, my)
                    print(health_value)
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
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_1.blit(correctImg[16], (112, 157))
                bg_ph_1.blit(correctImg[16], (712, 157))
                foundph1_1 = 3
        if foundph1_2 == 2: # หนังสือ
            drawcorrect(550, 100)
            drawcorrect(1140, 100)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_1.blit(correctImg[16], (550, 100))
                bg_ph_1.blit(correctImg[16], (1140, 100))
                foundph1_2 = 3
        if foundph1_3 == 2: # อะไรไม่รุข้างหน้าต่าง
            drawcorrect(221, 275)
            drawcorrect(811, 275)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_1.blit(correctImg[16], (221, 275))
                bg_ph_1.blit(correctImg[16], (811, 275))
                foundph1_3 = 3
        if foundph1_4 == 2: # หนังสือชั้น 3
            drawcorrect(550, 285)
            drawcorrect(1140, 285)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_1.blit(correctImg[16], (550, 285))
                bg_ph_1.blit(correctImg[16], (1140, 285))
                foundph1_4 = 3
        if foundph1_5 == 2: # ไม้ไรสักอย่าง
            drawcorrect(95, 450)
            drawcorrect(688, 450)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_1.blit(correctImg[16], (95, 450))
                bg_ph_1.blit(correctImg[16], (688, 450))
                foundph1_5 = 3
        if foundph1_6 == 2: # ถ้วย
            drawcorrect(348, 440)
            drawcorrect(937, 440)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_1.blit(correctImg[16], (348, 440))
                bg_ph_1.blit(correctImg[16], (937, 440))
                foundph1_6 = 3
        if foundph1_7 == 2: # ไห้ไรสักอย่าง
            drawcorrect(640,617)
            drawcorrect(52,617)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
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
                    print(mx, my)
                    print(health_value)
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
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_2.blit(correctImg[16], (536, 425))
                bg_ph_2.blit(correctImg[16], (1158, 425))
                foundph2_1 = 3
        if foundph2_2 == 2: # สามเหลี่ยม
            drawcorrect(226, 461)
            drawcorrect(845, 461)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_2.blit(correctImg[16], (226, 461))
                bg_ph_2.blit(correctImg[16], (845, 461))
                foundph2_2 = 3
        if foundph2_3 == 2: #ไวโอลีน
            drawcorrect(519, 614)
            drawcorrect(1146, 614)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_2.blit(correctImg[16], (519, 614))
                bg_ph_2.blit(correctImg[16], (1146, 614))
                foundph2_3 = 3
        if foundph2_4 == 2: #กระเป๋า
            drawcorrect(68, 491)
            drawcorrect(685, 491)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_2.blit(correctImg[16], (68, 491))
                bg_ph_2.blit(correctImg[16], (685, 491))
                foundph2_4 = 3
        if foundph2_5 == 2: #ลิ้นชัก
            drawcorrect(112, 399)
            drawcorrect(730, 399)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_2.blit(correctImg[16], (112, 399))
                bg_ph_2.blit(correctImg[16], (730, 399))
                foundph2_5 = 3
        if foundph2_6 == 2: #ม้วนกระดาศ
            drawcorrect(402, 300)
            drawcorrect(1021, 300)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_2.blit(correctImg[16], (402, 300))
                bg_ph_2.blit(correctImg[16], (1021, 300))
                foundph2_6 = 3
        if foundph2_7 == 2: # ผลไม้?
            drawcorrect(216, 195)
            drawcorrect(835, 195)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_2.blit(correctImg[16], (216, 195))
                bg_ph_2.blit(correctImg[16], (835, 195))
                foundph2_7 = 3
        if foundph2_8 == 2:
            drawcorrect(945, 420)
            drawcorrect(328, 420)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
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
                    print(mx, my)
                    print(health_value)
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
                        WALKCOUNT = 0
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
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_3.blit(correctImg[16], (551, 213))
                bg_ph_3.blit(correctImg[16], (1150, 213))
                foundph3_1 = 3
        if foundph3_2 == 2: # เก้าอี้
            drawcorrect(486, 297)
            drawcorrect(1086, 297)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_3.blit(correctImg[16], (486, 297))
                bg_ph_3.blit(correctImg[16], (1086, 297))
                foundph3_2 = 3
        if foundph3_3 == 2: # ไข่มุก
            drawcorrect(180, 515)
            drawcorrect(776, 515)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_3.blit(correctImg[16], (180, 515))
                bg_ph_3.blit(correctImg[16], (776, 515))
                foundph3_3 = 3
        if foundph3_4 == 2: # แก้วบนชั้นวาง ชั้น 2
            drawcorrect(127, 214)
            drawcorrect(727, 214)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_3.blit(correctImg[16], (127, 214))
                bg_ph_3.blit(correctImg[16], (727, 214))
                foundph3_4 = 3
        if foundph3_5 == 2: # หมีล่าง
            drawcorrect(223, 365)
            drawcorrect(812, 365)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
                bg_ph_3.blit(correctImg[16], (223, 365))
                bg_ph_3.blit(correctImg[16], (812, 365))
                foundph3_5 = 3
        if foundph3_6 == 2: #ขวดแก้วชั้นบน
            drawcorrect(70, 155)
            drawcorrect(670, 155)
            if WALKCOUNT > 16:
                WALKCOUNT = 0
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

#-----------------Broom game-----------------------
    if PLAY_BROOM:
        pygame.time.delay(0)
        bg_scrolling_b -= 1

        if timeb >= 180:
            PLAY_BROOM, idmap, countd = False, "18", 28
            bg = pygame.image.load(mapping[idmap])
            POSX_ESME, POSY_ESME = 500, 400
            POSX_SHE, POSY_SHE = 750, 400
            POSX_AVI, POSY_AVI = -10, 150
            POSX_VEN, POSY_VEN = -10, 400
            fadeout()
            PLAY_MAIN, STORY2 = True, True
            fadein(bg, -283, -358)

        elif timeb >= 120:
            if fadebg3 == False:
                fadescreen()
                fadebg3 = True
            win.blit(bg_b3, (bg_scrolling_b, 0))
            win.blit(bg_b3, (bg_scrolling_b+1280, 0))

        elif timeb >= 60:
            if fadebg2 == False:
                fadescreen()
                fadebg2 = True
            win.blit(bg_b2, (bg_scrolling_b, 0))
            win.blit(bg_b2, (bg_scrolling_b+1280, 0))

        elif timeb >= 0:
            win.blit(bg_b1, (bg_scrolling_b, 0))
            win.blit(bg_b1, (bg_scrolling_b+1280, 0))
        if bg_scrolling_b <= -1280:
            bg_scrolling_b = 0
        timeb += 0.05
        # y += 5

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and xb > 10:
            xb -= vel
            leftb = True
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and xb < bg_width-150:
            xb += vel
            rightb = True
        elif (keys[pygame.K_w] or keys[pygame.K_UP]) and yb > 5:
            yb -= vel
            rightb = True
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and yb < bg_height-500:
            yb += vel
            rightb = True
        else:
            rightb = False

    if PLAY_BROOM:
    #----------------------------------------------------------- stage 1 ----------------------------------------------------------------
        bird2.spawn(9,7,0); bird9.spawn(22,7,0); bird16.spawn(33,20,0)
        bird3.spawn(10,7,0); bird10.spawn(25,7,0); bird17.spawn(47,15,0)
        bird4.spawn(14,7,0); bird11.spawn(27,7,0)
        bird5.spawn(14.5,7,0); bird12.spawn(29,7,0)
        bird6.spawn(17,7,0); bird13.spawn(33,7,0)
        bird7.spawn(20,7,0); bird14.spawn(33,7,0)
        bird18.spawn(49,12,0)
        bird19.spawn(49,12,0)
        bird20.spawn(49,12,0)
        bird21.spawn(49,12,0)
        bird22.spawn(49,12,0)
    #--------------------------------------------------------- bounce ------------------------------------------------------------
        bird_1b.spawn(41,13,20,bounce=True)
        bird_2b.spawn(41,13,20,bounce=True)
        bird_3b.spawn(43,13,20,bounce=True)
        bird_4b.spawn(43,13,20,bounce=True)
        bird_5b.spawn(52,13,20,bounce=True)

    #--------------------------------------------------------- disco ------------------------------------------------------------
        bird01.spawn(18,20,0)
        bird02.spawn(20,20,0)
        bird03.spawn(24,20,0)
        bird04.spawn(40,20,0)
        bird05.spawn(25,20,0)
        bird06.spawn(30,20,0)
        bird07.spawn(35,20,0)
        bird08.spawn(29,20,0)
        bird09.spawn(50,20,0)
    #----------------------------------------------------------- stage 2 ----------------------------------------------------------------
        clock1.spawn(69,10,0)
        clock2.spawn(69.3,10,0)
        clock3.spawn(72,10,0)
        clock4.spawn(72.3,10,0)
        clock5.spawn(74,10,0)
        clock6.spawn(74,10,0)
        clock7.spawn(75,10,0)
        clock8.spawn(75.3,10,0)
        clock9.spawn(77,10,0)
        clock10.spawn(77.3,10,0)
        clock11.spawn(77.8,10,0)
        clock12.spawn(78,10,0)
        clock13.spawn(78.3,10,0)

        clock14.spawn(87,10,0)
        clock15.spawn(88,10,0)
        clock16.spawn(88.3,10,0)
        clock17.spawn(89,10,0)
        clock18.spawn(89.3,10,0)

        clock19.spawn(96,0,-10)
        clock20.spawn(96,0,10)
        clock21.spawn(100,0,-10)
        clock22.spawn(100,0,10)
        clock23.spawn(104,0,-10)
        clock24.spawn(104,0,10)
        clock25.spawn(108,0,-10)
        clock26.spawn(108,0,10)
    #--------------------------------------------------------- bounce ------------------------------------------------------------
        clock1b.spawn(81,20,20,bounce=True)
        clock2b.spawn(81,20,20,bounce=True)
        clock3b.spawn(82,20,20,bounce=True)
        clock4b.spawn(82,20,20,bounce=True)
        clock5b.spawn(83,20,20,bounce=True)
        clock6b.spawn(83,20,20,bounce=True)
        clock7b.spawn(84,20,20,bounce=True)
        clock8b.spawn(84,20,20,bounce=True)
        clock9b.spawn(85,20,20,bounce=True)
        clock10b.spawn(85,20,20,bounce=True)

        clock11b.spawn(97,10,10,bounce=True)
        clock12b.spawn(97,-10,10,bounce=True)
        clock13b.spawn(103,10,10,bounce=True)
        clock14b.spawn(103,-10,10,bounce=True)
        clock15b.spawn(109,10,10,bounce=True)
        clock16b.spawn(109,-10,10,bounce=True)
    #--------------------------------------------------------- disco ------------------------------------------------------------
        clock01.spawn(73,20,0)
        clock02.spawn(75,20,0)
        clock03.spawn(78,20,0)
        clock04.spawn(88,20,0)
        clock05.spawn(89,20,0)
    #------------------------------------------------------ stage 3 ห้องสมุด [121 - 180] -----------------------------------------------------
        bluebook1.spawn(129, 10, 0); bluebook2.spawn(134, 10, 0); bluebook3.spawn(145, 10, 0)
        bluebook4.spawn(152, 10, 0); bluebook5.spawn(162, 10, 0); bluebook6.spawn(167, 10, 0)
        bluebook7.spawn(172, 10, 0); bluebook8.spawn(130, 10, 0); bluebook9.spawn(135, 10, 0)
        bluebook10.spawn(145, 10, 0); bluebook11.spawn(154, 10, 0); bluebook12.spawn(162, 10, 0)
        bluebook13.spawn(168, 10, 0); bluebook14.spawn(173, 10, 0); bluebook15.spawn(133, 10, 0)
        bluebook16.spawn(149, 10, 0); bluebook17.spawn(154, 10, 0); bluebook18.spawn(164, 10, 0)
        redbook1.spawn(143, 10, 0); redbook2.spawn(147, 10, 0); redbook3.spawn(164, 10, 0)
        redbook4.spawn(126, 10, 0); redbook5.spawn(132, 10, 0); redbook6.spawn(149, 10, 0)
        redbook7.spawn(145, 10, 0); redbook8.spawn(151, 10, 0); redbook9.spawn(125, 10, 0)
        redbook10.spawn(139, 10, 0); redbook11.spawn(144, 10, 0); redbook12.spawn(149, 10, 0)
        redbook13.spawn(155, 10, 0); redbook14.spawn(127, 10, 0); redbook15.spawn(137, 10, 0); redbook16.spawn(152, 10, 0)
        purbook1.spawn(165, -10, 0); purbook2.spawn(156, -10, 0)
    # #--------------------------------------------------------- bounce ------------------------------------------------------------
        bluebook_1b.spawn(132,20,20,bounce=True)
        bluebook_2b.spawn(137,20,20,bounce=True)
        bluebook_3b.spawn(142,20,20,bounce=True)
        bluebook_4b.spawn(147,20,20,bounce=True)
        bluebook_5b.spawn(152,20,20,bounce=True)
        bluebook_6b.spawn(157,20,20,bounce=True)
        bluebook_7b.spawn(162,20,20,bounce=True)
        bluebook_8b.spawn(167,20,20,bounce=True)
        bluebook_9b.spawn(172,20,20,bounce=True)
    #--------------------------------------------------------- disco -------------------------------------------------------------
        bluebook01.spawn(129,20,0)
        bluebook02.spawn(150,20,0)
        bluebook03.spawn(139,20,0)
        bluebook04.spawn(140,20,0)
    #-------------------------------------------------------------------------------------------------------------------------------
        cooldownb += 0.05

        if heartb == 5:
            win.blit(heartimg, (920, 25))
            win.blit(heartimg, (985, 25))
            win.blit(heartimg, (1050, 25))
            win.blit(heartimg, (1115, 25))
            win.blit(heartimg, (1180, 25))        
        if heartb == 4:
            win.blit(heartimg, (985, 25))
            win.blit(heartimg, (1050, 25))
            win.blit(heartimg, (1115, 25))
            win.blit(heartimg, (1180, 25))
        if heartb == 3:
            win.blit(heartimg, (1050, 25))
            win.blit(heartimg, (1115, 25))
            win.blit(heartimg, (1180, 25))
        if heartb == 2:
            win.blit(heartimg, (1115, 25))
            win.blit(heartimg, (1180, 25))
        if heartb == 1:
            win.blit(heartimg, (1180, 25)) 
        if heartb == 0:
            heartb = 5
        win.blit(font.render("Time : "+str(int(timeb)), True, (255,255,255)), (20,20))
        redrawbroomGameWindow()

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

        win.blit(book_img[book_anim], (0, 0))

        if book_inven and book_anim == 19:
            if 'potion' not in inventory:
                win.blit(potion_s, (710, 212))
            if 'potion' in inventory:
                win.blit(potion, (710, 212))
            if 'magicpowder' not in inventory:
                win.blit(magicpowder_s, (800, 212))
            if 'magicpowder' in inventory:
                win.blit(magicpowder, (800, 212))
            if 'applescrap' not in inventory:
                win.blit(applescrap_s, (895, 205))
            if 'applescrap' in inventory:
                win.blit(applescrap, (895, 205))
            if 'puzzlepaper1' not in inventory:
                win.blit(puzzlepaper_s, (975, 215))
            if 'puzzlepaper1' in inventory:
                win.blit(puzzlepaper, (975, 215))
            if 'puzzlepaper2' not in inventory:
                win.blit(puzzlepaper_s, (690, 308))
            if 'puzzlepaper2' in inventory:
                win.blit(puzzlepaper, (690, 308))
            if 'puzzlepaper3' not in inventory:
                win.blit(puzzlepaper_s, (785, 308))
            if 'puzzlepaper3' in inventory:
                win.blit(puzzlepaper, (785, 308))
            if 'puzzlepaper4' not in inventory:
                win.blit(puzzlepaper_s, (880, 308))
            if 'puzzlepaper4' in inventory:
                win.blit(puzzlepaper, (880, 308))
            if 'puzzlepaper5' not in inventory:
                win.blit(puzzlepaper_s, (975, 308))
            if 'puzzlepaper5' in inventory:
                win.blit(puzzlepaper, (975, 308))

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
        # print("row1", row1, "row2", row2, "row3", row3, "row4", row4)

    if PLAY_FRONT:
        frontgame()
    pygame.display.update()
    
    # print(X, Y)
    # print(idmap)

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mx, my = pygame.mouse.get_pos()
        # print(mx, my)

pygame.quit()
