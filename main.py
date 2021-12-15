import pygame, json
from pygame import mixer
from pygame import display
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.draw import circle

pygame.init()
#-------------------------------Set variable--------------------------------
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("W <it> CH AcademY")

mapping = open("map.txt", "r").read()
mapping = dict(json.loads(mapping))
walls = open("walls.txt", 'r').read()
walls = dict(json.loads(walls))
idmap = "00"
bg = pygame.image.load(mapping[idmap])
bg2 = pygame.image.load(mapping[idmap])
bgblood = pygame.image.load('sprite/map/forestblood.jpg')
bgfirstaid = pygame.image.load('sprite/map/firstaidroom.jpg')
bgfront = pygame.image.load("sprite/front.jpg")
BG_SCROLLING, ANIM = 0, 0
bg_width, bg_height = bg.get_rect().size
icon = pygame.image.load("sprite/minilogo.png")
pygame.display.set_icon(icon)
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
mx, my = -1, -1 #เมาส์ ใส่ไว้กันคนไม่คลิกเมาส์

run = True
PLAY_FRONT, PLAY_MAIN, PLAY_PH1, PLAY_PH2, PLAY_PH3 = True, False, False, False, False
PLAY_BROOM, PLAY_SEFOR = False, False
LEFT, RIGHT = False, False
DOWN, UP = False, False
mouseon = 0
#----------------------------------Sound-----------------------------------
music = True
cd_foot = 5
s_volum = 1.0
bgm_intro = pygame.mixer.Sound("sound/intro.mp3"); bgm_intro.set_volume(1.0)
bgm_hall = pygame.mixer.Sound("sound/schooltheme.mp3"); bgm_hall.set_volume(1.0)
bgm_opendoor = pygame.mixer.Sound("sound/Wood Door - Open_Close.mp3"); bgm_opendoor.set_volume(1.0)
bgm_canteen = pygame.mixer.Sound("sound/canteen.mp3"); bgm_canteen.set_volume(1.0)
bgm_corridor = pygame.mixer.Sound("sound/class.mp3"); bgm_corridor.set_volume(1.0)
bgm_garden = pygame.mixer.Sound("sound/garden.mp3"); bgm_garden.set_volume(1.0)
boom_sound = pygame.mixer.Sound("sound/explode.mp3"); boom_sound.set_volume(1.0)
bgm_dark = pygame.mixer.Sound("sound/dark song.mp3"); boom_sound.set_volume(1.0)
foot = pygame.mixer.Sound("sound/wood.mp3"); foot.set_volume(0.4)
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
#-----------------------------------Icon------------------------------------
door_icon = readvar('var.txt', 'door')
hand_icon = readvar('var.txt', 'hand')
chat_icon = readvar('var.txt', 'chat')
#-----------------------------Front and Cutscene----------------------------
FRONTANIM = False
play_dialog, play_cutscene, nextdia = False, False, False
STORY1, STORY2, STORY3, STORY4, STORY5 = False, False, False, False, False
BLACK, alpha = 0, 255
posx_txt, posy_txt = 205, 80
counttxt, countd = 0, 0
checkpoint = 4

