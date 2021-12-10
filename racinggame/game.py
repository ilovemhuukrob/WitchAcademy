import pygame
pygame.init()

wildth, height = 1280, 720
win = pygame.display.set_mode((wildth, height))

pygame.display.set_caption("ขี่ไม้กวาด")

bg = pygame.image.load("sprite/racing/bg/mountain.png").convert()
bg2 = pygame.image.load("sprite/racing/bg/forest1.jpg").convert()
bg3 = pygame.image.load("sprite/racing/bg/library.jpg").convert()
bg4 = pygame.image.load("sprite/racing/bg/forest1.jpg").convert()
bg_wildth, bg_height = bg.get_rect().size

start_scrolling = wildth/2
stage_wildth = 1280*2
stage_position_x = 0

circle_radius = 25
circle_posistion_x = circle_radius

bg_scrolling = 0

FONT = pygame.font.SysFont("Sans", 20)

def redrawGameWindow():
    global walkcount
    
    if walkcount + 1 >= 44: #กัน out of range
        walkcount = 0

    if right:
        win.blit(walkright[walkcount], (x, y))
        walkcount += 1
    # elif left:
    #     win.blit(walkright[walkcount], (x, y))
    #     walkcount += 1
        
    else:
        win.blit(nowalk[walkcount], (x, y))
        walkcount += 1
    pygame.display.update()
    
def fadescreen():
    """blit fade screen"""
    fade = pygame.Surface((1280, 720))
    fade.fill((0,0,0))
    for alpha in range(0, 75):
        fade.set_alpha(alpha)
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

# crash = 0
# moncount = 0
# def spawn(monster, posx, posy):
#     global moncount
#     global crash
#     global x
#     global y
#     global heart

#     if moncount + 1 >= len(monster):
#         moncount = 0
#     wmon, hmon = monster[moncount].get_rect().size
#     print(wmon, hmon)
#     if posy-180 < y < posy-10 and posx-100 < x < posx-50:
#         crash += 1/3
#     if crash >= 1:
#         heart -= 1
#         crash = 0

#     win.blit(monster[moncount], (posx, posy))
#     moncount += 1


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

class mon:
    def __init__(self, posx, posy, monster):
        self.posx = posx
        self.posy = posy
        self.monster = monster
        self.moncount = 0
        self.crash = 0
        self.pas = False

    def spawn(self, sec, speedx, speedy, bounce=False):
        global x
        global y
        global heart
        global cooldown
        global hplay
        global wplay


        if time >= sec:

            if self.moncount + 1 >= len(self.monster):
                self.moncount = 0
            wmon, hmon = self.monster[self.moncount].get_rect().size
            # print(wmon, hmon)
            if y < self.posy < y+hplay-80 and x < self.posx < x+wplay-80 and cooldown > 2:
                heart -= 1
                cooldown = 0
            # if self.posy-180 < y < self.posy-10 and self.posx-100 < x < self.posx-50 and cooldown > 2:
            #     heart -= 1
            #     cooldown = 0

            win.blit(self.monster[self.moncount], (self.posx, self.posy))
            self.moncount += 1

            if bounce:
                if self.posy < 0:
                    self.pas = True
                elif self.posy > 620:
                    self.pas = False
                if self.pas:
                    speedy *= -1

            self.posx -= speedx
            self.posy += speedy


walkright, nowalk = readvar('front.txt', 'racing/broom'), readvar('front.txt', 'racing/broom')


heartimg = pygame.image.load('sprite/racing/broom/heart.png')

bbubl, rbubl = readvar('stage 1.txt', 'clocktower/bbubl'), readvar('stage 1.txt', 'clocktower/rbubl')
clock = readvar('stage 1.txt', 'clocktower/clock')
poisonbot, ghost = readvar('stage 1.txt', 'clocktower/poison'), readvar('stage 1.txt', 'clocktower/ghost')

onefairy, twofairy = readvar('stage 2.txt', 'onefairy'), readvar('stage 2.txt', 'twofairy')
broom, pump = readvar('stage 2.txt', 'broom'), readvar('stage 2.txt', 'pump')
spider, bat, bird = readvar('stage 2.txt', 'spider'), readvar('stage 2.txt', 'bat'), readvar('stage 2.txt', 'bird')

