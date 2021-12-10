import pygame, json
pygame.init()

#---------------------------------------------------------------------------
"""set variable"""
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("W <it> CH AcademY")
bg = pygame.image.load("sprite/secretforest.jpg")
fog = pygame.image.load("sprite/fog.png")
bg_width, bg_height = bg.get_rect().size
#icon = pygame.image.load("sprite/icongame.png")
#pygame.display.set_icon(icon)

PLAYER_RADIUS = 13
PLAYER_POSITION_X = PLAYER_RADIUS-10
PLAYER_POSITION_Y = 25

start_scrolling_x = (width/2)
stage_wildth = 1280
stage_position_x = 0

start_scrolling_y = height/2
stage_height = 720
stage_position_y = 0

X, Y, vel, WALKCOUNT, CHECK = 598, 613, 15, 0, 'UP'
COUNTYEL, YELLOW_POS_X, YELLOW_POS_Y = 0, 242, 242
MAGIC_POSITION_X, MAGIC_POSITION_Y = 0, 0
hp_player, fight, MAGICCOUNT = 50, False, 0
hp_yellow = 65
yellowdead = False

run = True
LEFT, RIGHT = False, False
DOWN, UP, CIRCLE = False, False, False
gosecretfor, gameover = True, False

walls = open("walls.txt", 'r').read()
walls = dict(json.loads(walls))

#music = pygame.mixer.Sound("testbg.mp3")
magicsound = pygame.mixer.Sound("sprite/magic/magicsound.mp3")
#---------------------------------------------------------------------------
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

walkr, walkl = readvar('var.txt', 'walkr'), readvar('var.txt', 'walkl')
walkd, walku = readvar('var.txt', 'walkd'), readvar('var.txt', 'walku')
rspell, lspell = readvar('var.txt', 'rspell'), readvar('var.txt', 'lspell')
dspell, uspell = readvar('var.txt', 'dspell'), readvar('var.txt', 'uspell')
magic, deadplayer = readvar('var.txt', 'circle'), readvar('var.txt', 'dead')
yellow, deadyellow = readvar('monvar.txt', '/yellow'), readvar('monvar.txt', 'deadyellow')

damagewalkr = pygame.image.load("sprite/damage taken/walkr1.png")
damagewalkl = pygame.image.load("sprite/damage taken/walkl1.png")
damagewalkd = pygame.image.load("sprite/damage taken/walkd1.png")
damagewalku = pygame.image.load("sprite/damage taken/walku1.png")

for i in range(9):
    walkr[i] = pygame.transform.scale(walkr[i], (int(width*0.07), int(height*0.13)))
    walkl[i] = pygame.transform.scale(walkl[i], (int(width*0.07), int(height*0.13)))
    walkd[i] = pygame.transform.scale(walkd[i], (int(width*0.07), int(height*0.13)))
    walku[i] = pygame.transform.scale(walku[i], (int(width*0.07), int(height*0.13)))
    damagewalkr = pygame.transform.scale(damagewalkr, (int(width*0.07), int(height*0.13)))
    damagewalkl = pygame.transform.scale(damagewalkl, (int(width*0.07), int(height*0.13)))
    damagewalkd = pygame.transform.scale(damagewalkd, (int(width*0.07), int(height*0.13)))
    damagewalku = pygame.transform.scale(damagewalku, (int(width*0.07), int(height*0.13)))
    rspell[i] = pygame.transform.scale(rspell[i], (int(width*0.07), int(height*0.13)))
    lspell[i] = pygame.transform.scale(lspell[i], (int(width*0.07), int(height*0.13)))

#---------------------------------------------------------------------------
def fadescreen():
    """blit fade screen"""
    fade = pygame.Surface((1280, 720))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        if gameover:
            redrawDead()
        elif gameover == False:
            redrawGameWindow()
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
#---------------------------------------------------------------------------
def redrawMagic(wall=[(0,0,0,0)]):
    """blit magic"""
    global MAGICCOUNT
    global WALKCOUNT
    global CIRCLE
    global MAGIC_POSITION_X
    global MAGIC_POSITION_Y

    if MAGICCOUNT + 1 >= 17:
        MAGICCOUNT, WALKCOUNT = 0, 0
        MAGIC_POSITION_X , MAGIC_POSITION_Y = 0, 0
        CIRCLE = False
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
                l -= 113
            if CHECK == "RIGHT":
                j -= 60
            if i < MAGIC_POSITION_X < j and k < MAGIC_POSITION_Y < l:
                showmagic = False
                break
            else:
                showmagic = True
        print(MAGIC_POSITION_X, MAGIC_POSITION_Y)
        print(i,j,k,l)
        if showmagic:
            win.blit(magic[MAGICCOUNT], (MAGIC_POSITION_X, MAGIC_POSITION_Y))
    MAGICCOUNT += 1
