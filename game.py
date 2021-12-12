import pygame
pygame.init()

#---------------------------------------------------------------------------
"""set variable"""
walkcount = 0
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("W <it> CH AcademY")
bg = pygame.image.load("sprite/hallway.jpg")
font = pygame.font.Font('sprite/Tangerine-Bold.ttf', 72)
txtp1 = '901502'
run = True
ANIM = 0

def readvar(file, string):
    """readline variable"""
    f, mylist = open(file, 'r'), []
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

scrollpaper = readvar('var.txt', 'scrollpaper')

def redrawpaper():
    """blit dialog"""
    global ANIM
    if ANIM+1 >= 15:
        ANIM = 14
    win.blit(scrollpaper[ANIM], ((1280/2)-(scrollpaper[ANIM].get_rect().size[0]/2), 0))
    ANIM += 1

while run:
    pygame.time.delay(25)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False

    win.blit(bg, (0, 0))
    redrawpaper()
    pygame.display.update()

pygame.quit()