bluebook, purbook, redbook = readvar('stage 3.txt', 'bluebook'), readvar('stage 3.txt', 'purbook'), readvar('stage 3.txt', 'redbook')

#----------------------------------------------------------- stage 1 หอนาฬิกา ----------------------------------------------------------------
rbubl1 = mon(1280, 160, rbubl); rbubl2 = mon(1280, 560, rbubl); rbubl3 = mon(1280, 160, rbubl)
rbubl4 = mon(1280, 160, rbubl); rbubl5 = mon(1280, 220, rbubl); rbubl6 = mon(1280, 220, rbubl); rbubl7 = mon(1280, 220, rbubl)
bbubl1 = mon(1280, 525, bbubl); bbubl2 = mon(1280, 525, bbubl); bbubl3 = mon(1280, 525, bbubl)
bbubl4 = mon(1280, 350, bbubl); bbubl5 = mon(1280, 350, bbubl); bbubl6 = mon(1280, 350, bbubl)
bbubl7 = mon(1280, 450, bbubl); bbubl8 = mon(1280, 450, bbubl); bbubl9 = mon(1280, 450, bbubl)
ghost1 = mon(1280, 500, ghost); ghost2 = mon(1280, 500, ghost); ghost3 = mon(1280, 150, ghost); ghost4 = mon(1280, 150, ghost)
poisonbot1 = mon(1280, 280, poisonbot); bird10 = mon(1280, 360, bird)
clock1 = mon(1280, 360, clock); clock2 = mon(1280, 360, clock); clock3 = mon(1280, 360, clock)

bird1 = mon(1280, 140, bird); bird2 = mon(1280, 140, bird); bird3 = mon(1280, 140, bird)
bird4 = mon(1280, 190, bird); bird5 = mon(1280, 190, bird); bird6 = mon(1280, 190, bird)
bird7 = mon(1280, 240, bird); bird8 = mon(1280, 240, bird); bird9 = mon(1280, 240, bird)
spider1 = mon(670, 0, spider); spider2 = mon(670, 0, spider)
pump1 = mon(500, 0, pump); pump2 = mon(500, 0, pump); pump3 = mon(500, 0, pump); pump4 = mon(500, 0, pump)
bat1 = mon(1280, 150, bat); bat2 = mon(1280, 200, bat); bat3 = mon(1280, 250, bat)
onefairy1 = mon(1280, 340, onefairy); onefairy2 = mon(1280, 480, onefairy); onefairy3 = mon(1280, 480, onefairy)
twofairy1 = mon(1280, 400, twofairy); twofairy2 = mon(1280, 400, twofairy); twofairy3 = mon(1280, 600, twofairy); twofairy4 = mon(1280, 600, twofairy)
broom1 = mon(1280, 500, broom); broom2 = mon(1280, 500, broom)
broom3 = mon(1280, 530, broom); broom4 = mon(1280, 530, broom); broom5 = mon(1280, 530, broom)

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

# -------------------------------------------------------------------------------------------------------------------------------


#-----------------music-------------------------------
# music = pygame.mixer.Sound("testbg.mp3")
# crash = pygame.mixer.Sound("Crash1_.mp3")
#-----------------------------------------------------------------
x = 50
y = 355
vel = 30
left = False
right = False
walkcount = 0
check = ''
time = 0
heart = 5
cooldown = 0

hplay, wplay = walkright[walkcount].get_rect().size

fadebg2 = False
fadebg3 = False
fadebg4 = False

# pygame.mixer.Sound.play(music)
run = True
while run:
    pygame.time.delay(30)
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif keys[pygame.K_ESCAPE]:
            run = False

    bg_scrolling -= 1
    
    if time >= 180:
        if fadebg4 == False:
            fadescreen()
            fadebg4 = True
        win.blit(bg4, (bg_scrolling, 0))
        win.blit(bg4, (bg_scrolling+1280, 0))

    elif time >= 120:
        if fadebg3 == False:
            fadescreen()
            fadebg3 = True
        win.blit(bg3, (bg_scrolling, 0))
        win.blit(bg3, (bg_scrolling+1280, 0))
    
    elif time >= 60:
        if fadebg2 == False:
            fadescreen()
            fadebg2 = True
        win.blit(bg2, (bg_scrolling, 0))
        win.blit(bg2, (bg_scrolling+1280, 0))

    elif time >= 0:
        win.blit(bg, (bg_scrolling, 0))
        win.blit(bg, (bg_scrolling+1280, 0))
    if bg_scrolling <= -1280:
        bg_scrolling = 0
    time += 0.05
    # y += 5

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x > 10:
        x -= vel
        left = True
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < bg_wildth-150:
        x += vel
        right = True
    elif (keys[pygame.K_w] or keys[pygame.K_UP]) and y > 5:
        y -= vel
        right = True
    elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and y < bg_height-250:
        y += vel
        right = True
    else:
        right = False