#---------------------------------------------------------------------------
def redrawDead():
    """blit the main character dead"""
    global WALKCOUNT
    if WALKCOUNT >= 9:
        win.blit(deadplayer[8], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
    else:
        win.blit(deadplayer[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
    WALKCOUNT += 1
#---------------------------------------------------------------------------
def redrawGameWindow():
    """blit the main character"""
    global WALKCOUNT
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    global YELLOW_POS_X
    global YELLOW_POS_Y

    if WALKCOUNT + 1 >= 9 and gameover != True and CIRCLE != True: #กัน out of range
        WALKCOUNT = 0

    if RIGHT and CIRCLE == False:
        win.blit(walkr[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALKCOUNT += 1

    elif LEFT and CIRCLE == False:
        win.blit(walkl[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALKCOUNT += 1

    elif DOWN and CIRCLE == False:
        win.blit(walkd[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALKCOUNT += 1

    elif UP and CIRCLE == False:
        win.blit(walku[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALKCOUNT += 1

    elif CIRCLE:
        if WALKCOUNT >= 9:
            WALKCOUNT = 8
        if CHECK == 'RIGHT':
            win.blit(rspell[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'LEFT':
            win.blit(lspell[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'DOWN':
            win.blit(dspell[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'UP':
            win.blit(uspell[WALKCOUNT], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        WALKCOUNT += 1

    elif RIGHT == False and LEFT == False and DOWN == False and UP == False:
        if CHECK == 'RIGHT':
            win.blit(walkr[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'LEFT':
            win.blit(walkl[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'DOWN':
            win.blit(walkd[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'UP':
            win.blit(walku[0], (PLAYER_POSITION_X, PLAYER_POSITION_Y))

    if -15 <= YELLOW_POS_Y-PLAYER_POSITION_Y <= 60 and yellowdead == False and\
       abs(YELLOW_POS_X-PLAYER_POSITION_X) <= 19 and fight == True and CIRCLE == False:
        if CHECK == 'RIGHT':
            win.blit(damagewalkr, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'LEFT':
            win.blit(damagewalkl, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'DOWN':
            win.blit(damagewalkd, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
        elif CHECK == 'UP':
            win.blit(damagewalku, (PLAYER_POSITION_X, PLAYER_POSITION_Y))
#---------------------------------------------------------------------------
def redrawMonster():
    """blit monster"""
    global COUNTYEL
    global YELLOW_POS_X
    global YELLOW_POS_Y
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    
    if yellowdead == False:
        if COUNTYEL + 1 >= 9: #กัน out of range
            COUNTYEL = 0
        if YELLOW_POS_X >= PLAYER_POSITION_X+15:
            YELLOW_POS_X -= 5
        if YELLOW_POS_X <= PLAYER_POSITION_X+15:
            YELLOW_POS_X += 5
        if YELLOW_POS_Y >= PLAYER_POSITION_Y+25:
            YELLOW_POS_Y -= 5
        if YELLOW_POS_Y <= PLAYER_POSITION_Y+50:
            YELLOW_POS_Y += 5
        win.blit(yellow[COUNTYEL], (YELLOW_POS_X, YELLOW_POS_Y))
    elif yellowdead:
        if COUNTYEL <= 8:
            pygame.time.delay(10)
            win.blit(deadyellow[COUNTYEL], (YELLOW_POS_X, YELLOW_POS_Y))
        else:
            YELLOW_POS_X, YELLOW_POS_Y = 242, 242
    COUNTYEL += 1
#---------------------------------------------------------------------------
def scrolling():
    """scrolling background"""
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
def secretfor(wall=[(0,0,0,0)]):
    """secret forest map"""
    global X
    global Y
    global CHECK
    global RIGHT
    global LEFT
    global DOWN
    global UP
    global CIRCLE
    global WALKCOUNT
    global PLAYER_RADIUS
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y

    if keys[pygame.K_SPACE] and gameover == False and fight == True and CIRCLE == False:
        CIRCLE = True
        pygame.mixer.Sound.play(magicsound)
        WALKCOUNT = 0
    elif keys[pygame.K_a] and X > vel and gameover == False and CIRCLE == False:
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
    elif keys[pygame.K_d] and gameover == False and CIRCLE == False:
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
    elif keys[pygame.K_s] and gameover == False and CIRCLE == False:
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
    elif keys[pygame.K_w] and gameover == False and CIRCLE == False:
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
#---------------------------------------------------------------------------
"""mainloop"""
while run:
    pygame.time.delay(25)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False
#------------------------------------
    if gosecretfor == True:
        secretfor(walls["secretfor"])
        rel_x = -X % bg_width
        rel_y = -Y % bg_height

        if Y <= 253:
            fight = True
        if Y >= 662:
            win.blit(bg ,(-238, -662))
        else:
            win.blit(bg ,(-238, rel_y-bg_height))
#---------------------------------------------------------------------------

#     print(X, Y)
#     print('PLAYER', PLAYER_POSITION_X, PLAYER_POSITION_Y)
#     print('MONSTER', YELLOW_POS_X, YELLOW_POS_Y)

    if fight and gameover == False:
        if CIRCLE:
            redrawMagic(walls["secretfor"])
        if YELLOW_POS_Y-PLAYER_POSITION_Y <= 30:
            redrawMonster()
            redrawGameWindow()
        else:
            redrawGameWindow()
            redrawMonster()
        pygame.draw.rect(win, (250-(hp_player*5), hp_player*5, 0), [390, 40, hp_player*10, 15])
        
    elif gameover:
        redrawDead()
        if WALKCOUNT == 15:
            fadescreen()
            gameover = False
    else:
        redrawGameWindow()

#---------------------------------------------------------------------------

    if gosecretfor:
        win.blit(fog ,(-238, rel_y-bg_height))

    if -15 <= YELLOW_POS_Y-PLAYER_POSITION_Y <= 60 and yellowdead == False and \
       abs(YELLOW_POS_X-PLAYER_POSITION_X) <= 19 and fight == True: #ฝั่งลบ มอนสูงกว่าคน
        if hp_player <= 0:
            hp_player, WALKCOUNT = 50, 0
            YELLOW_POS_X, YELLOW_POS_Y = 242, 242
            fight = False
            gameover = True
            CIRCLE = False
        else:
            hp_player -= 0.5

    if abs((MAGIC_POSITION_X+50)-YELLOW_POS_X) <= 50 and \
       abs(MAGIC_POSITION_Y-YELLOW_POS_Y) <= 100 and yellowdead == False:
        hp_yellow -= 2
        if hp_yellow < 0:
            COUNTYEL = 0
            yellowdead = True

    pygame.display.update()

pygame.quit()
