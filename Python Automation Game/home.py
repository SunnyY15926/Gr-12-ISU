import pygame
import random
import math

from player import Player
from button import Button
from loader import Loader
from page import Page
#from map import Map
from textbox import Textbox
from resource import Resource

pygame.init()
expand = 32  # 32
size = [30, 22]  # aspect ratio
screen = pygame.display.set_mode((size[0]*expand, size[1]*expand))
pygame.display.set_caption("Home")
font = pygame.font.Font('freesansbold.ttf', 11)
# print(pygame.font.get_fonts())
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (150, 150, 150)
black = (0,0,0)

p1 = Player(40, 40)
#character = pygame.image.load("download.png")
#character = pygame.transform.scale(character, (40, 40))

mouseCoords = [0,0,0,0]


def draw(): #runs once and initializes game variables
    run = True
    fps = 60
    pageNum = 0
    tab = 0
    subtab = 0
    clock = pygame.time.Clock()
    drawCoords = [0, 0, 0, 0]

    dialogue = [Textbox(55, 350, 855, 235)]
    resources = Resource()

    largeFont = pygame.font.Font('freesansbold.ttf', 20)
    mainPage = [
        Button(60, 290, 160, 60,"Play",1,largeFont),
        Button(60, 360, 160, 60,"Exit",-1,largeFont),
        Button(60, 430, 160, 60,"Load Save",2,largeFont), #change from 2 to another page index
        Button(60, 500, 160, 60,"Reset Save",3,largeFont) #change from 3 to another page index
    ]
    tabButtons = [
        
        Button(200, 25, 130, 30,"Build",1),
        Button(350, 25, 130, 30,"Settlement",2),
        Button(500, 25, 130, 30,"Storage",3),
        Button(650, 25, 130, 30,"Forest",4)
    ]
    buildButtons = [
        Button(200, 70, 130, 30,"Campfire",1),
        Button(200, 110, 130, 30,"Workshop",1),
        Button(200, 150, 130, 30,"Fireplace",1),
        Button(200, 190, 130, 30,"Drying Rack",1),
        Button(200, 230, 130, 30,"Silo", 1)
        ]  
    settlementButtons = [
        Button(200, 70, 130, 30,"Workers",2),
        Button(200, 110, 130, 30,"Military",2),
        Button(200, 150, 130, 30,"Housing",2)
    ]
    storageButtons = [
        Button(200, 70, 130, 30,"Inventory",3),
        Button(200, 110, 130, 30,"Silo Storage",3)
    ]
    # [4 position], text, page, resourceType, reward, timer,resource, isUnlocked)
    forestLoaders = [
        Loader(200, 70, 130, 30, "Forage", 4, 'food', 2, 60, resources,True),
        Loader(200, 110, 130, 30,"Gather", 4, 'wood', 1, 120, resources,True),
        Loader(200, 150, 130, 30,"Cut Trees", 4, 'wood',5,240, resources,True)
    ]

    pages = [
        Page(mainPage),
        Page(buildButtons + tabButtons, dialogue),
        Page(settlementButtons + tabButtons, dialogue),
        Page(storageButtons + tabButtons, dialogue, [], [resources]),
        Page(tabButtons, dialogue, forestLoaders),
        Page([]) #adventure screen, add features to this page later
        ]

    def redraw(screen): #loops and redraws screen 
        screen.fill(white)
        if pageNum == -1:
            pygame.quit()
            run = False
        else:
            pages[pageNum].draw(screen)
            pages[pageNum].tick()

        #update using page OOP
        '''
        if tab == 2:  # map screen
            screen.blit(character, (p1.getX(), p1.getY()))
        '''

        pygame.draw.rect(screen, red, (drawCoords)) #scaffolding tool for drawing rectangles when designing UI
        pygame.display.update()
        
    #redraw(screen)

    while run:
        clock.tick(fps) 
        redraw(screen) #updates the UI

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # dictionary of all keys:boolean for whether its pressed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False
            if keys[pygame.K_w]:
                p1.move(0, -p1.getSpeed())
            if keys[pygame.K_s]:
                p1.move(0, p1.getSpeed())
            if keys[pygame.K_a]:
                p1.move(-p1.getSpeed(), 0)
            if keys[pygame.K_d]:
                p1.move(p1.getSpeed(), 0)

            #mouse events
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            if event.type == pygame.MOUSEBUTTONDOWN: #detects mouse click
                mouseCoords[0:2] = [mouseX, mouseY]
                if pages[pageNum].mouseClick(mouseX,mouseY): #checks for valid button press
                    pageNum = pages[pageNum].mouseClick(mouseX,mouseY)

            if pygame.mouse.get_pressed()[0]: # detects left click
                mouseCoords[2:4] = [mouseX,mouseY]
                drawCoords = rectTool(mouseCoords)

            if event.type == pygame.MOUSEBUTTONUP:
                pages[pageNum].offClick()
                
                print("pygame.draw.rect(screen,grey,%s)" % drawCoords) #scaffold ui code
            
def rectTool(pos):
    '''
    turns 4 cartesian coordinates into a rectangle parameters rounded to the nearest 5
    '''
    if not pos:
        pass
    if pos[0]>pos[2]:
        pos[2],pos[0] = pos[0],pos[2]
    if pos[1]>pos[3]:
        pos[3],pos[1] = pos[1],pos[3]
    x1 = round(pos[0] // 5) * 5
    y1 = round(pos[1] // 5) * 5
    x2 = round((pos[2] - x1)// 5) * 5 
    y2 = round((pos[3] - y1)// 5) * 5 
    return [x1, y1, x2, y2]

draw()