#---------------------------------------------------- stage1 หอนาฬิกา [1 - 60] -------------------------------------------------------------------------
    bird10.spawn(3, 20, 0)

    rbubl1.spawn(5, 7, 0); rbubl2.spawn(18, 7, 0); rbubl3.spawn(31, 7, 0)
    rbubl4.spawn(17, 7, 0); rbubl5.spawn(42, 7, 0); rbubl6.spawn(53, 7, 0); rbubl7.spawn(56, 7, 0)
    bbubl1.spawn(10, 7, 0); bbubl2.spawn(31, 7, 0); bbubl3.spawn(48, 7, 0)
    bbubl4.spawn(25, 7, 0); bbubl5.spawn(33, 7, 0); bbubl6.spawn(46, 7, 0)
    bbubl7.spawn(10, 7, 0); bbubl8.spawn(10, 7, 0); bbubl9.spawn(10, 7, 0)
    ghost1.spawn(20, 30, 0); ghost2.spawn(13, 25, 0); ghost3.spawn(22, 25, 0); ghost4.spawn(35, 25, 0)
    poisonbot1.spawn(55, 12, -12, bounce=True)
    clock1.spawn(16, 20, 0); clock2.spawn(39, 20, 0); clock3.spawn(52, 20, 0)

#------------------------------------------------------- stage 2 ป่า [61 - 120] ------------------------------------------------
    bird1.spawn(68, 7, 0); bird2.spawn(84, 7, 0); bird3.spawn(104, 7, 0)
    bird4.spawn(68, 7, 0); bird5.spawn(84, 7, 0); bird6.spawn(104, 7, 0)
    bird7.spawn(71, 7, 0); bird8.spawn(105, 7, 0); bird9.spawn(111, 7, 0)
    spider1.spawn(74, 0, 7); spider2.spawn(89, 0, 7)
    pump1.spawn(82, 0, 7); pump2.spawn(89, 0, 7); pump3.spawn(96, 0, 7); pump4.spawn(107, 0, 7)
    bat1.spawn(80, 20, 0); bat2.spawn(96, 20, 0); bat3.spawn(83, 25, 0)
    onefairy1.spawn(98, 7, 0); onefairy2.spawn(75, 7, 0); onefairy3.spawn(94, 7, 0)
    twofairy1.spawn(80, 7, 0); twofairy2.spawn(107, 7, 0); twofairy3.spawn(69, 7, 0); twofairy4.spawn(88, 7, 0)
    broom1.spawn(94, 20, 0); broom2.spawn(105, 20, 0)
    broom3.spawn(70, 20, 0); broom4.spawn(90, 20, 0); broom5.spawn(110, 20, 0)
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

    cooldown += 0.05

    if heart == 5:
        win.blit(heartimg, (920, 25))
        win.blit(heartimg, (985, 25))
        win.blit(heartimg, (1050, 25))
        win.blit(heartimg, (1115, 25))
        win.blit(heartimg, (1180, 25))        
    if heart == 4:
        win.blit(heartimg, (985, 25))
        win.blit(heartimg, (1050, 25))
        win.blit(heartimg, (1115, 25))
        win.blit(heartimg, (1180, 25))
    if heart == 3:
        win.blit(heartimg, (1050, 25))
        win.blit(heartimg, (1115, 25))
        win.blit(heartimg, (1180, 25))
    if heart == 2:
        win.blit(heartimg, (1115, 25))
        win.blit(heartimg, (1180, 25))
    if heart == 1:
        win.blit(heartimg, (1180, 25)) 
    if heart == 0:
        heart = 5
    win.blit(FONT.render("Score : "+str(int(time)), True, (255,255,255)), (20,20))
    # win.blit(FONT.render("Heart : "+ "<3"*(int(heart)), True, (255,255,255)), (900,20))
    redrawGameWindow()

pygame.quit()