logo = pygame.image.load('sprite/logo.png')
press = pygame.image.load('sprite/press.png')
font = pygame.font.Font('sprite/alagard.ttf', 21)
avilia_walkr, avilia_walkl = readvar('var.txt', 'avilia/walkr'), readvar('var.txt', 'avilia/walkl')
avilia_walkd, avilia_walku = readvar('var.txt', 'avilia/walkd'), readvar('var.txt', 'avilia/walku')
esme_walkr = readvar('var.txt', 'esme/walkr')
she_walkr = readvar('var.txt', 'sheree/walkr')
ven_walkr = readvar('var.txt', 'veneno/walkr')
ven_walku = readvar('var.txt', 'veneno/walku')
ven_walkd = readvar('var.txt', 'veneno/walkd')
m1_walkl, m2_walkl = readvar('var.txt', 'm1_walkl'), readvar('var.txt', 'm2_walkl')
m1_b, m2_b = readvar('var.txt', 'm1_b'), readvar('var.txt', 'm2_b')
head_walku = readvar('var.txt', 'headmaster/walku')
head_walkd = readvar('var.txt', 'headmaster/walkd')
she_push = readvar('var.txt', 'sheree/push')
esme_fail = readvar('var.txt', 'esme/fail')
sheree_b = readvar('var.txt', 'sheree/broom')
esme_b = readvar('var.txt', 'esme/broom')
avilia_b = readvar('var.txt', 'avilia/broom')
explosion = readvar('var.txt', 'explosion')
dialogbox = readvar('var.txt', 'dialogbox')
lstdialog = readvar('dialog.txt', '')
dia_she = pygame.image.load('sprite/sheree/sheree.png')
dia_esme = pygame.image.load('sprite/esme/esme.png')
dia_avi = pygame.image.load('sprite/avilia/avilia.png')
dia_ven = pygame.image.load('sprite/veneno/veneno.png')
dia_stella = pygame.image.load('sprite/stella/dia_stella.png')
dia_head = pygame.image.load('sprite/headmaster/headmaster.png')
esme_sleep = pygame.image.load('sprite/esme/sleep.png')
apple = pygame.image.load('sprite/item/apple.png')
bubble = readvar('var.txt', 'bubble/bubble')
sad, upset, shock = readvar('var.txt', 'sad'), readvar('var.txt', 'upset'), readvar('var.txt', 'shock')
sad, upset, shock = bubble+sad+sad, bubble+upset+upset, bubble+shock+shock
POSX_AVI, POSY_AVI = -300, 0
POSX_ESME, POSY_ESME = -150, 0
POSX_SHE, POSY_SHE = 300, 0
POSX_VEN, POSY_VEN = 0, 0
POSX_M1, POSY_M1 = 100, 363
POSX_M2, POSY_M2 = 100, 323
ANIMB, WALK_ESME, WALK_SHE, WALK_VEN, WALK_M1, WALK_M2, WALK_H = 0, 0, 0, 0, 0, 0, 0
#------------------------------Book Scroll paper----------------------------
book_img = readvar('var.txt', 'book')
paper_b1 = readvar('var.txt', 'B1')
paper_901502 = readvar('var.txt', '901502')
paper_blackcathate = readvar('var.txt', 'blackcathate')
paper_bnwbklu = readvar('var.txt', 'bnwbklu')
paper_rulemf = readvar('var.txt', 'rulemf')
paper_ruleph = readvar('var.txt', 'ruleph')
paper_rulepz = readvar('var.txt', 'rulepz')
paper_rulerc = readvar('var.txt', 'rulerc')
book_anim, ANIM_PAPER = 0, 0
openbook, closebook = False, False
nextpage, backpage = False, False
book_map, book_inven, book_menu = True, False, False
cd_paper, what_paper, closepaper = 0, [], False
seepaper = False
applescrap_b = pygame.image.load('sprite/book/applescrap.png')
applescrap_s = pygame.image.load('sprite/book/applescrap_s.png')
magicpowder_b = pygame.image.load('sprite/book/magicpowder.png')
magicpowder_s = pygame.image.load('sprite/book/magicpowder_s.png')
puzzlepaper_b = pygame.image.load('sprite/book/puzzlepaper.png')
puzzlepaper_s = pygame.image.load('sprite/book/puzzlepaper_s.png')
potion_b = pygame.image.load('sprite/book/potion.png')
potion_s = pygame.image.load('sprite/book/potion_s.png')
#-----------------------------------Item------------------------------------
item = []
applescrap = pygame.image.load('sprite/item/applescrap.png')
potion = pygame.image.load('sprite/item/potion.png')
magicpowder = pygame.image.load('sprite/item/magicpowder.png')
paper1 = pygame.image.load("sprite/item/paper1.png")
paper2 = pygame.image.load("sprite/item/paper2.png")
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
            bgm_intro.stop()
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
    if WALK_AVI+1 > len(avilia_walkr)-1: #กัน out of range
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
    elif not RIGHT and not LEFT and not DOWN and not UP:
        if CHECK == 'RIGHT':
            win.blit(avilia_walkr[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'LEFT':
            win.blit(avilia_walkl[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'DOWN':
            win.blit(avilia_walkd[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'UP':
            win.blit(avilia_walku[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
#---------------------------------------------------------------------------
def fadeout(maxtime=150):
    """ fade out screen """
    fade = pygame.Surface((1280, 720))
    fade.fill((0,0,0))
    for alpha in range(0, maxtime):
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
def redrawobtain(string1, string2):
    global alpha, X, Y
    txt1 = font.render(string1, True, (0, 0, 0))
    txt2 = font.render(string2, True, (0, 0, 0))
    if alpha > 0:
        alpha = max(alpha-0.5, 0)
        txt1_surf, txt2_surf = txt1.copy(), txt2.copy()
        alpha1_surf = pygame.Surface(txt1_surf.get_size(), pygame.SRCALPHA)
        alpha2_surf = pygame.Surface(txt2_surf.get_size(), pygame.SRCALPHA)
        alpha1_surf.fill((255, 255, 255, alpha))
        alpha2_surf.fill((255, 255, 255, alpha))
        txt1_surf.blit(alpha1_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        txt2_surf.blit(alpha2_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        win.blit(txt1_surf, (int((X+(89/2))-(txt1.get_size()[0]/2)), Y-55))
        win.blit(txt2_surf, (int((X+(89/2))-(txt2.get_size()[0]/2)), Y-30))
#---------------------------------------------------------------------------
def meanwalk(idm, way, stop):
    global WALK_M1, WALK_M2, POSX_M1, POSY_M1, POSX_M2, POSY_M2
    if WALK_M1+1 > len(m1_walkl)-1:WALK_M1 = 0
    if WALK_M2+1 > len(m2_walkl)-1:WALK_M2 = 0
    if idm == 1:
        if way == 'right':
            if POSX_M1 != stop:
                POSX_M1 += 5
                WALK_M1 += 1
            win.blit(pygame.transform.flip(m1_walkl[WALK_M1], True, False), (POSX_M1, POSY_M1))
        if way == 'left':
            if POSX_M1 != stop:
                POSX_M1 -= 5
                WALK_M1 += 1
            win.blit(m1_walkl[WALK_M1], (POSX_M1, POSY_M1))
    if idm == 2:
        if way == 'right':
            if POSX_M2 != stop:
                POSX_M2 += 5
                WALK_M2 += 1
            win.blit(pygame.transform.flip(m2_walkl[WALK_M2], True, False), (POSX_M2, POSY_M2))
        if way == 'left':
            if POSX_M2 != stop:
                POSX_M2 -= 5
                WALK_M2 += 1
            win.blit(m2_walkl[WALK_M2], (POSX_M2, POSY_M2))
#---------------------------------------------------------------------------
def meanbroom(idm, way, stop):
    global WALK_M1, WALK_M2, POSX_M1, POSY_M1, POSX_M2, POSY_M2
    if WALK_M1+1 > len(m1_b)-1:WALK_M1 = 0
    if WALK_M2+1 > len(m2_b)-1:WALK_M2 = 0
    if idm == 1:
        win.blit(pygame.transform.flip(m1_b[WALK_M1], True, False), (POSX_M1-50, POSY_M1))
        if POSX_M1 != stop:
            POSX_M1 -= 10
    if idm == 2:
        win.blit(pygame.transform.flip(m2_b[WALK_M2], True, False), (POSX_M2-50, POSY_M2))
        if POSX_M2 != stop:
            POSX_M2 -= 10
    WALK_M1 += 1
    WALK_M2 += 1
#---------------------------------------------------------------------------
def shepush():
    global WALK_SHE, POSX_SHE, POSY_SHE
    if WALK_SHE > 11:WALK_SHE = 11
    win.blit(she_push[WALK_SHE], (POSX_SHE, POSY_SHE))
    WALK_SHE += 1
#---------------------------------------------------------------------------
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
#---------------------------------------------------------------------------
def aviwalk(way, stop):
    global WALK_AVI, POSX_AVI, POSY_AVI
    if WALK_AVI+1 > len(avilia_walkr)-1:WALK_AVI = 0
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
#---------------------------------------------------------------------------
def shewalk(way, stop):
    global WALK_SHE, POSX_SHE, POSY_SHE
    if WALK_SHE+1 > len(she_walkr)-1:WALK_SHE = 0
    if way == 'right':
        if POSX_SHE != stop:
            POSX_SHE += 5
            WALK_SHE += 1
        win.blit(she_walkr[WALK_SHE], (POSX_SHE, POSY_SHE))
    if way == 'left':
        if POSX_SHE != stop:
            POSX_SHE -= 5
            WALK_SHE += 1
        win.blit(pygame.transform.flip(she_walkr[WALK_SHE], True, False), (POSX_SHE, POSY_SHE))
#---------------------------------------------------------------------------
def esmewalk(way, stop):
    global WALK_ESME, POSX_ESME, POSY_ESME
    if WALK_ESME+1 > len(esme_walkr)-1:WALK_ESME = 0
    if way == 'right':
        if POSX_ESME != stop:
            POSX_ESME += 5
            WALK_ESME += 1
        win.blit(esme_walkr[WALK_ESME], (POSX_ESME, POSY_ESME))
    if way == 'left':
        if POSX_ESME != stop:
            POSX_ESME -= 5
            WALK_ESME += 1
        win.blit(pygame.transform.flip(esme_walkr[WALK_ESME], True, False), (POSX_ESME, POSY_ESME))
#---------------------------------------------------------------------------
def venwalk(way, stop):
    global WALK_VEN, POSX_VEN, POSY_VEN
    if WALK_VEN+1 > len(ven_walkr)-1:WALK_VEN = 0
    if way == 'right':
        if POSX_VEN != stop:
            POSX_VEN += 5
            WALK_VEN += 1
        win.blit(ven_walkr[WALK_VEN], (POSX_VEN, POSY_VEN))
    if way == 'left':
        if POSX_VEN != stop:
            POSX_VEN -= 5
            WALK_VEN += 1
        win.blit(pygame.transform.flip(ven_walkr[WALK_VEN], True, False), (POSX_VEN, POSY_VEN))
    if way == 'up':
        if POSY_VEN != stop:
            POSY_VEN -= 5
            WALK_VEN += 1
        win.blit(ven_walku[WALK_VEN], (POSX_VEN, POSY_VEN))
    if way == 'down':
        if POSY_VEN != stop:
            POSY_VEN += 5
            WALK_VEN += 1
        win.blit(ven_walkd[WALK_VEN], (POSX_VEN, POSY_VEN))
#---------------------------------------------------------------------------
def headwalk(way, stop):
    global WALK_H, POSX_H, POSY_H
    if WALK_H+1 > len(head_walkl)-1:WALK_H = 0
    if way == 'up':
        if POSY_H != stop:
            POSY_H -= 5
            WALK_H += 1
        win.blit(head_walku[WALK_H], (POSX_H, POSY_H))
    if way == 'down':
        if POSY_H != stop:
            POSY_H += 5
            WALK_H += 1
        win.blit(head_walkd[WALK_H], (POSX_H, POSY_H))
#---------------------------------------------------------------------------
def shebroom(way, stop):
    global WALK_SHE, POSX_SHE, POSY_SHE
    if WALK_SHE+1 > len(sheree_b)-1:WALK_SHE = 0
    she_copy = sheree_b[WALK_SHE].copy()
    she_copy = pygame.transform.scale(she_copy, (135, 135))
    if way == 'left':
        win.blit(pygame.transform.flip(she_copy, True, False), (POSX_SHE-50, POSY_SHE))
        if POSX_SHE != stop:
            POSX_SHE -= 10
    WALK_SHE += 1
#---------------------------------------------------------------------------
def avibroom(way, stop):
    global WALK_AVI, POSX_AVI, POSY_AVI, countd
    if WALK_AVI+1 > len(avilia_b)-1:WALK_AVI = 0
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
#---------------------------------------------------------------------------
def esmebroom(way, stop):
    global WALK_ESME, POSX_ESME, POSY_ESME
    if WALK_ESME+1 > len(esme_b)-1:WALK_ESME = 0
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
#---------------------------------------------------------------------------
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
#---------------------------------------------------------------------------
def redrawicon(icon, posx, posy):
    global ANIM
    if icon == "door":
        if ANIM+1 > len(door_icon)-1:ANIM = 0
        win.blit(door_icon[ANIM], (posx, posy))
    if icon == "hand":
        if ANIM+1 > len(hand_icon)-1:ANIM = 0
        win.blit(hand_icon[ANIM], (posx, posy))
    if icon == "chat":
        if ANIM+1 > len(chat_icon)-1:ANIM = 0
        win.blit(chat_icon[ANIM], (posx, posy))
    ANIM += 1
#---------------------------------------------------------------------------
def redrawblack():
    """ blit black """
    global BLACK
    pygame.draw.rect(win, (0), [0, 0, 1280, BLACK])
    pygame.draw.rect(win, (0), [0, 722-BLACK, 1280, 100])
#---------------------------------------------------------------------------
def redrawdialog(countd):
    """ blit dialog """
    global ANIM, counttxt, nextdia, play_dialog
    global posx_txt, posy_txt
    if ANIM > 9:ANIM = 9
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
        if lstdialog[countd].split()[0] == 'Stella':
            win.blit(dia_stella, (141.5, 450))
        if lstdialog[countd].split()[0] == 'Headmaster':
            win.blit(dia_head, (141.5, 450))
        if counttxt <= len(lstdialog[countd].split(' : ')[1])-1:
            message = font.render(lstdialog[countd].split(' : ')[1][counttxt], True, (0, 0, 0))
            dialogbox[9].blit(message, (posx_txt, posy_txt))
            posx_txt += message.get_rect().size[0]+0.5
        if posx_txt >= 950:
            posx_txt, posy_txt = 205, 120
        counttxt += 1
    ANIM += 1
#---------------------------------------------------------------------------
def redrawpaper(paper):
    "blit paper"
    global ANIM_PAPER
    global cd_paper
    global closepaper
    global seepaper
    if ANIM_PAPER+1 > 14:ANIM_PAPER = 14
    win.blit(paper[ANIM_PAPER], (0, 0))

    if ANIM_PAPER == 14:
        cd_paper += 1
        if cd_paper >= 30 and not book_inven:
            closepaper = True
            paper.reverse()
            ANIM_PAPER = 0
            cd_paper = 0
        if book_inven and not seepaper:
            closepaper = True
            paper.reverse()
            ANIM_PAPER = 0
            cd_paper = 0

    else:
        ANIM_PAPER += 1

    if closepaper and ANIM_PAPER == 14:
        ANIM_PAPER = 0
        what_paper.clear()
        closepaper = False

#---------------------------------------------------------------------------
def cutscene():
    """ blit cutscene """
    global STORY1, STORY2, STORY3, STORY4, STORY5, play_dialog, play_cutscene
    global ANIM, ANIMB, checkpoint
    global countd, counttxt, posx_txt, posy_txt, nextdia
    global POSX_ESME, POSY_ESME, POSX_AVI, POSY_AVI
    global POSX_SHE, POSY_SHE, POSY_M1, POSY_M2
    if STORY1:
        if lstdialog[countd].split()[0] == 'End':
            play_dialog, STORY1 = False, False
        if countd < 16: meanwalk(2, 'right', 550)
        if countd in range(0, 7): aviwalk('left', 1065)
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
            else: ANIMB = 0
        if countd in [16] and counttxt < 52:
            meanwalk(2, 'right', 550)
            meanwalk(1, 'right', 550)
        if countd in [16] and counttxt < 32: shewalk('right', 630)
        if countd > 16 or (countd == 16 and counttxt >= 52):
            meanbroom(2, 'left', -100)
            meanbroom(1, 'left', -100)
            POSY_M1 -= 2.5
            POSY_M2 -= 2.5
        if countd > 16 or (countd == 16 and counttxt >= 32):
            shebroom('left', -100)
            POSY_SHE -= 2.5
        if countd < 16: meanwalk(1, 'right', 550)
    elif STORY2:
        if lstdialog[countd].split()[0] == 'End':
            play_dialog, STORY2 = False, False
        if countd in [28] and POSX_AVI == 200: play_dialog = True
        if countd in range(28, 35):
            avibroom('right', 200)
            shewalk('left', 750)
            meanwalk(1, 'left', 880)
            meanwalk(2, 'left', 860)
            esmewalk('right', 500)
        if countd in [32] and counttxt in range(50, 65):
            redrawbubble('shock', POSX_ESME+2, POSY_ESME-40)
            redrawbubble('shock', POSX_AVI+2, POSY_AVI-40)
        else: ANIMB = 0
        if countd in [35]:
            if counttxt in range(0, 20):
                shewalk('left', 750)
                meanwalk(1, 'left', 880)
                meanwalk(2, 'left', 860)
                esmewalk('right', 500)
                win.blit(apple, (POSX_SHE-25+(counttxt), POSY_SHE+30))
            if counttxt in range(20, 47):
                if counttxt == 20:
                    boom_sound.play()
                    bgm_garden.stop()
                    bgm_dark.play()
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
            play_dialog, STORY3, countd = False, False, 0
            bgm_dark.stop()
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
    elif STORY4:
        if countd == 69 and POSX_VEN > 1100:
            STORY4, checkpoint = False, 5
        if lstdialog[countd].split()[0] == 'End':
            play_dialog, countd = False, 69
        if countd in range(62, 70) and STORY4:
            if countd < 69 or (countd == 69 and POSX_VEN < 870):
                headwalk('up', 255)
            if countd == 69 and 975 > POSX_VEN >= 870:
                headwalk('down', 255)
            if countd == 69 and 950 > POSX_VEN > 900:
                win.blit(apple, ((POSX_H+35)-((POSX_VEN-900)/5)*2, POSY_H+25))
            if countd == 69 and 1100 > POSX_VEN > 975:
                win.blit(explosion[int((POSX_VEN-980)/5)], (POSX_H-150, POSY_H-150))
        if countd == 69 and POSY_VEN == 325 and POSX_VEN >= 800:
            venwalk('right', 1300)
        elif countd == 69 and POSX_VEN == 800:
            venwalk('up', 325)
        elif countd == 69 and POSY_VEN == 355:
            venwalk('right', 800)
        elif countd == 69 and POSX_VEN == 550:
            venwalk('down', 355)
        if countd in range(65, 69) and POSY_VEN == 255:
            venwalk('left', 550)
            if countd == 65 and POSX_VEN == 550:
                posx_apple, posy_apple = POSX_VEN-35, POSY_VEN+25
                win.blit(apple, (posx_apple, posy_apple))
            if countd == 66:
                if counttxt in range(0, 20):
                    win.blit(apple, (POSX_VEN-35-(counttxt*2), POSY_VEN+25))
        elif countd == 65 and POSX_VEN == 570:
            venwalk('up', 255)
        if countd in range(62, 65) and POSX_VEN == 570:
            venwalk('left', 570)
            play_dialog = True
        elif countd == 62 and not play_dialog and POSY_VEN == 355:
            venwalk('left', 570)
        elif countd == 62 and not play_dialog and POSX_VEN == 780:
            venwalk('down', 355)
        elif countd == 62 and not play_dialog:
            venwalk('left', 780)
    elif STORY5:
        if lstdialog[countd].split()[0] == 'End':
            play_dialog, countd = False, 77
        if countd == 77:
            esmewalk('right', 320)
            venwalk('left', 320)
        if POSX_VEN <= 350:
            play_cutscene, STORY5, checkpoint = False, False, 6
        if countd in range(70, 77):
            esmewalk('right', 320)
            venwalk('left', 480)
    if play_dialog:redrawdialog(countd)
    if keys[pygame.K_SPACE] and play_dialog:
        nextdia = True
#     if keys[pygame.K_SPACE] and play_dialog and counttxt >= len(lstdialog[countd].split(':')[1])-1:
#         if countd in [0] and counttxt >= 10:nextdia = True
#         if countd in [3] and counttxt >= 90:nextdia = True
#         if countd in [7] and counttxt >= 50:nextdia = True
#         if countd in [11] and counttxt >= 25:nextdia = True
#         if countd in [16] and counttxt >= 50:nextdia = True
#         if countd in [32] and counttxt >= 70:nextdia = True
#         if countd in [35] and counttxt >= 50:nextdia = True
#         elif countd not in [0, 3, 7, 11, 16, 32, 35]:nextdia = True
    elif nextdia:
        if not keys[pygame.K_SPACE]:
            countd += 1
            if lstdialog[countd-1].split()[0] != lstdialog[countd].split()[0]: ANIM = 0
            counttxt, posx_txt, posy_txt = 0, 205, 80
            dialogbox[9] = pygame.image.load('sprite/dialog/dialogbox10.png')
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

    #แกนY
    if Y > stage_height-PLAYER_RADIUS:
        Y = stage_height-PLAYER_RADIUS
    if Y < PLAYER_RADIUS:
        Y = PLAYER_RADIUS
    if Y < start_scrolling_y:
        PLAYER_POSITION_Y = Y
    elif Y > stage_height-start_scrolling_y:
        PLAYER_POSITION_Y = Y-stage_height+height
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
    global cd_foot
    if keys[pygame.K_a] and X > vel and not openbook and safe < 1 and not play_dialog and not play_cutscene:
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
        if cd_foot > 10:
            foot.play(maxtime=500)
            cd_foot = -2
        cd_foot += 1
    elif keys[pygame.K_d] and not openbook and safe < 1 and not play_dialog and not play_cutscene:
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
        if cd_foot > 10:
            foot.play(maxtime=500)
            cd_foot = -2
        cd_foot += 1
    elif keys[pygame.K_s] and not openbook and safe < 1 and not play_dialog and not play_cutscene:
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
        if cd_foot > 10:
            foot.play(maxtime=500)
            cd_foot = -2
        cd_foot += 1
    elif keys[pygame.K_w] and not openbook and safe < 1 and not play_dialog and not play_cutscene:
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
        if cd_foot > 10:
            foot.play(maxtime=500)
            cd_foot = -2
        cd_foot += 1
    else:
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = False
        foot.stop()

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
        if checkpoint >= 3:
            if idmapnew == "09":
                bg = pygame.image.load('sprite/map/firstaidroom_esme.jpg')
                bg2 = pygame.image.load('sprite/map/firstaidroom_esme.jpg')

        if checkpoint >= 4:
            if idmapnew == "00":
                bg = pygame.image.load('sprite/map/entryhall.jpg')
                bg2 = pygame.image.load('sprite/map/entryhall.jpg')
            if idmapnew == "11":
                bg = pygame.image.load('sprite/map/Pathnpc.jpg')
                bg2 = pygame.image.load('sprite/map/Pathnpc.jpg')
            if idmapnew == "15":
                bg = pygame.image.load('sprite/map/westcorridor_1.jpg')
                bg2 = pygame.image.load('sprite/map/westcorridor_1.jpg')
            if idmapnew == "16":
                bg = pygame.image.load('sprite/map/westcorridor_2.jpg')
                bg2 = pygame.image.load('sprite/map/westcorridor_2.jpg')
            if idmapnew == "18":
                bg = bgblood
                bg2 = bgblood
        X = nx
        Y = ny
        change = True
        # music = True
        #=========================hall================================
        if idmapold == '01' and idmapnew == '02': # hall ==> canteen
            bgm_hall.set_volume(0.4)
            bgm_canteen.play(-1)
        #========================eastcorridor1===========================
        elif idmapold == '03' and idmapnew == '08': # eastcorridor1 ==> eastgarden
            bgm_corridor.stop()
            bgm_hall.stop()
            bgm_garden.play(-1).set_volume(0.7)
        elif idmapold == '03' and idmapnew == '02': # eastcorridor1 ==> canteen
            bgm_corridor.stop()
            bgm_hall.play(-1).set_volume(0.4)
            bgm_canteen.play(-1)
        #========================eastcorridor2===========================
        elif idmapold == '04' and idmapnew == '19': # eastcorridor2 ==> eastforest
            bgm_corridor.stop()
            bgm_hall.stop()
            bgm_garden.play(-1).set_volume(0.7)
        elif idmapold == '04' and idmapnew == '10': # eastcorridor2 ==> battleroom
            bgm_corridor.stop()
            bgm_hall.play(-1).set_volume(1.0)
        #========================battleroom===========================
        elif idmapold == '10' and idmapnew == '04': # battleroom ==> eastcorridor2
            bgm_hall.set_volume(0.4)
            bgm_corridor.play(-1)
        #========================eastforest===========================
        elif idmapold == '19' and idmapnew == '04': # eastforest ==> eastcorridor2
            bgm_garden.stop()
            bgm_hall.play(-1).set_volume(0.4)
            bgm_corridor.play(-1)
        #========================westgargen===========================
        elif idmapold == '14' and idmapnew == '13': # westgarden ==> sechall
            bgm_garden.stop()
            bgm_hall.play(-1).set_volume(1.0)
        elif idmapold == '14' and idmapnew == '15': # westgarden ==> westcorridor1
            bgm_garden.stop()
            bgm_hall.play(-1).set_volume(0.4)
            bgm_corridor.play(-1)
        #========================sechall===========================
        elif idmapold == '13' and idmapnew == '14': # westgarden ==> sechall
            bgm_hall.stop()
            bgm_garden.play(-1).set_volume(0.7)
        #========================path==============================
        elif idmapold == '11' and idmapnew == '15': # path ==> westcorridor1
            bgm_hall.set_volume(0.4)
            bgm_corridor.play(-1)
        #========================westcorridor1===========================
        elif idmapold == '15' and idmapnew == '14': # westcorridor1 ==> westgarden
            bgm_corridor.stop()
            bgm_hall.stop()
            bgm_garden.play(-1).set_volume(0.7)
        elif idmapold == '15' and idmapnew == '11': # westcorridor1 ==> path
            bgm_corridor.stop()
            bgm_hall.play(-1).set_volume(1.0)
        #========================westcorridor2===========================
        elif idmapold == '16' and idmapnew == '17': # westcorridor2 ==> westforest
            bgm_corridor.stop()
            bgm_hall.stop()
            bgm_garden.play(-1); bgm_garden.set_volume(0.7)
        #========================westforest===========================
        elif idmapold == '17' and idmapnew == '16': # westforest ==> westcorridor2
            bgm_garden.stop()
            bgm_hall.play(-1).set_volume(0.4)
            bgm_corridor.play(-1)
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
            self.posy += 7.5
            bg.blit(self.name[self.count], (self.posx, self.posy))
        if self.posy >= turnd:
            self.sub_u = True
            self.sub_d = False
        self.count += 1
#------------------------------------Sup------------------------------------
#-----------Entryhalls
sub_entryhalls_01 = sup("g5_", 906, 200)
# ----------Hallways
sub_hallways_01 = sup("sup01_", 1141, 407)
#-----------Canteen
sub_canteen_01 = sup("g12_", 1197, 578)
#-----------Hall
sub_halls_01 = sup("g4_", 641,232)
#-----------Path
sub_path_01 = sup("g5_", 888, 598)
#-----------Westgarden
sub_wastgar_01 = sup("g4_",893,350)
#-----------Eastgarden
sub_eastgar_01 = sup("g8_", 813, 368)
#-----------Eastforest
sub_eastforest_01 = sup("g7_", 1435, 409)
#-----------Westforest
sub_wastforest_01 = sup("g12_", 697,400)
#-----------Westcorridor1
sub_wastcor1_01 = sup("g8_", 797, 225)
#---------------------------------Photohunt---------------------------------
font_ph = pygame.font.Font('sprite/photohunt/2005_iannnnnAMD.ttf', 72)
HeartImg = pygame.image.load('sprite/photohunt/heart.png')
bg_ph_1 = pygame.image.load('sprite/photohunt/stage 1.png')
bgm_ph1 = pygame.mixer.Sound('sound/bgm_ph1.mp3'); bgm_ph1.set_volume(0.3)
bg_ph_2 = pygame.image.load('sprite/photohunt/stage 2.png')
bgm_ph2 = pygame.mixer.Sound('sound/tech_rom.mp3'); bgm_ph2.set_volume(0.3)
bg_ph_3 = pygame.image.load('sprite/photohunt/stage 3.png')
bgm_ph3 = pygame.mixer.Sound('sound/research_roon.mp3'); bgm_ph3.set_volume(0.3)
c_sound = pygame.mixer.Sound("sound/magicsound.mp3"); c_sound.set_volume(0.5)
w_sound = pygame.mixer.Sound("sound/Swoosh.mp3"); w_sound.set_volume(0.5)
win_screen = pygame.image.load('sprite/photohunt/bg_end_ph.jpg')

stage = 0
score_value = 0
health_value = 3
foundph1_1 = foundph1_2 = foundph1_3 = foundph1_4 = foundph1_5 = foundph1_6 = foundph1_7 = 1
foundph2_1 = foundph2_2 = foundph2_3 = foundph2_4 = foundph2_5 = foundph2_6 = foundph2_7 = foundph2_8 = 1
foundph3_1 = foundph3_2 = foundph3_3 = foundph3_4 = foundph3_5 = foundph3_6 = 1
sec = 65 # Timeset <<<<<<<<<<<
WALKCOUNT = 0


correctImg = readvar('photohunt.txt', 'circle')
bucket = pygame.image.load('sprite/item/bucket.png')
finish_ph1 = finish_ph2 = finish_ph3 = False

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
prize_pz = False
play_pz = False

def col(row, xrow, yrow):
    if yrow >= 400:
        win.blit(col_down[row], (xrow, yrow))
    win.blit(col_mid[row], (xrow, yrow+90))
    if yrow+180 <= 590:
        win.blit(col_up[row], (xrow, yrow+180))

#------------Broom Game-------------
bg_b1 = pygame.image.load("sprite/racing/bg/mountain.png").convert()
bg_b2 = pygame.image.load("sprite/racing/bg/forest1.jpg").convert()
bg_b3 = pygame.image.load("sprite/racing/bg/library.jpg").convert()
bg_b4 = pygame.image.load("sprite/racing/bg/forest1.jpg").convert()

#------------Sound---------------
bgm_1 = pygame.mixer.Sound("sound/forest.mp3"); bgm_1.set_volume(1.0)
bgm_2 = pygame.mixer.Sound("sound/clocktower2.mp3"); bgm_2.set_volume(1.0)
bgm_3 = pygame.mixer.Sound("sound/library.mp3"); bgm_3.set_volume(1.0)
crash = pygame.mixer.Sound("sound/crash.mp3"); crash.set_volume(1.0)

bg_scrolling_b = 0
stage_b = 0

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

class mon:
    def __init__(self, posx, posy, monster):
        self.posx_rs = posx
        self.posy_rs = posy
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
                crash.play()
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
        if heartb <= 0 or timeb <= 2:
            self.posx = self.posx_rs
            self.posy = self.posy_rs

broomright, nobroom = avilia_b.copy(), avilia_b.copy()

heartimg = pygame.image.load('sprite/racing/heart.png')

clock = readvar('broomgame.txt', 'clock/clock')
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
bird_1b = mon(1280,0,bird); bird_2b = mon(1280,720,bird); bird_3b = mon(1280,0,bird)
bird_4b = mon(1280,720,bird); bird_5b = mon(1280,0,bird)
#--------------------------------------------------------- disco ------------------------------------------------------------
bird01 = mon(1280,10,bird); bird02 = mon(1280,610,bird); bird03 = mon(1280,310,bird)
bird04 = mon(1280,90,bird); bird05 = mon(1280,10,bird); bird06 = mon(1280,10,bird)
bird07 = mon(1280,80,bird); bird08 = mon(1280,610,bird); bird09 = mon(1280,90,bird)
#----------------------------------------------------------- stage 2 ----------------------------------------------------------------
clock1 = mon(1280,310,clock); clock2 = mon(1280,220,clock); clock3 = mon(1280,70,clock)
clock4 = mon(1280,160,clock); clock5 = mon(1280,370,clock); clock6 = mon(1280,600,clock)
clock7 = mon(1280,130,clock); clock8 = mon(1280,130,clock); clock9 = mon(1280,340,clock)
clock10 = mon(1280,250,clock); clock11 = mon(1280,438,clock); clock12 = mon(1280,50,clock); clock13 = mon(1280,150,clock)
clock14 = mon(1280,310,clock); clock15 = mon(1280,600,clock); clock16 = mon(1280,510,clock)
clock17 = mon(1280,84,clock); clock18 = mon(1280,182,clock)
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

#---------------Secret forest--------------------------------
bg_sf = pygame.image.load("sprite/map/secretforest.jpg")
fog = pygame.image.load("sprite/fog.png")
MAGIC_POSITION_X, MAGIC_POSITION_Y = 0, 0
hp_player, fight, MAGICCOUNT = 50, False, 0
CIRCLE_SF = False
gameover_sf = False
cd_fs = 0
cd_fs2 = 0
cd_fs3 = 0
cd_fs4 = 0
cd_fs5 = 0
bgm_sf = pygame.mixer.Sound("sound/secret forest.mp3"); bgm_sf.set_volume(1.0)
roar = pygame.mixer.Sound("sound/roar.mp3"); roar.set_volume(1.0)
bgm_sf2 = pygame.mixer.Sound("sound/secret forest song.mp3"); bgm_sf2.set_volume(1.0)
damage = False
endevent_sf = False

rspell, lspell = readvar('var.txt', 'rspell'), readvar('var.txt', 'lspell')
dspell, uspell = readvar('var.txt', 'dspell'), readvar('var.txt', 'uspell')
magic, deadplayer = readvar('var.txt', 'circle'), readvar('var.txt', 'dead/')
yellow, deadyellow = readvar('monvar.txt', '/yellow'), readvar('monvar.txt', 'deadyellow')

damagewalkr = pygame.image.load("sprite/avilia/damage taken/walkr1.png")
damagewalkl = pygame.image.load("sprite/avilia/damage taken/walkl1.png")
damagewalkd = pygame.image.load("sprite/avilia/damage taken/walkd1.png")
damagewalku = pygame.image.load("sprite/avilia/damage taken/walku1.png")

for i in range(9):
    avilia_walkr[i] = pygame.transform.scale(avilia_walkr[i], (int(width*0.07), int(height*0.13)))
    avilia_walkl[i] = pygame.transform.scale(avilia_walkl[i], (int(width*0.07), int(height*0.13)))
    avilia_walkd[i] = pygame.transform.scale(avilia_walkd[i], (int(width*0.07), int(height*0.13)))
    avilia_walku[i] = pygame.transform.scale(avilia_walku[i], (int(width*0.07), int(height*0.13)))
    damagewalkr = pygame.transform.scale(damagewalkr, (int(width*0.07), int(height*0.13)))
    damagewalkl = pygame.transform.scale(damagewalkl, (int(width*0.07), int(height*0.13)))
    damagewalkd = pygame.transform.scale(damagewalkd, (int(width*0.07), int(height*0.13)))
    damagewalku = pygame.transform.scale(damagewalku, (int(width*0.07), int(height*0.13)))
    rspell[i] = pygame.transform.scale(rspell[i], (int(width*0.07), int(height*0.13)))
    lspell[i] = pygame.transform.scale(lspell[i], (int(width*0.07), int(height*0.13)))

def redrawMagic(wall=[(0,0,0,0)]):
    """blit magic"""
    global MAGICCOUNT
    global WALK_AVI
    global CIRCLE_SF
    global MAGIC_POSITION_X
    global MAGIC_POSITION_Y

    if MAGICCOUNT + 1 >= 17:
        MAGICCOUNT, WALK_AVI = 0, 0
        MAGIC_POSITION_X , MAGIC_POSITION_Y = 0, 0
        CIRCLE_SF = False
        showmagic = True
    elif MAGICCOUNT < 17:
        if CHECK == 'RIGHT':
            MAGIC_POSITION_X = PLAYER_POSITION_X+125
            MAGIC_POSITION_Y = PLAYER_POSITION_Y-30
            # win.blit(magic[MAGICCOUNT], (MAGIC_POSITION_X, MAGIC_POSITION_Y))
        elif CHECK == 'LEFT':
            MAGIC_POSITION_X = PLAYER_POSITION_X-235
            MAGIC_POSITION_Y = PLAYER_POSITION_Y-30
            # win.blit(magic[MAGICCOUNT], (MAGIC_POSITION_X, MAGIC_POSITION_Y))
        elif CHECK == 'UP':
            MAGIC_POSITION_X = PLAYER_POSITION_X-55
            MAGIC_POSITION_Y = PLAYER_POSITION_Y-200
            # win.blit(magic[MAGICCOUNT], (MAGIC_POSITION_X, MAGIC_POSITION_Y))
        elif CHECK == 'DOWN':
            MAGIC_POSITION_X = PLAYER_POSITION_X-55
            MAGIC_POSITION_Y = PLAYER_POSITION_Y+100
            # win.blit(magic[MAGICCOUNT], (MAGIC_POSITION_X, MAGIC_POSITION_Y))
        for i,j,k,l in wall:
            if CHECK == "UP":
                l -= 80
            if CHECK == "DOWN":
                k += 90
            if i < MAGIC_POSITION_X+100 < j and k < MAGIC_POSITION_Y+100 < l:
                showmagic = False
                break
            else:
                showmagic = True 
        print("magic", MAGIC_POSITION_X+100, MAGIC_POSITION_Y+100)
        print("i=",i,"j=",j,"k=",k,"l=",l)
        if showmagic:
            win.blit(magic[MAGICCOUNT], (MAGIC_POSITION_X, MAGIC_POSITION_Y))
    MAGICCOUNT += 1

def redrawDead():
    """blit the main character dead"""
    global WALK_AVI
    if WALK_AVI >= 9:
        win.blit(deadplayer[8], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
    else:
        win.blit(deadplayer[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
    WALK_AVI += 1

def redrawGameWindow_sefor():
    """blit the main character"""
    global WALK_AVI
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    global damage

    if WALK_AVI + 1 >= 9 and gameover_sf != True and CIRCLE_SF != True: #กัน out of range
        WALK_AVI = 0
    if RIGHT and CIRCLE_SF == False:
        win.blit(avilia_walkr[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALK_AVI += 1
    elif LEFT and CIRCLE_SF == False:
        win.blit(avilia_walkl[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALK_AVI += 1
    elif DOWN and CIRCLE_SF == False:
        win.blit(avilia_walkd[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALK_AVI += 1
    elif UP and CIRCLE_SF == False:
        win.blit(avilia_walku[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALK_AVI += 1
    elif CIRCLE_SF:
        if WALK_AVI >= 9:
            WALK_AVI = 8
        if CHECK == 'RIGHT':
            win.blit(rspell[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'LEFT':
            win.blit(lspell[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'DOWN':
            win.blit(dspell[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'UP':
            win.blit(uspell[WALK_AVI], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALK_AVI += 1
    elif not RIGHT and not LEFT and not DOWN and not UP:
        if CHECK == 'RIGHT':
            win.blit(avilia_walkr[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'LEFT':
            win.blit(avilia_walkl[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'DOWN':
            win.blit(avilia_walkd[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'UP':
            win.blit(avilia_walku[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
    if damage and not CIRCLE_SF:
        if CHECK == 'RIGHT':
            win.blit(damagewalkr, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'LEFT':
            win.blit(damagewalkl, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'DOWN':
            win.blit(damagewalkd, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'UP':
            win.blit(damagewalku, (PLAYER_POSITION_X, PLAYER_POSITION_Y))

def secretfor(wall=[(0,0,0,0)]):
    """secret forest map"""
    global X
    global Y
    global CHECK
    global RIGHT
    global LEFT
    global DOWN
    global UP
    global CIRCLE_SF
    global WALK_AVI
    global PLAYER_RADIUS
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    global cd_foot

    if keys[pygame.K_SPACE] and gameover_sf == False and fight == True and CIRCLE_SF == False:
        CIRCLE_SF = True
        foot.stop()
        pygame.mixer.Sound.play(c_sound)
        WALK_AVI = 0
    elif keys[pygame.K_a] and X > vel and gameover_sf == False and CIRCLE_SF == False:
        for i,j,k,l in wall:
            if i < X < j and k < Y < l-15:
                adam = 0
                break
            else:
                adam = vel
        # print(i,j,k,l)
        X -= adam
        RIGHT = False
        LEFT = True
        UP = False
        DOWN = False
        CHECK = 'LEFT'
        if cd_foot > 10:
            foot.play(maxtime=500)
            cd_foot = -2
        cd_foot += 1
    elif keys[pygame.K_d] and gameover_sf == False and CIRCLE_SF == False:
        for i,j,k,l in wall:
            if i-15 < X < j-15 and k < Y < l-15:
                adam = 0
                break
            else:
                adam = vel
        # print(i,j,k,l)
        X += adam
        RIGHT = True
        LEFT = False
        UP = False
        DOWN = False
        CHECK = 'RIGHT'
        if cd_foot > 10:
            foot.play(maxtime=500)
            cd_foot = -2
        cd_foot += 1
    elif keys[pygame.K_s] and gameover_sf == False and CIRCLE_SF == False:
        for i,j,k,l in wall:
            if i < X < j-15 and k-15 < Y < l-15:
                adam = 0
                break
            else:
                adam = vel
        # print(i,j,k,l)
        Y += adam
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = True
        CHECK = 'DOWN'
        if cd_foot > 10:
            foot.play(maxtime=500)
            cd_foot = -2
        cd_foot += 1
    elif keys[pygame.K_w] and gameover_sf == False and CIRCLE_SF == False:
        for i,j,k,l in wall:
            if i < X < j-15 and k < Y < l:
                adam = 0
                break
            else:
                adam = vel
        # print(i,j,k,l)
        Y -= adam
        RIGHT = False
        LEFT = False
        UP = True
        DOWN = False
        CHECK = 'UP'
        if cd_foot > 10:
            foot.play(maxtime=500)
            cd_foot = -2
        cd_foot += 1
    else:
        RIGHT = False
        LEFT = False
        UP = False
        DOWN = False
        foot.stop()
    scrolling()

class monf:
    def __init__(self, posx, posy, monter, deadani, num):
        self.posx = posx
        self.posy = posy
        self.count = num
        self.dead = False
        self.hp = 65
        self.monter = monter
        self.deadani = deadani
        self.birth = False
        self.roar = True

    def redrawmonster(self):
        if self.dead == False:
            if self.count + 1 >= 9: #กัน out of range
                self.count = 0
            if self.posx >= PLAYER_POSITION_X+15:
                self.posx -= 5
            if self.posx <= PLAYER_POSITION_X+15:
                self.posx += 5
            if self.posy >= PLAYER_POSITION_Y+25:
                self.posy -= 5
            if self.posy <= PLAYER_POSITION_Y+50:
                self.posy += 5
            win.blit(self.monter[self.count], (self.posx, self.posy))
        elif self.dead:
            if self.count <= 8:
                pygame.time.delay(10)
                win.blit(self.deadani[self.count], (self.posx, self.posy))
            # else:
            #     self.posx, self.posy = 242, 242
        self.count += 1

    def spawn(self):
        global PLAYER_POSITION_X
        global PLAYER_POSITION_Y
        global MAGIC_POSITION_X
        global MAGIC_POSITION_Y
        global fight
        global hp_player
        global gameover_sf
        global CIRCLE_SF
        global WALK_AVI
        global damage

        self.birth = True

        if self.roar:
            roar.play()
            self.roar = False

        if -15 <= self.posy-PLAYER_POSITION_Y <= 60 and self.dead == False and \
        abs(self.posx-PLAYER_POSITION_X) <= 19+5 and fight == True: #ฝั่งลบ มอนสูงกว่าคน
            damage = True
            if hp_player <= 0:
                WALK_AVI = 0
                # self.posx, self.posy = 242, 242
                fight = False
                gameover_sf = True
                CIRCLE_SF = False
            else:
                hp_player -= 0.5

        if abs((MAGIC_POSITION_X+50)-self.posx) <= 50 and \
        abs(MAGIC_POSITION_Y-self.posy) <= 100 and self.dead == False:
            self.hp -= 2
            if self.hp < 0:
                self.count = 0
                self.dead = True

    #     if -15 <= self.posy-PLAYER_POSITION_Y <= 60 and self.dead == False and\
    #    abs(self.posx-PLAYER_POSITION_X) <= 19 and fight == True and CIRCLE_SF == False:
    #         if CHECK == 'RIGHT':
    #             win.blit(damagewalkr, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
    #         elif CHECK == 'LEFT':
    #             win.blit(damagewalkl, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
    #         elif CHECK == 'DOWN':
    #             win.blit(damagewalkd, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
    #         elif CHECK == 'UP':
    #             win.blit(damagewalku, (PLAYER_POSITION_X, PLAYER_POSITION_Y))

    def posyandplay(self):
        return self.posy-PLAYER_POSITION_Y <= 30
    
    def deadmai(self):
        return self.dead

    def birthmai(self):
        return self.birth

yellmon = monf(242, 242, yellow, deadyellow, 0)
yellmon2 = monf(103, 298, yellow, deadyellow, 1)
yellmon3 = monf(1018, 328, yellow, deadyellow, 2)
yellmon4 = monf(583, 208, yellow, deadyellow, 3)
yellmon5 = monf(583, 613, yellow, deadyellow, 4)
#---------------------------------------------------------------------------
"""mainloop"""
bgm_intro.play(-1, maxtime=79000)
while run:
    # pygame.time.delay(30)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_e] and (PLAY_MAIN or PLAY_SEFOR) and not play_pz and checkpoint >= 4:
            openbook = True

    if PLAY_MAIN:
        pygame.time.delay(45)
    #--------------hallway-01--------------
        if idmap == "01": #HALLWAY
            wall(walls["hallway"])
            sub_hallways_01.walkrl(1141, 1697)
            idmap, change = changemap(0, 1280, 598, 720, 508, 43, idmap, "00", change)
            idmap, change = changemap(0, 13, 328, 388, 1123, 343, idmap, "11", change)
            idmap, change = changemap(1198, 1280, 0, 720, 33, 163, idmap, "02", change)
            # idmap, change = changemap(0, 1280, 0, 28, X, 583, idmap, "09", change)

            if not change:
                if X >= 628:
                    win.blit(bg ,(-628, rel_y-bg_height))
                elif Y >= 358:
                    win.blit(bg ,(rel_x-bg_width, -358))
                else:
                    win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
                bg.blit(bg2 ,(0, 0))
                if 0 <= Y <= 43:
                    redrawicon("door", X+70, Y)
                    if keys[pygame.K_f]:
                        bgm_opendoor.play(maxtime=1400)
                        CHECK = "UP"
                        idmap, change = changemap(0, 1280, 0, 43, X, 583, idmap, "09", change)

            change = False
    #--------------canteen-02--------------
        elif idmap == "02": #CANTEEN
            wall(walls["canteen"])
            sub_canteen_01.walkrl(775,1197)
            if X >= 1203:
                X = 28
                Y = 463
                stage_height = 720
                bg = pygame.image.load("sprite/map/eastcorridor_1.jpg")
                bg2 = pygame.image.load("sprite/map/eastcorridor_1.jpg")
                idmap = "03"
                bgm_canteen.stop()
                bgm_hall.set_volume(0.4)
                bgm_corridor.play(-1)
            elif Y >= 778 and Y <= 838 and X >= 828:
                X = 28
                Y = 223
                stage_height = 720
                bg = pygame.image.load("sprite/map/eastgarden.jpg")
                bg2 = pygame.image.load("sprite/map/eastgarden.jpg")
                idmap = "08"
                bgm_hall.stop()
                bgm_canteen.stop()
                bgm_garden.play(-1).set_volume(0.7)
            elif X <= 13 and Y >= 148 and Y <= 163:
                X = 1168
                Y = 238
                stage_height = 720
                bg = pygame.image.load("sprite/map/hallway.jpg")
                bg2 = pygame.image.load("sprite/map/hallway.jpg")
                idmap = "01"
                bgm_canteen.stop()
                bgm_hall.set_volume(1.0)
            elif X >= 798 and Y >= 283 and Y <= 598:
                stage_height = 720
                win.blit(bg ,(-453, -283))
            elif X >= 453:
                stage_height = 950
                win.blit(bg ,(-453, rel_y-bg_height))
            else:
                stage_height = 950
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
            bg.blit(bg2 ,(0, 0))
            if 918 <= X <= 1098 and 88 <= Y <= 118 and checkpoint >= 4 and not prize_pz:
                redrawicon("hand", X+20, Y-50)
                if keys[pygame.K_f]:
                    safe += 1
    #--------------eastcor1-03-------------
        elif idmap == "03":
            wall(walls["eastcor1"])
            idmap, change = changemap(0,13,0,720,1108,478,idmap,"02", change)
            idmap, change = changemap(0,1280,0,13,X,583,idmap,"04", change)
            idmap, change = changemap(0,1280,628,1280,388,28,idmap,"08", change)
            if not change:
                bg.blit(bg2 ,(0, 0))
                if Y >= 178:
                    win.blit(bg ,(-28, -178))
                else:
                    win.blit(bg ,(-28, rel_y-bg_height))
            if 1138 <= X <= 1198 and 463 <= Y < 523:
                redrawicon("door", X+27, Y-50)
                if keys[pygame.K_f]:
                    bgm_hall.stop()
                    bgm_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/map/classroom.jpg")
                    bg2 = pygame.image.load("sprite/map/classroom.jpg")
                    X = 58
                    Y = 268
                    idmap = "05"
                    CHECK = "RIGHT"
            if 1138 <= X <= 1198 and 103 <= Y < 148:
                redrawicon("door", X+27, Y-50)
                if keys[pygame.K_f]:
                    bgm_hall.stop()
                    bgm_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/map/classroom.jpg")
                    bg2 = pygame.image.load("sprite/map/classroom.jpg")
                    X = 58
                    Y = 268
                    idmap = "06"
                    CHECK = "RIGHT"
            change = False
    #--------------eastcor2-04-------------
        elif idmap == "04":
            wall(walls["eastcor2"])
            idmap, change = changemap(0,1280,632,1280,X,28,idmap,"03", change)
            idmap, change = changemap(0,1280,0,13,1123,613,idmap,"19", change)
            # idmap, change = changemap(0,13,0,720,1123,343,idmap,"10", change)
            if not change:
                win.blit(bg ,(-28, -13))
                if 0 <= X <= 13:
                    redrawicon("door", X+27, Y-50)
                    if keys[pygame.K_f]:
                        bgm_opendoor.play(maxtime=1400)
                        CHECK = "LEFT"
                        idmap, change = changemap(0,13,0,720,1123,343,idmap,"10", change)
            if 1138 <= X <= 1198 and 328 <= Y <= 373:
                redrawicon("door", X+27, Y-50)
                if keys[pygame.K_f]:
                    bgm_hall.stop()
                    bgm_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/map/classroom.jpg")
                    bg2 = pygame.image.load("sprite/map/classroom.jpg")
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
                redrawicon("door", X+27, Y-50)
                if keys[pygame.K_f]:
                    bgm_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/map/eastcorridor_1.jpg")
                    bg2 = pygame.image.load("sprite/map/eastcorridor_1.jpg")
                    X = 1093
                    Y = 493
                    idmap = "03"
                    CHECK = "LEFT"
                    bgm_hall.play(-1,fade_ms=5000)
    #--------------classroom2-06-------------
        elif idmap == "06":
            wall(walls["classroom"])

            win.blit(bg ,(-238, -118))
            if 13 <= X <= 28 and 253 <= Y < 283:
                redrawicon("door", X+27, Y-50)
                if keys[pygame.K_f]:
                    bgm_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/map/eastcorridor_1.jpg")
                    bg2 = pygame.image.load("sprite/map/eastcorridor_1.jpg")
                    X = 1093
                    Y = 133
                    idmap = "03"
                    CHECK = "LEFT"
                    bgm_hall.play(-1,fade_ms=5000)
    #--------------classroom3-07-------------
        elif idmap == '07':
            wall(walls["classroom"])

            win.blit(bg ,(-238, -118))
            if 13 <= X <= 28 and 253 <= Y < 283:
                redrawicon("door", X+27, Y-50)
                if keys[pygame.K_f]:
                    bgm_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/map/eastcorridor_2.jpg")
                    bg2 = pygame.image.load("sprite/map/eastcorridor_2.jpg")
                    X = 1093
                    Y = 358
                    idmap = "04"
                    CHECK = "LEFT"
                    bgm_hall.play(-1,fade_ms=5000)
    #--------------eastgarden-08-----------
        elif idmap == "08":
            wall(walls["eastgar"])
            sub_eastgar_01.walkrl(216, 1581)
            if X <= 13:
                bg = pygame.image.load("sprite/map/canteen.jpg")
                bg2 = pygame.image.load("sprite/map/canteen.jpg")
                stage_height = 950
                X = 813
                Y = 823
                idmap = "02"
                bgm_garden.stop()
                bgm_hall.play(-1).set_volume(0.4)
                bgm_canteen.play(-1)
            elif Y <= 13:
                bg = pygame.image.load("sprite/map/eastcorridor_1.jpg")
                bg2 = pygame.image.load("sprite/map/eastcorridor_1.jpg")
                X = 433
                Y = 613
                idmap = "03"
                bgm_garden.stop()
                bgm_hall.play(-1).set_volume(0.4)
                bgm_corridor.play(-1)
            else:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
                bg.blit(bg2 ,(0, 0))
                if checkpoint >= 4 and "puzzlepaper5" not in item:
                    bg.blit(paper2, (1700, 300))
                    if 808 <= X <= 838 and 118 <= Y <= 163:
                        redrawicon("hand", X+20, Y-50)
                        if keys[pygame.K_f] and ("puzzlepaper5" not in item):
                            item.append("puzzlepaper5")
                            what_paper = paper_bnwbklu.copy()
    #--------------firstaid-09-------------
        elif idmap == "09": #FIRSTAID ROOM
            wall(walls["firstaid"])
            # idmap,change = changemap(0,1280,613,1280,253,43,idmap,"01", change)
            # idmap,change = changemap(1207,1280,0,720,28,373,idmap,"10", change)
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
                if 598 <= Y <= 720:
                    redrawicon("door", X+27, Y-50)
                    if keys[pygame.K_f]:
                        bgm_opendoor.play(maxtime=1400)
                        CHECK = "DOWN"
                        idmap,change = changemap(0,1280,598,1280,253,58,idmap,"01", change)
                if 1183 <= X <= 1280:
                    redrawicon("door", X+27, Y-50)
                    if keys[pygame.K_f]:
                        bgm_opendoor.play(maxtime=1400)
                        CHECK = "RIGHT"
                        idmap,change = changemap(1183,1280,0,720,43,373,idmap,"10", change)
            change = False
            if STORY4 and not play_dialog:
                if not play_cutscene:
                    fadeout()
                    play_cutscene = True
                    idmap, countd = "21", 62
                    bg = pygame.image.load('sprite/map/teacherroomcutscene.jpg')
                    lstdialog = readvar('dialog.txt', '')
                    POSX_VEN, POSY_VEN = 1300, 325
                    POSX_H, POSY_H = 435, 255
                    fadein(bg, -238, -118)
            if (X == 28 and Y <= 253) or (73 <= X <= 88 and Y <= 253):
                if not play_dialog and checkpoint >= 4:
                    redrawicon("chat", X+20, Y-50)
                    if keys[pygame.K_f] and checkpoint >= 4:
                        if 'potion' not in item or 'magicpowder' not in item or 'applescrap' not in item:
                            lstdialog = ['Esme : If you forget the details of the ingredients, You can press E to see it']
                        if 'potion' in item and 'magicpowder' in item and 'applescrap' in item:
                            lstdialog = ['Avilia : Take it. These are the ingredients that you want.',
                                         'Esme : Thank you Avilia, You saved my life! I will definitely repay you.',
                                         'Avilia : I hope I become your best friend Esme.',
                                         "Esme : Of course, from now on, we've been best friends"]
                            STORY4 = True
                        play_dialog, ANIM, countdnpc = True, 0, 0
                if play_dialog:
                    redrawdialog(countdnpc)
                    if keys[pygame.K_SPACE] and counttxt >= len(lstdialog[countdnpc].split(':')[1])-1:nextdia = True
                    elif nextdia:
                        if countdnpc >= len(lstdialog)-1:countdnpc, ANIM, play_dialog = 0, 0, False
                        if not keys[pygame.K_SPACE] and play_dialog:countdnpc += 1
                        if lstdialog[countdnpc-1].split()[0] != lstdialog[countdnpc].split()[0] and play_dialog:ANIM = 0
                        counttxt, posx_txt, posy_txt = 0, 205, 80
                        dialogbox[9] = pygame.image.load('sprite/dialog/dialogbox10.png')
                        nextdia = False
            if not STORY3:
                if BLACK > 0:
                    BLACK -= 4
                if BLACK <= 0 and checkpoint == 3:
                    checkpoint, CHECK = 4, 'DOWN'
                    fadeout()
                    bg = pygame.image.load('sprite/map/firstaidroom_esme.jpg')
                    bg2 = pygame.image.load('sprite/map/firstaidroom_esme.jpg')
                    fadein(bg, -28, -13)
                    play_cutscene = False
                    X, Y = 28, 238
                redrawblack()
            if STORY3:
                if BLACK < 100:
                    BLACK += 4
                redrawblack()
                cutscene()
    #---------------battle-10--------------
        elif idmap == "10": #BATTLE ROOM
            wall(walls["battle"])
            # idmap, change = changemap(0,13,0,720,1168,493,idmap,"09", change)
            # idmap, change = changemap(1222,1280,0,720,28,373,idmap,"04", change)
            if not change:
                if X >= 523 and Y >= 103:
                    win.blit(bg ,(-523, -103))
                elif Y >= 103:
                    win.blit(bg ,(rel_x-bg_width, -103))
                elif X >= 523:
                    win.blit(bg ,(-523, -103))
                else:
                    win.blit(bg ,(rel_x-bg_width, -103))
                if 0 <= X <= 28 and 298 <= Y <= 463:
                    redrawicon("door", X+27, Y-50)
                    if keys[pygame.K_f]:
                        bgm_opendoor.play(maxtime=1400)
                        CHECK = "LEFT"
                        idmap, change = changemap(0,28,298,463,1168,493,idmap,"09", change)
                if 1198 <= X <= 1280:
                    redrawicon("door", X+27, Y-50)
                    if keys[pygame.K_f]:
                        bgm_opendoor.play(maxtime=1400)
                        CHECK = "RIGHT"
                        idmap,change = changemap(1198,1280,0,720,28,373,idmap,"04", change)
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
                    POSX_AVI, POSY_AVI, WALK_AVI = 1280, 343, 0
                    play_cutscene = True
                    fadeout()
                    fadein(bg, -1108, -313)
                if BLACK < 100:
                    BLACK += 4
                win.blit(bg ,(-1108, -313))
                redrawblack()
                cutscene()
            if not change and not play_cutscene:
                sub_path_01.walkrl(538, 2419)
                if (X <= 598 and Y >= 313) or (X <= 598 and Y < 313):
                    win.blit(bg ,(-598, -313))
                elif X >= 1108:
                    win.blit(bg ,(-1108, -313))
                elif Y < 313 or Y >= 313:
                    win.blit(bg ,(rel_x-bg_width, -313))
                bg.blit(bg2 ,(0, 0))
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
                bg.blit(bg2 ,(0, 0))
                if checkpoint >= 4 and "puzzlepaper4" not in item:
                    bg.blit(paper2, (879, 240))
                    if 388 <= X <= 463 and 0 <= Y <= 103:
                        redrawicon("hand", X+20, Y-50)
                        if keys[pygame.K_f] and ("puzzlepaper4" not in item):
                            item.append("puzzlepaper4")
                            what_paper = paper_901502.copy()
                    
            change = False
    #--------------entryhall-00------------
        elif idmap == "00":
            if checkpoint >= 4:
                wall(walls["entryhall"])
            else:
                wall(walls["entryhall_2"])
            if music:
                bgm_hall.play(-1)
                music = False
            sub_entryhalls_01.walkrl(422, 906)
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
                bg.blit(bg2 ,(0, 0))
                if checkpoint >= 4 and "puzzlepaper3" not in item:
                    bg.blit(paper1, (860, 800))
                    if 418 <= X <= 448 and 418 <= Y <= 508:
                        redrawicon("hand", X+20, Y-50)
                        if keys[pygame.K_f] and ("puzzlepaper3" not in item):
                            item.append("puzzlepaper3")
                            what_paper = paper_b1.copy()
            change = False
    #----------------hall-13---------------
        elif idmap == "13":
            wall(walls["hall"])
            sub_halls_01.walkrl(641,905)
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
                bg.blit(bg2 ,(0, 0))
            change = False
    #-------------westgarden-14------------
        elif idmap == "14":
            wall(walls["westgar"])
            sub_wastgar_01.walkrl(893, 1571)
            idmap, change = changemap(1207,1280,0,720,73,Y,idmap,"13", change)
            idmap, change = changemap(0,1280,0,13,748,613,idmap,"15", change)
            if not change:
                win.blit(bg ,(rel_x-bg_width, rel_y-bg_height))
                bg.blit(bg2 ,(0, 0))
                if checkpoint >= 4 and "puzzlepaper2" not in item:
                    bg.blit(paper1, (793, 300))
                    if 352 <= X <= 412 and 118 <= Y <= 163:
                        redrawicon("hand", X+20, Y-50)
                        if keys[pygame.K_f] and ("puzzlepaper2" not in item):
                            item.append("puzzlepaper2")
                            what_paper = paper_blackcathate.copy()
            change = False
    #--------------westcor1-15-------------
        elif idmap == "15":
            if checkpoint >= 4:
                wall(walls["westcor1"])
            else:
                wall(walls["westcor1_close"])
            sub_wastcor1_01.walkrl(598, 808)
            idmap, change = changemap(0,1280,628,720,832,28,idmap,"14", change)
            idmap, change = changemap(0,1280,0,13,X,502,idmap,"16", change)
            idmap,change = changemap(1198,1280,0,720,28,343,idmap,"11", change)
            if not change:
                if Y >= 365:
                    win.blit(bg ,(-28, -365))
                else:
                    win.blit(bg ,(-28, rel_y-bg_height))
                if 13 <= X <= 28 and 313 <= Y < 388:
                    redrawicon("door", X+27, Y-50)
                    if keys[pygame.K_f]:
                        bgm_hall.stop()
                        bgm_opendoor.play(maxtime=1400)
                        bg = pygame.image.load("sprite/map/apothecaryroom.jpg")
                        bg2 = pygame.image.load("sprite/map/apothecaryroom.jpg")
                        X = 973
                        Y = 373
                        idmap = "20"
                        CHECK = "LEFT"
                if 13 <= X <= 28 and 103 <= Y < 163:
                    redrawicon("door", X+27, Y-50)
                    if keys[pygame.K_f]:
                        bgm_hall.stop()
                        bgm_opendoor.play(maxtime=1400)
                        bg = pygame.image.load("sprite/map/teacherroom.jpg")
                        bg2 = pygame.image.load("sprite/map/teacherroom.jpg")
                        X = 958
                        Y = 313
                        idmap = "21"
                        CHECK = "LEFT"
                if 373 <= X <= 433 and 313 <= Y <= 358 and checkpoint == 4:
                    if not play_dialog and 'potion' not in item:
                        redrawicon("chat", X+20, Y-50)
                        if keys[pygame.K_f]:
                            if not finish_ph1 or not finish_ph2 or not finish_ph3:
                                lstdialog = ['Avilia : sorry for bothering, But do you have any potion left over for me?',
                                             'Stella : There is enough potion at the Academy for every student.',
                                             'Avilia : Could you please give me?',
                                             'Stella : Sure, but you have to clean all the left-wing rooms in the west hall.',
                                             "Avilia : All right, if you're really going to give that to me."]
                            if finish_ph1 and finish_ph2 and finish_ph3:
                                lstdialog = ["Stella : You did great, Now it's yours"]
                                if 'potion' not in item:
                                    item.append('potion')
                                    alpha = 255
                            play_dialog, ANIM, countdnpc = True, 0, 0
                    if play_dialog:
                        redrawdialog(countdnpc)
                        if keys[pygame.K_SPACE] and counttxt >= len(lstdialog[countdnpc].split(':')[1])-1:nextdia = True
                        elif nextdia:
                            if countdnpc >= len(lstdialog)-1:countdnpc, ANIM, play_dialog = 0, 0, False
                            if not keys[pygame.K_SPACE] and play_dialog:countdnpc += 1
                            if lstdialog[countdnpc-1].split()[0] != lstdialog[countdnpc].split()[0] and play_dialog:ANIM = 0
                            counttxt, posx_txt, posy_txt = 0, 205, 80
                            dialogbox[9] = pygame.image.load('sprite/dialog/dialogbox10.png')
                            nextdia = False
                bg.blit(bg2 ,(0, 0))
            change = False
    #--------------westcor2-16-------------
        elif idmap == "16":
            if checkpoint >= 4:
                wall(walls["westcor2"])
            else:
                wall(walls["westcor2_close"])
            idmap ,change = changemap(0,1280,613,720,X,103,idmap,"15", change)
            idmap , change = changemap(0,1280,0,13,43,598,idmap,"17", change)

            if not change:
                if Y >= 73:
                    win.blit(bg ,(-28, -73))
                else:
                    win.blit(bg ,(-28, rel_y-bg_height))
                if 13 <= X <= 28 and 208 <= Y < 358:
                    redrawicon("door", X+27, Y-50)
                    if keys[pygame.K_f]:
                        bgm_hall.stop()
                        bgm_opendoor.play(maxtime=1400)
                        bg = pygame.image.load("sprite/map/researchroom.jpg")
                        bg2 = pygame.image.load("sprite/map/researchroom.jpg")
                        X = 973
                        Y = 373
                        idmap = "22"
                        CHECK = "LEFT"
            change = False
    #-------------westforest-17------------
        elif idmap == "17":
            
            wall(walls["westfor"])
            sub_wastforest_01.walkrl(240,697)
            idmap ,change = changemap(0,1280,628,720,598,28,idmap,"16", change)
            idmap, change = changemap(1213,1280,0,720,28,418,idmap,"18", change)
            if not change:
                if X >= 583:
                    win.blit(bg ,(-583, -58))
                else:
                    win.blit(bg ,(rel_x-bg_width, -58))
                bg.blit(bg2 ,(0, 0))
            change = False
    #--------------forest-18---------------
        elif idmap == "18":
            if checkpoint >= 4:
                wall(walls["forestblood"])
            else:
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
                if checkpoint >= 4:
                    if 418 <= X <= 463 and 238 <= Y <= 268:
                        redrawicon("door", X+27, Y-50)
                        if keys[pygame.K_f]:
                            PLAY_SEFOR = True
                            PLAY_MAIN = False
                            X = 583
                            Y = 583
                            CHECK = "UP"
                            bg = pygame.image.load("sprite/map/secretforest.jpg")
                            bg2 = pygame.image.load("sprite/map/secretforest.jpg")
                            bgm_garden.stop()
                            bgm_sf.play(-1)

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
            sub_eastforest_01.walkrl(853, 1446)
            idmap ,change = changemap(0,13,0,720,1198,418,idmap,"18", change)
            idmap,change = changemap(0,1280,628,720,598,28,idmap,"04", change)

            if X <= 13:
                bg = pygame.image.load("sprite/map/forest.jpg")
                bg2 = pygame.image.load("sprite/map/forest.jpg")
                X = 1198
                Y = 418
                idmap = "18"
            elif Y >= 628:
                bg = pygame.image.load("sprite/map/eastcorridor_2.jpg")
                bg2 = pygame.image.load("sprite/map/eastcorridor_2.jpg")
                X = 598
                Y = 28
                idmap = "04"
            if not change:
                if X >= 583:
                    win.blit(bg ,(-583, -58))
                else:
                    win.blit(bg ,(rel_x-bg_width, -58))
                bg.blit(bg2 ,(0, 0))
            change = False
    #------------apothecaryroom-20----------
        elif idmap == "20":
            if finish_ph1:
                wall(walls['apothecaryroom_nobucket'])
            else:
                wall(walls['apothecaryroom'])
            win.blit(bg ,(-238, -118))

            if 1168 <= X <= 1280 and 298 <= Y < 433:
                redrawicon("door", X+27, Y-50)
                if keys[pygame.K_f]:
                    bgm_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/map/westcorridor_1.jpg")
                    bg2 = pygame.image.load("sprite/map/westcorridor_1.jpg")
                    X = 58
                    Y = 343
                    idmap = "15"
                    CHECK = "RIGHT"
                    bgm_hall.play(-1,fade_ms=5000)
            if not finish_ph1:
                win.blit(bucket, (673, 403))
                if 613 <= X <= 718 and 283 <= Y <= 463:
                    redrawicon("hand", X+20, Y-50)
                    if keys[pygame.K_f]:
                        PLAY_PH1 = True
                        PLAY_MAIN = False
            if not STORY5 and checkpoint == 6:
                fadeout()
                X, Y = 1153, 373
                checkpoint = 7
                bg = pygame.image.load('sprite/map/apothecaryroomcutscene2.jpg')
                fadein(bg, -238, -118)
            if STORY5:
                cutscene()
    #------------teacherroom-21-------------
        elif idmap == "21":
            if finish_ph3:
                wall(walls['teacherroom_nobucket'])
            else:
                wall(walls['teacherroom'])

            win.blit(bg ,(-238, -118))
            if 1168 <= X <= 1630 and 298 <= Y < 433:
                redrawicon("door", X+27, Y-50)
                if keys[pygame.K_f]:
                    bgm_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/map/westcorridor_1.jpg")
                    bg2 = pygame.image.load("sprite/map/westcorridor_1.jpg")
                    X = 58
                    Y = 133
                    idmap = "15"
                    CHECK = "RIGHT"
                    bgm_hall.play(-1,fade_ms=5000)
            # win.fill((0,0,255), rect=[800,433,50,50])
            if not finish_ph3:
                win.blit(bucket, (808, 373))
                if 763 <= X <= 853 and 283 <= Y <= 358:
                    redrawicon("hand", X+20, Y-50)
                    if keys[pygame.K_f]:
                        PLAY_PH3 = True
                        PLAY_MAIN = False
            if STORY4:
                cutscene()
            if not STORY4 and checkpoint == 5:
                fadeout()
                STORY5, play_dialog = True, True
                idmap, countd = "20", 70
                POSX_ESME, POSY_ESME, WALK_ESME = 320, 290, 8
                POSX_VEN, POSY_VEN, WALK_VEN = 480, 290, 0
                bg = pygame.image.load('sprite/map/apothecaryroomcutscene.jpg')
                fadein(bg, -238, -118)
    #------------researchroom-22------------
        elif idmap == "22":
            if finish_ph2:
                wall(walls['researchroom_nobucket'])
            else:
                wall(walls['researchroom'])

            win.blit(bg ,(-238, -118))
            if 1168 <= X <= 1630 and 358 <= Y < 433:
                redrawicon("door", X+27, Y-50)
                if keys[pygame.K_f]:
                    bgm_opendoor.play(maxtime=1400)
                    bg = pygame.image.load("sprite/map/westcorridor_2.jpg")
                    bg2 = pygame.image.load("sprite/map/westcorridor_2.jpg")
                    X = 58
                    Y = 298
                    idmap = "16"
                    CHECK = "RIGHT"
                    bgm_hall.play(-1,fade_ms=5000)
            # win.fill((0,0,255), rect=[223,450,50,50])
            if not finish_ph2:
                win.blit(bucket, (448, 493))
                if 403 <= X <= 493 and 313 <= Y <= 388:
                    redrawicon("hand", X+20, Y-50)
                    if keys[pygame.K_f]:
                        PLAY_PH2 = True
                        PLAY_MAIN = False
        if not play_cutscene:
            redrawGameWindow()
        if item == [] and checkpoint >= 4 and not play_cutscene:
            redrawobtain('press E to open your book', 'or press F to interact')
        if 'puzzlepaper1' in item or 'puzzlepaper2' in item or 'puzzlepaper3' in item or 'puzzlepaper4' in item or 'puzzlepaper5' in item:
            redrawobtain('you obtain', 'a puzzle paper')
        if 'magicpowder' in item and idmap != "15" and idmap != "20" and idmap != "21" and idmap != "22" and not play_cutscene:
            redrawobtain('you obtain', 'a magic powder')
        if 'potion' in item and idmap != "02" and not play_cutscene:
            redrawobtain('you obtain', 'a potion')

#-----------------Photohunt--------------------
    elif PLAY_PH1:
        pygame.time.delay(30)
        sec -= 0.05
        if stage == 0:
            bgm_ph1.play(-1)
            stage = 1
            what_paper = paper_ruleph.copy()
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
        if score_value == 7:
            fadeout(200)
            bgm_ph1.stop()
            PLAY_PH1 = False ;PLAY_MAIN = True
            finish_ph1 = True
            score_value, sec, health_value, stage = 0, 65, 3, 0
        elif health_value == 0 or sec <= 0:
            fadeout(200)
            bgm_ph1.stop()
            PLAY_PH1 = False ;PLAY_MAIN = True
            bg_ph_1 = pygame.image.load('sprite/photohunt/stage 1.png')
            score_value, sec, health_value, stage = 0, 65, 3, 0
            foundph1_1 = foundph1_2 = foundph1_3 = foundph1_4 = foundph1_5 = foundph1_6 = foundph1_7 = 1

    elif PLAY_PH2:
        pygame.time.delay(30)
        sec -= 0.05
        if stage == 0:
            bgm_ph2.play(-1)
            stage = 1
            what_paper = paper_ruleph.copy()
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
        if score_value == 8:
            fadeout(200)
            bgm_ph2.stop()
            PLAY_PH2 = False ;PLAY_MAIN = True
            finish_ph2 = True
            score_value, sec, health_value, stage = 0, 65, 3, 0
        elif health_value <= 0 or sec <= 0:
            fadeout(200)
            bgm_ph2.stop()
            PLAY_PH2 = False ;PLAY_MAIN = True
            bg_ph_2 = pygame.image.load('sprite/photohunt/stage 2.png')
            score_value, sec, health_value, stage = 0, 65, 3, 0
            foundph2_1 = foundph2_2 = foundph2_3 = foundph2_4 = foundph2_5 = foundph2_6 = foundph2_7 = foundph2_8 = 1

    elif PLAY_PH3:
        pygame.time.delay(30)
        sec -= 0.05
        if stage == 0:
            bgm_ph3.play(-1)
            stage = 1
            what_paper = paper_ruleph.copy()
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
        if score_value == 6:
            fadeout(200)
            bgm_ph3.stop()
            PLAY_PH3 = False ;PLAY_MAIN = True
            finish_ph3 = True
            score_value, sec, health_value, stage = 0, 65, 3, 0
        elif health_value <= 0 or sec <= 0:
            fadeout(200)
            bgm_ph3.stop()
            PLAY_PH3 = False ;PLAY_MAIN = True
            bg_ph_3 = pygame.image.load('sprite/photohunt/stage 3.png')
            score_value, sec, health_value, stage = 0, 65, 3, 0
            foundph3_1 = foundph3_2 = foundph3_3 = foundph3_4 = foundph3_5 = foundph3_6 = 1

#-----------------Broom game-----------------------
    if PLAY_BROOM:
        pygame.time.delay(25)
        bg_scrolling_b -= 1
        timeb = 180
        if timeb >= 180:
            bgm_3.stop()
            bgm_garden.play()
            PLAY_BROOM, idmap, countd = False, "18", 28
            bg = pygame.image.load(mapping[idmap])
            POSX_ESME, POSY_ESME = 500, 400
            POSX_SHE, POSY_SHE = 750, 400
            POSX_AVI, POSY_AVI = -10, 150
            POSX_VEN, POSY_VEN = -10, 400
            POSX_M1, POSY_M1 = 880, 380
            POSX_M2, POSY_M2 = 860, 450
            fadeout()
            PLAY_MAIN, STORY2 = True, True
            fadein(bg, -283, -358)

        elif timeb >= 120:
            if fadebg3 == False:
                fadeout()
                fadebg3 = True
            win.blit(bg_b3, (bg_scrolling_b, 0))
            win.blit(bg_b3, (bg_scrolling_b+1280, 0))
            if stage_b == 2:
                stage_b = 3
                bgm_3.play(-1)
                bgm_2.stop()

        elif timeb >= 60:
            if fadebg2 == False:
                fadeout()
                fadebg2 = True
            win.blit(bg_b2, (bg_scrolling_b, 0))
            win.blit(bg_b2, (bg_scrolling_b+1280, 0))
            if stage_b == 1:
                stage_b = 2
                bgm_2.play(-1)
                bgm_1.stop()
            
        elif timeb >= 0:
            win.blit(bg_b1, (bg_scrolling_b, 0))
            win.blit(bg_b1, (bg_scrolling_b+1280, 0))
            if stage_b == 0:
                stage_b = 1
                bgm_hall.stop()
                bgm_1.play(-1)
                what_paper = paper_rulerc.copy()

            
        if bg_scrolling_b <= -1280:
            bg_scrolling_b = 0
        timeb += 0.05
        # y += 5

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and xb > 10:
            xb -= vel
            leftb = True
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and xb < bg_width-1000:
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
            for _ in range(1000):
                yb -= 15
            fadeout()
            timeb = 0
            heartb = 5
            xb = 50
            yb = 355
        redrawbroomGameWindow()

#-----------------Secret forest-------------------
    if PLAY_SEFOR:
        pygame.time.delay(25)
        secretfor(walls["secretfor"])
        rel_x = -X % bg_width
        rel_y = -Y % bg_height
        cd_fs += 1
        damage = False
        if Y >= 662:
            win.blit(bg ,(-238, -662))
        else:
            win.blit(bg ,(-238, rel_y-bg_height))

        if "applescrap" not in item:
            bg.blit(applescrap, (870, 500))
        if "applescrap" in item:
            redrawobtain('you obtain', 'an apple scrap')
        # print(X, Y)
        # print('PLAYER', PLAYER_POSITION_X, PLAYER_POSITION_Y)
        # print('MONSTER', YELLOW_POS_X, YELLOW_POS_Y)

        if fight and not gameover_sf and not what_paper:
            if CIRCLE_SF:
                redrawMagic(walls["wallmagic"])
            # if YELLOW_POS_Y-PLAYER_POSITION_Y <= 30:
            #     redrawMonster()
            #     redrawGameWindow()
            # else:
            #     redrawGameWindow()
            #     redrawMonster()
            yellmon.spawn()
            if yellmon.deadmai():
                if cd_fs >= 10:
                    yellmon2.spawn()
                    cd_fs2 += 1
                if cd_fs2 >= 100:
                    yellmon3.spawn()
                    cd_fs3 += 1
                if cd_fs3 >= 100:
                    yellmon4.spawn()
                    cd_fs4 += 1
                if cd_fs4 >= 100:
                    yellmon5.spawn()
                    cd_fs5 += 1
            if yellmon.posyandplay() and yellmon.birthmai(): yellmon.redrawmonster()
            if yellmon2.posyandplay() and yellmon2.birthmai(): yellmon2.redrawmonster()
            if yellmon3.posyandplay() and yellmon3.birthmai(): yellmon3.redrawmonster()
            if yellmon4.posyandplay() and yellmon4.birthmai(): yellmon4.redrawmonster()
            if yellmon5.posyandplay() and yellmon5.birthmai(): yellmon5.redrawmonster()
            redrawGameWindow_sefor()
            if not yellmon.posyandplay() and yellmon.birthmai(): yellmon.redrawmonster()
            if not yellmon2.posyandplay() and yellmon2.birthmai(): yellmon2.redrawmonster()
            if not yellmon3.posyandplay() and yellmon3.birthmai(): yellmon3.redrawmonster()
            if not yellmon4.posyandplay() and yellmon4.birthmai(): yellmon4.redrawmonster()
            if not yellmon5.posyandplay() and yellmon5.birthmai(): yellmon5.redrawmonster()

            pygame.draw.rect(win, (250-(hp_player*5), hp_player*5, 0), [390, 40, hp_player*10, 15])

            if all([yellmon.deadmai(), yellmon2.deadmai(), yellmon3.deadmai(), yellmon4.deadmai(), yellmon5.deadmai(), not CIRCLE_SF]):
                fight = False
                endevent_sf = True
                bg = pygame.image.load("sprite/map/secretforest.jpg")
            
        elif gameover_sf:
            redrawDead()
            if WALK_AVI == 15:
                fadeout()
                X, Y = 583, 583
                hp_player = 50
                gameover_sf = False
                fight = False
                damage = False
                yellmon = monf(242, 242, yellow, deadyellow, 0)
                yellmon2 = monf(103, 298, yellow, deadyellow, 1)
                yellmon3 = monf(1018, 328, yellow, deadyellow, 2)
                yellmon4 = monf(583, 208, yellow, deadyellow, 3)
                yellmon5 = monf(583, 613, yellow, deadyellow, 4)
                cd_fs = 0
                cd_fs2 = 0
                cd_fs3 = 0
                cd_fs4 = 0
                cd_fs5 = 0
                CHECK = "UP"
                item.pop()
        else:
            redrawGameWindow_sefor()
        if 538 <= X <= 658 and 208 <= Y <= 253 and not endevent_sf and not fight:
            redrawicon("hand", X+20, Y-50)
            if keys[pygame.K_f] and ("applescrap" not in item):
                what_paper = paper_rulemf.copy()
                fight = True
                alpha = 255
                item.append("applescrap")
                bg = pygame.image.load("sprite/map/secretforest.jpg")

        if not fight:
            if 598 <= Y <= 613:
                redrawicon("door", X+27, Y-50)
                if keys[pygame.K_f]:
                    PLAY_SEFOR = False
                    PLAY_MAIN = True
                    X = 448
                    Y = 358
                    CHECK = "DOWN"
                    bg = bgblood
                    bg2 = bgblood
                    bgm_garden.play(-1)
                    bgm_sf.stop()
                    idmap = "18"

        win.blit(fog ,(-238, rel_y-bg_height))


#-----------------MAIN GAME-----------------------------------------------

    if openbook and (PLAY_MAIN or (PLAY_SEFOR and not fight)) and not play_cutscene:

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

        if (keys[pygame.K_e] or keys[pygame.K_ESCAPE]) and (book_anim == 9 or book_anim == 19 or book_anim == 29):
            backpage, book_map, book_inven, book_menu = True, False, False, False

        if backpage and not book_map and not book_inven and not book_menu:
            book_anim -= 1
            if book_anim == 0:
                backpage, openbook, book_map = False, False, True

        win.blit(book_img[book_anim], (0, 0))

        if book_inven and book_anim == 19:
            if 'potion' not in item:
                win.blit(potion_s, (710, 212))
            if 'potion' in item:
                win.blit(potion_b, (710, 212))
            if 'magicpowder' not in item:
                win.blit(magicpowder_s, (800, 212))
            if 'magicpowder' in item:
                win.blit(magicpowder_b, (800, 212))
            if 'applescrap' not in item:
                win.blit(applescrap_s, (895, 205))
            if 'applescrap' in item:
                win.blit(applescrap_b, (895, 205))
            if 'puzzlepaper1' not in item:
                win.blit(puzzlepaper_s, (975, 215))
            if 'puzzlepaper1' in item:
                win.blit(puzzlepaper_b, (975, 215))
                if 978 <= mx <= 1048 and 224 <= my <= 290 and not seepaper:
                    what_paper = paper_rulepz.copy()
                    mx, my = -1, -1
                    seepaper = True
            if 'puzzlepaper2' not in item:
                win.blit(puzzlepaper_s, (690, 308))
            if 'puzzlepaper2' in item:
                win.blit(puzzlepaper_b, (690, 308))
                if 695 <= mx <= 763 and 307 <= my <= 394 and not seepaper:
                    what_paper = paper_blackcathate.copy()
                    mx, my = -1, -1
                    seepaper = True
            if 'puzzlepaper3' not in item:
                win.blit(puzzlepaper_s, (785, 308))
            if 'puzzlepaper3' in item:
                win.blit(puzzlepaper_b, (785, 308))
                if 790 <= mx <= 859 and 307 <= my <= 394 and not seepaper:
                    what_paper = paper_b1.copy()
                    mx, my = -1, -1
                    seepaper = True
            if 'puzzlepaper4' not in item:
                win.blit(puzzlepaper_s, (880, 308))
            if 'puzzlepaper4' in item:
                win.blit(puzzlepaper_b, (880, 308))
                if 884 <= mx <= 952 and 307 <= my <= 394 and not seepaper:
                    what_paper = paper_901502.copy()
                    mx, my = -1, -1
                    seepaper = True
            if 'puzzlepaper5' not in item:
                win.blit(puzzlepaper_s, (975, 308))
            if 'puzzlepaper5' in item:
                win.blit(puzzlepaper_b, (975, 308))
                if 979 <= mx <= 1045 and 307 <= my <= 394 and not seepaper:
                    what_paper = paper_bnwbklu.copy()
                    mx, my = -1, -1
                    seepaper = True
            if 0 <= mx <= 1280 and 0 <= my <= 720 and seepaper and ANIM_PAPER == 14:
                seepaper = False
                mx, my = -1, -1

    if safe >= 1 and ("puzzlepaper1" not in item):
        item.append("puzzlepaper1")
        alpha = 255
        what_paper = paper_rulepz.copy()

    if safe >= 1 and not prize_pz and 'magicpowder' not in item and not what_paper:
        play_pz = True
        if keys[pygame.K_f] and safe > 15:
            safe = -5
            play_pz = False

        win.blit(bar, (533, 455))

        # win.blit(colum[row1], (548, yrow))
        # win.blit(colum[row2], (618, yrow))
        # win.blit(colum[row3], (685, yrow))
        # win.blit(colum[row4], (748, yrow))

        if keys[pygame.K_d] and cd_pz > 10 and up_pz > 10 and down_pz > 10:
            rowza += 1
            cd_pz = -2
        if keys[pygame.K_a] and cd_pz > 10 and up_pz > 10 and down_pz > 10:
            rowza -= 1
            cd_pz = -2
        if rowza < 1:
            rowza = 4
        elif rowza > 4:
            rowza = 1

        if keys[pygame.K_w] and up_pz > 10 and cd_pz > 10:
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
        if keys[pygame.K_s] and down_pz > 10 and cd_pz > 10:
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
        print("row1", row1, "row2", row2, "row3", row3, "row4", row4)

        if keys[pygame.K_SPACE] and cd_pz > 10:
            if (row1 == 1 or row1 == 9 or row1 == 4 or row1 == 7) and \
                (row2 == 9 or row2 == 1 or row2 == 4 or row2 == 7) and \
                (row3 == 4 or row3 == 9 or row3 == 1 or row3 == 7) and \
                (row4 == 7 or row4 == 4 or row4 == 9 or row4 == 1) and not prize_pz:
                prize_pz = True
                item.append("magicpowder")
                alpha = 255
                safe = 0
            else:
                w_sound.play()
                row1 = 0
                row2 = 0
                row3 = 0
                row4 = 0
                row[1] = 0
                row[2] = 0
                row[3] = 0
                row[4] = 0

    if what_paper:
        redrawpaper(what_paper)

    if PLAY_FRONT:
        frontgame()
    pygame.display.update()
    
    print(X, Y)
    # print(item)
    # print(ANIM_PAPER)
    # print(seepaper)
    # print(idmap)

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouseon += 1
    else:
        mouseon = 0
    if mouseon == 1:
        mx, my = pygame.mouse.get_pos()

pygame.quit()
