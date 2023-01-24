from cmu_112_graphics import *
from tkinter import * 
import random
from PIL import ImageTk

def appStarted(app):
    #background variables#
    app.hsbgImg = app.loadImage('homescreenbg.png')
    app.grassImg = app.loadImage('grass.png')
    app.wood1Img = app.loadImage('wood1.png')
    app.wood2Img = app.loadImage('wood2.png')

    #interface variables#
    app.width = 1280
    app.height = 720
    app.homeScreen = True
    app.x = app.width/2
    app.y = app.height/2
    app.playScreen = False
    app.helpScreen = False
    app.goBack = False
 
    #trail variables#
    app.borderWidth = app.height/72
    app.boxX = app.width/25
    app.boxY = app.height*4/75
    app.trailList = []
    app.moving = []
    app.noTrail = True
    app.moveDiff = 10
    app.timer = 0
    app.delay = 10

    #interface variables#
    app.quitScreen = False
    app.health = 30
    app.startHealth = 30
    app.startSun = 2000
    app.sun = 2000
    app.plant = ['sunflower', 'peashooter', 'cabbagepult', 'spikeweed', \
        'puffshroom']
    app.buyFill = ['', '', '', '', '']
    app.buy = [False, False, False, False, False]
    app.speedFill = '#90EE90'
    app.pauseFill = '#add8e6'
    app.speed = False
    app.pause = False
    app.speeded = 20

    #plant variables#
    #SUNFLOWERS#
    app.sfIntImg = app.loadImage('sunflower.png')
    app.sfImg = app.loadImage('sunflower1.png')
    app.sunFlower = [['Sunflower', 0, 1000, 0, 250, 2, None, None], \
        ['Twin Sunflower', 0, 2000, 0, 500, 5, None, None], \
        ['Primal Sunflower', 0, 4000, 0, 1000, 10, None, None]]
    #PEASHOOTERS
    app.psIntImg = app.loadImage('peashooter.png')
    app.psImg = app.loadImage('peashooter1.png')
    app.peaShooter = [['Peashooter', 5, 600, 8, 150, 0, 1, 0],\
        ['Repeater', 10, 1500, 10, 375, 0, 2, 0],\
        ['Threepeater', 15, 2500, 12, 625, 2, 3, 0]]
    #CABBAGE#
    app.cbIntImg = app.loadImage('cabbagepult.png')
    app.cbImg = app.loadImage('cabbagepult1.png')
    app.cabbagePult = [['Cabbage-Pult', 5, 800, 10, 200, 0, 1, 0], \
        ['Melon-Pult', 8, 2500, 15, 625, 0, 1, 3], \
        ['Winter-Melon', 10, 5000, 15, 1250, 0, 1, 3]]
    #SPIKEWEED#
    app.swIntImg = app.loadImage('spikeweed.png')
    app.swImg = app.loadImage('spikeweed1.png')
    app.spikeWeed = [['Spikeweed', 1, 500, 1, 125, 0, 0, 1], \
        ['Spikerock', 2, 1000, 1, 250, 0, 0, 1], \
        ['Iceweed', 3, 1500, 1, 375, 0, 0, 1]]
    #PUFFSHROOM#
    app.pusIntImg = app.loadImage('puffshroom.png')
    app.pusImg = app.loadImage('puffshroom1.png')
    app.puffShroom = [['Puff-Shroom', 2, 100, 5, 25, 0, 10, 0], \
        ['Fume-Shroom', 2, 300, 10, 75, 0, 10, 10], \
        ['Spore-Shroom', 3, 600, 10, 150, 0, 10, 10]]

    #Upgraded Unit Pictures#
    app.twIntImg = app.loadImage('twinsunflower.png')
    app.twImg = app.loadImage('twinsunflower1.png')
    app.prIntImg = app.loadImage('primalsunflower.png')
    app.prImg = app.loadImage('primalsunflower1.png')
    app.reIntImg = app.loadImage('repeater.png')
    app.reImg = app.loadImage('repeater1.png')
    app.thIntImg = app.loadImage('threepeater.png')
    app.thImg = app.loadImage('threepeater1.png')
    app.mpIntImg = app.loadImage('melonpult.png')
    app.mpImg = app.loadImage('melonpult1.png')
    app.wmIntImg = app.loadImage('wintermelon.png')
    app.wmImg = app.loadImage('wintermelon1.png')
    app.srIntImg = app.loadImage('spikerock.png')
    app.srImg = app.loadImage('spikerock1.png')
    app.iwIntImg = app.loadImage('iceweed.png')
    app.iwImg = app.loadImage('iceweed1.png')
    app.fsIntImg = app.loadImage('fumeshroom.png')
    app.fsImg = app.loadImage('fumeshroom1.png')
    app.ssIntImg = app.loadImage('sporeshroom.png')
    app.ssImg = app.loadImage('sporeshroom1.png')

    #plant gameplay variables
    app.plantList = []
    app.plantClickList = []
    app.drawDict = {'sunflower': app.sfImg, \
         'twinsunflower': app.twImg,\
             'primalsunflower': app.prImg, 'peashooter': app.psImg,\
        'repeater': app.reImg, 'threepeater': app.thImg, \
            'cabbagepult': app.cbImg,\
             'melonpult': app.mpImg,\
        'wintermelon': app.wmImg, 'spikeweed': app.swImg, \
            'spikerock': app.srImg,\
             'iceweed': app.iwImg,\
        'puffshroom': app.pusImg,'fumeshroom': app.fsImg, \
            'sporeshroom': app.ssImg}
    app.plantStatDict = {'sunflower': ['Sunflower', 0, 1000, 0, 250, 2, None, \
        None, 'Upgrade to Twin Sunflower?', app.twIntImg],\
        'twinsunflower': ['Twin Sunflower', 0, 2000, 0, 500, 5, None, \
            None, 'Upgrade to Primal Sunflower?', app.prIntImg],\
        'primalsunflower': ['Primal Sunflower', 0, 4000, 0, 1000, 10, None, \
            None, 'Max Level', app.prIntImg],\
        'peashooter': ['Peashooter', 5, 600, 8, 150, 0, 1, \
            False, 'Upgrade to Repeater?', app.reIntImg],\
        'repeater': ['Repeater', 10, 1500, 10, 375, 0, 1, \
            False, 'Upgrade to Threepeater?', app.thIntImg],\
        'threepeater': ['Threepeater', 15, 2500, 12, 625, 2, 1, \
            False, 'Max Level', app.thIntImg],\
        'cabbagepult': ['Cabbage-Pult', 5, 800, 10, 200, 0, 1, \
            False, 'Upgrade to Melon-Pult?', app.mpIntImg],\
        'melonpult': ['Melon-Pult', 8, 2500, 15, 625, 0, 1, \
            True, 'Upgrade to Winter-Melon?', app.wmIntImg],\
        'wintermelon': ['Winter-Melon', 10, 5000, 15, 1250, 0, 1, \
            True, 'Max Level', app.wmIntImg],\
        'spikeweed': ['Spikeweed', 1, 500, 1, 125, 0, 0, \
            True, 'Upgrade to Spikerock?', app.srIntImg], \
        'spikerock': ['Spikerock', 2, 1000, 1, 250, 0, 0, \
            True, 'Upgrade to Iceweed?', app.iwIntImg],\
        'iceweed': ['Iceweed', 3, 1500, 1, 375, 0, 0, \
            True, 'Max Level', app.iwIntImg],\
        'puffshroom':['Puff-Shroom', 2, 100, 5, 25, 0, 1, \
            False, 'Upgrade to Puff-shroom?', app.fsIntImg],\
        'fumeshroom':['Fume-Shroom', 2, 300, 10, 75, 0, 1, \
            True, 'Upgrade to Spore-Shroom?', app.ssIntImg],\
        'sporeshroom':['Spore-Shroom', 3, 600, 10, 150, 0, 1, \
            True, 'Max Level', app.ssIntImg]}
    app.drawDict1 = {'sunflower': app.sfIntImg, 
        'twinsunflower': app.twIntImg,\
             'primalsunflower': app.prIntImg,\
        'peashooter': app.psIntImg, 'repeater': app.reIntImg, \
            'threepeater': app.thIntImg,\
             'cabbagepult': app.cbIntImg, 'melonpult': app.mpIntImg,\
        'wintermelon': app.wmIntImg, 'spikeweed': app.swIntImg,\
            'spikerock': app.srIntImg, \
            'iceweed': app.iwIntImg,\
        'puffshroom': app.pusIntImg, 'fumeshroom': app.fsIntImg, \
            'sporeshroom': app.ssIntImg}
    app.plantUpgradeDict = {'sunflower': 'twinsunflower', \
        'twinsunflower': 'primalsunflower',
    'primalsunflower': 'primalsunflower', 'peashooter': 'repeater', \
        'repeater': 'threepeater',
    'threepeater': 'threepeater', 'cabbagepult': 'melonpult', \
        'melonpult': 'wintermelon',
    'wintermelon': 'wintermelon', 'spikeweed': 'spikerock', \
        'spikerock': 'iceweed', 
    'iceweed': 'iceweed', 'puffshroom': 'fumeshroom', \
        'fumeshroom': 'sporeshroom',
    'sporeshroom': 'sporeshroom'}

    #zombie Variables#
    app.zombieStatDict = {'regularZombie': [2, 40, 1, 1, 10], 
    'coneHead': [3, 60, 1.5, 1, 150],
    'bucketHead': [4, 80, 2, 1, 200],
    'imp': [1, 20, 0.5, 2, 50],
    'gargantuar': [25, 500, 12.5, 0.5, 1250],
    'footballZombie': [5, 100, 2.5, 1, 250],
    'camelZombie': [5, 100, 2.5, 1, 250],
    'zombieBull': [10, 200, 5, 2, 500],
    'yetiZombie': [15, 300, 7.5, 1, 750],
    'flagZombie': [2, 50, 1, 1, 100],
    'zomBoss': [200, 10000, 100, 1, 1000]}
    
    #zombie pictures#
    app.flagImg = app.loadImage('flagzombie.png')
    app.regImg = app.loadImage('regularzombie.png')
    app.coneImg = app.loadImage('conehead.png')
    app.bucketImg = app.loadImage('buckethead.png')
    app.impImg = app.loadImage('imp.png')
    app.gargantuarImg = app.loadImage('gargantuar.png')
    app.footballImg = app.loadImage('footballzombie.png')
    app.camelImg = app.loadImage('camelzombie.png')
    app.bullImg = app.loadImage('zombiebull.png')
    app.yetiImg = app.loadImage('yetizombie.png')
    app.bossImg = app.loadImage('zomboss.png')

    #parts of game variables(wave stuff)#
    app.wave = 0
    app.buff = False
    app.zombieWave = []
    app.zombieWaveList = []
    app.startX = 0
    app.startY = 0
    app.drawDict2 = {'flagZombie': app.flagImg, 'coneHead': app.coneImg,\
        'bucketHead': app.bucketImg, 'gargantuar': app.gargantuarImg, \
        'footballZombie': app.footballImg, 'camelZombie': app.camelImg, \
        'zombieBull': app.bullImg, 'yetiZombie': app.yetiImg, \
        'zomBoss': app.bossImg, 'regularZombie': app.regImg, 'imp': app.impImg}

    #deathScreen#
    app.dead = False

    #projectile Images#
    app.peaImg = app.loadImage('pea.png')
    app.bigPeaImg = app.loadImage('bigpea.png')
    app.largePeaImg = app.loadImage('largepea.png')
    app.cabbageImg = app.loadImage('cabbage.png')
    app.waterMelImg = app.loadImage('watermelon.png')
    app.winterMelImg = app.loadImage('wintermel.png')
    app.sporeImg = app.loadImage('spore.png')
    app.bigSporeImg = app.loadImage('bigspore.png')
    app.largeSporeImg = app.loadImage('largespore.png')
    
    #shooting#
    app.shootTimer = 0
    app.projectileList = []
    app.projMove = 20
    app.projectileDict = {'peashooter': app.peaImg, 'repeater': app.bigPeaImg,\
        'threepeater': app.largePeaImg, 'cabbagepult': app.cabbageImg,\
        'melonpult': app.waterMelImg, 'wintermelon': app.winterMelImg,\
        'puffshroom': app.sporeImg, 'fumeshroom': app.bigSporeImg,\
        'sporeshroom': app.largeSporeImg, 'spikeweed': None,\
        'spikerock': None, 'iceweed': None}

def keyPressed(app, event):
    if app.playScreen:
        if event.key == 'Space':
            if app.pause:
                app.pause = False
                app.pauseFill = '#add8e6'
            else:
                app.pause = True
                app.pauseFill = '#00008B'

def mousePressed(app, event):
    findScreen(app, event)
    if app.helpScreen:
        if clickedBack(app, event.x, event.y):
            goBackHomeFromHelp(app)
    #QUIT SCREEN STUFF#
    if app.quitScreen:
        #quit game#
        if quitBoundsQuit(app, event.x, event.y):
            quitGame(app)        
        #return to game#
        if quitBoundsReturn(app, event.x, event.y):
            returnToGame(app)    
    #dead screen stuff#
    if app.dead:
        app.playscreen = False
        #play again#
        if playAgainBounds(app, event.x, event.y):
            playAgain(app)                
        #quit#
        if quitAfterDeadBounds(app, event.x, event.y):
            quitAfterDead(app)
    #PLAY SCREEN STUFF#
    if app.playScreen:
        #resets everything to False#
        resetFalse(app, event.x, event.y)
        #pressing quit button#
        pressedQuit(app, event.x, event.y) 
        #pressing pause button#
        pressedPause(app, event.x, event.y)
        #pressing speed button#
        pressedSpeed(app, event.x, event.y)
        #pressing a plant#
        pressingInShop(app, event.x, event.y)
        #plant pressed#
        buying(app, event.x, event.y)
        #Choosing a plant#
        choosing(app, event.x, event.y)             
        #upgrade#
        upgrading(app, event.x, event.y)
        #sell#
        selling(app, event.x, event.y)

def redrawAll(app, canvas):
    if app.homeScreen:
        drawHomescreenBackground(app, canvas)
        drawHomeScreen(app, canvas)
    if app.playScreen:
        drawInGrass(app, canvas)
        drawMap(app, canvas)
        shadeBoard(app, canvas)
        drawPlantRange(app, canvas)
        drawInterfaceBackground(app, canvas)
        drawPlants(app, canvas)
        drawQuitButton(app, canvas)
        drawPauseButton(app, canvas)
        drawSpeedUpButton(app, canvas)
        drawBuyInterface(app, canvas)
        drawBottomInterface(app, canvas)

        drawZombies(app, canvas)
        drawProjectiles(app, canvas)
    if app.quitScreen:
        quitScreen(app, canvas)
    if app.dead:
        deadScreen(app, canvas)
    if app.helpScreen:
        drawHelpScreen(app, canvas)
        drawBackButton(app, canvas)

def timerFired(app):
    checkSpeed(app)
    app.timerDelay = app.speeded
    if app.dead or app.quitScreen or app.pause:
        return None
    if app.playScreen:
        increaseTimers(app)
        removeDeadZombies(app)
        checkIfDead(app)  
        callNewWave(app)
        drawInZombies(app)
        moveZombies(app)
        findZombiePath(app)
        zombieDealDamage(app)
        shooting(app)
        moveProjectile(app)
        generateSun(app)
        spikesDoDamage(app)
        buffZombies(app)

#draws homescreen background#
def drawHomescreenBackground(app, canvas):
    canvas.create_image(app.width/2, app.height/2, \
        image=ImageTk.PhotoImage(app.hsbgImg))

#draws in the grass#
def drawInGrass(app, canvas):
    canvas.create_image(app.width*2/5, app.height*2/5, \
        image=ImageTk.PhotoImage(app.grassImg))

#draws interface background#
def drawInterfaceBackground(app, canvas):
    canvas.create_image(app.width*2/5, app.height*9/10, \
        image=ImageTk.PhotoImage(app.wood1Img))
    canvas.create_image(app.width*9/10, app.height/2, \
        image=ImageTk.PhotoImage(app.wood2Img))

#finds what screen everything is on#
def findScreen(app, event):
    if app.homeScreen:
        if event.x > app.width*6.5/12 and event.x < app.width*10.5/12:
            if event.y > app.height*4.5/8 and event.y < app.height*6.5/8:
                app.homeScreen = False
                app.helpScreen = True
        if event.x > app.width*1.5/12 and event.x < app.width*5.5/12:
            if event.y > app.height*4.5/8 and event.y < app.height*6.5/8:
                app.homeScreen = False
                app.playScreen = True
                createTrail(app)
                findZombiePath(app)
                app.startX = app.trailList[-1][0]*app.boxX + app.boxX
                app.startY = app.trailList[-1][1] + app.boxY/2

#draws home screen#
def drawHomeScreen(app, canvas):
        canvas.create_text(app.width/2, app.height/6, 
        font='Arial 70 bold', text = 'Plants vs Zombies')
        canvas.create_text(app.width/2, app.height/3, 
        font='Arial 70 bold', text = 'Tower Defense!')
        canvas.create_rectangle(app.width*1.5/12, app.height*4.5/8, \
            app.width*5.5/12,
        app.height*6.5/8, outline = 'black', width = 3, fill = '#b5651d')
        canvas.create_text(app.width*3.5/12, app.height*5.5/8, 
        font='Arial 55 bold', text = 'Play!')
        canvas.create_rectangle(app.width*6.5/12, app.height*4.5/8, \
            app.width*10.5/12,
        app.height*6.5/8, outline = 'black', width = 3, fill = '#b5651d')
        canvas.create_text(app.width*8.5/12, app.height*5.5/8, 
        font='Arial 55 bold', text = 'Help')

#draws help screen#
def drawHelpScreen(app, canvas):
    canvas.create_text(app.width/2, app.height/6, 
    font='Arial 40 bold', text = 'Welcome to Plants vs Zombies Tower Defense!')
    canvas.create_text(app.width/2, app.height*2/6, 
        font='Arial 20 bold', text = 
    'The objective of the game is to defend against the zombies for as long \
as possible.')
    canvas.create_text(app.width/2, app.height*2.5/6, 
        font='Arial 20 bold', text = 
    'We can do this by buying and upgrading plants that will shoot projectiles \
at the zombies.')
    canvas.create_text(app.width/2, app.height*3/6, 
        font='Arial 20 bold', text = 
    'Plants can be bought and upgraded using sun.')
    canvas.create_text(app.width/2, app.height*3.5/6, 
        font='Arial 20 bold', text = 
    'Sun is generated by sunflowers and awarded upon zombie kill.')
    canvas.create_text(app.width/2, app.height*4/6, 
        font='Arial 20 bold', text = 
    'If the zombie reaches the end of the trail, you will lose health.')
    canvas.create_text(app.width/2, app.height*4.5/6, 
        font='Arial 20 bold', text = 
    'If this health drops below 0, you will die.')
    canvas.create_text(app.width/2, app.height*5/6, 
        font='Arial 20 bold', text = 
    'The game goes by waves and the waves get harder as the game progresses. \
Good Luck! :D')

#checks if clicked back from help screen#
def clickedBack(app, x, y):
    if x > app.width*4.1/5 and x < app.width*4.9/5:
        if y > app.height*4.7/5 and y < app.height*4.95/5:
            return True

#draws back button on help screen#
def drawBackButton(app, canvas):
    canvas.create_rectangle(app.width*4.1/5, app.height*4.7/5, app.width*4.9/5,\
         app.height*4.95/5, fill = '#b5651d', )
    canvas.create_text(app.width*9/10, app.height*9.65/10, 
        font ='Arial 20 bold',
        text = 'Back', fill = 'black')

#returns player back to homescreen from help screen#
def goBackHomeFromHelp(app):
    app.homeScreen = True
    app.helpScreen = False

#Code for Creating the Trail#
def drawMap(app, canvas):
    canvas.create_rectangle(app.width*4/5, 0, app.width*4/5, app.height, \
        width = app.borderWidth/5)
    canvas.create_rectangle(0, app.height*4/5, app.width*4/5, app.height*4/5, \
        width = app.borderWidth/5)
    canvas.create_rectangle(0, 0, 0, app.height, width = app.borderWidth)
    canvas.create_rectangle(0, 0, app.width, 0, width = app.borderWidth)
    for xcord in range(20):
        for ycord in range(15):
            canvas.create_rectangle(app.width/25*(xcord), \
                app.height*4/75*(ycord),\
                app.width/25*(xcord+1), app.height*4/75*(ycord+1))

#creates the trail#
def createTrail(app):
    if not app.noTrail:
        return None
    startBoxY = random.randint(0, 14)
    startX = 0
    startY = startBoxY*app.boxY
    while startX < 19:
        if startX == 0:
            app.trailList.append([startX, startY])
            startX += 1
            app.trailList.append([startX, startY])
        move = random.randint(-1, 1)
        if move == -1:
            startY -= app.boxY
            if isLegal(app, startX, startY):
                app.trailList.append([startX, startY])
                app.moving.append('down')
            else:
                startY += app.boxY
        if move == 0:
            startX += 1
            app.trailList.append([startX, startY])
            app.moving.append('left')
        if move == 1:
            startY += app.boxY
            if isLegal(app, startX, startY):
                app.trailList.append([startX, startY])
                app.moving.append('up')
            else:
                startY -= app.boxY
    app.moving.append('left')
    app.noTrail = False

#checks if block is legal#
def isLegal(app, startX, startY):
    if startY < 0 or (startY + app.boxY) > app.height*4/5:
        return False
    if len(app.trailList) >= 2:
        elem = app.trailList[-2]
        if compare(elem[0], elem[1], startX, startY):
            return False
    if len(app.trailList) >= 3:
        elem1 = app.trailList[-1]
        elem2 = app.trailList[-3]
        if round(elem1[0] - startX) == 0:
            if round(elem2[1] - startY) == 0:
                return False
    return True

#helper for islegal#
def compare(prevX, prevY, x, y):
    if round(prevX - x) == 0 and round(prevY - y) == 0:
        return True
    return False

#shades in the track#
def shadeBoard(app, canvas):
    for entry in app.trailList:
        canvas.create_rectangle(entry[0]*app.boxX, entry[1], \
            (entry[0]+1)*app.boxX, (entry[1]+app.boxY), fill = '#b5651e')
    if True in app.plantClickList:
        plantNum = app.plantClickList.index(True)
        plantX = app.plantList[plantNum][1]
        plantY = app.plantList[plantNum][2]
        canvas.create_rectangle(plantX//(app.boxX)*app.boxX,\
            plantY//(app.boxY)*app.boxY,\
            plantX//(app.boxX)*app.boxX + app.boxX,\
            plantY//(app.boxY)*app.boxY + app.boxY, fill = 'yellow')
       
#Code for Quit Button#
def drawQuitButton(app, canvas):
    canvas.create_rectangle(app.width*4.1/5, app.height*4.7/5, app.width*4.9/5,\
         app.height*4.95/5, fill = 'red', )
    canvas.create_text(app.width*9/10, app.height*9.65/10, 
        font ='Arial 20 bold',
        text = 'Quit?', fill = 'black')

#code for drawing pause#
def drawPauseButton(app, canvas):
    canvas.create_rectangle(app.width*4.1/5, app.height*4.4/5, app.width*4.9/5,\
         app.height*4.65/5, fill = f'{app.pauseFill}', )
    canvas.create_text(app.width*9/10, app.height*9.05/10, 
        font ='Arial 20 bold',
        text = 'Pause?', fill = 'black')

#drawing speedUp#
def drawSpeedUpButton(app, canvas):
    canvas.create_rectangle(app.width*4.1/5, app.height*4.1/5, app.width*4.9/5,\
         app.height*4.35/5, fill = f'{app.speedFill}')
    canvas.create_text(app.width*9/10, app.height*8.45/10, 
        font ='Arial 20 bold',
        text = 'Speed Up?', fill = 'black')

#checks if game is sped up or not
def checkSpeed(app):
    if app.speed:
        app.speeded = 5
    else: 
        app.speeded = 20

#checks if ur pressing on the quit button#
def pressedQuit(app, x, y):
    if x > app.width*4.1/5 and x < app.width*4.9/5:
        if y > app.height*4.7/5 and y < app.height*4.95/5:
            app.quitScreen = True 

#checks if ur pressing on the quit button#
def pressedPause(app, x, y):
    if x > app.width*4.1/5 and x < app.width*4.9/5:
        if y > app.height*4.4/5 and y < app.height*4.65/5:
            if app.pause:
                app.pause = False
                app.pauseFill = '#add8e6'
            else:
                app.pause = True
                app.pauseFill = '#00008B'

#checks if ur pressing on the quit button#
def pressedSpeed(app, x, y):
    if x > app.width*4.1/5 and x < app.width*4.9/5:
        if y > app.height*4.1/5 and y < app.height*4.35/5:
            if app.speed:
                app.speed = False
                app.speedFill = '#90EE90'
            else:
                app.speed = True
                app.speedFill = '#006400'

#Code for Quit interface#
def quitScreen(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, 
        fill = '#F0F8FF')
    canvas.create_text(app.width/2, app.height/3, 
        font ='Arial 40 bold',
        text = 'Are You Sure You Want To Quit?', fill = 'black')
    canvas.create_rectangle(app.width/6, app.height*7/12, app.width/2.5, \
        app.height*3/4, width = app.borderWidth/2)
    canvas.create_rectangle(app.width*3/5, app.height*7/12, app.width*5/6, \
        app.height*3/4, width = app.borderWidth/2)
    canvas.create_text(app.width*17/60, app.height*8/12, \
        font = 'Arial 30 bold', text = 'Yes :(')
    canvas.create_text(app.width*43/60, app.height*8/12, \
        font = 'Arial 30 bold', text = 'No :)')

#draws the death screen
def deadScreen(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, 
        fill = '#F0F8FF')
    canvas.create_text(app.width/2, app.height/3, 
        font ='Arial 40 bold',
        text = f'You died on wave {app.wave}', fill = 'black')
    canvas.create_rectangle(app.width/6, app.height*7/12, app.width/2.5, \
        app.height*3/4, width = app.borderWidth/2)
    canvas.create_rectangle(app.width*3/5, app.height*7/12, app.width*5/6, \
        app.height*3/4, width = app.borderWidth/2)
    canvas.create_text(app.width*17/60, app.height*8/12, \
        font = 'Arial 30 bold', text = 'Play Again')
    canvas.create_text(app.width*43/60, app.height*8/12, \
        font = 'Arial 30 bold', text = 'Go Home')

#Code for Right Side Interface#
def drawBuyInterface(app, canvas):
    #Buy Symbol#
    canvas.create_text(app.width*9/10, app.height*.66/24, \
        text = f'Health: {app.health}', font = 'Arial 16')
    canvas.create_text(app.width*9/10, app.height*1.5/24, \
        text = f'Sun: {app.sun}', font = 'Arial 16')
    canvas.create_text(app.width*9/10, app.height*2.33/24, \
        text = f'Current Wave: {app.wave}', font = 'Arial 16')
    canvas.create_rectangle(app.width*4/5, app.height/8, app.width, \
        app.height/8, width = app.borderWidth/10)
    canvas.create_text(app.width*9/10, app.height*1.25/8, text = "Dave's Shop",\
        font = 'Ariel 20')
    #sunflower#
    canvas.create_rectangle(app.width*4/5, app.height*1.5/8, app.width, \
        app.height*2.5/8, width = app.borderWidth/5, fill = f'{app.buyFill[0]}')
    canvas.create_image(app.width*8.5/10, app.height*2/8, \
        image=ImageTk.PhotoImage(app.sfIntImg))
    canvas.create_text(app.width*9.5/10, app.height*1.8/8, text = 'Sunflower',\
        font='Arial 11')
    canvas.create_text(app.width*9.5/10, app.height*2.2/8, \
        text = f'Cost: {app.sunFlower[0][2]}', font='Arial 11')
    #peashooter#
    canvas.create_rectangle(app.width*4/5, app.height*2.5/8, app.width, \
        app.height*3.5/8, width = app.borderWidth/5, fill = f'{app.buyFill[1]}')
    canvas.create_image(app.width*8.5/10, app.height*3/8, \
        image=ImageTk.PhotoImage(app.psIntImg))
    canvas.create_text(app.width*9.5/10, app.height*2.8/8, text = 'Peashooter',\
        font='Arial 11')
    canvas.create_text(app.width*9.5/10, app.height*3.2/8, \
        text = f'Cost: {app.peaShooter[0][2]}', font='Arial 11')
    #cabagePult#
    canvas.create_rectangle(app.width*4/5, app.height*3.5/8, app.width, \
        app.height*4.5/8, width = app.borderWidth/5, fill = f'{app.buyFill[2]}')
    canvas.create_image(app.width*8.5/10, app.height*4/8, \
        image=ImageTk.PhotoImage(app.cbIntImg))
    canvas.create_text(app.width*9.5/10, app.height*3.8/8, \
        text = 'Cabbage-Pult',\
        font='Arial 11')
    canvas.create_text(app.width*9.5/10, app.height*4.2/8, \
        text = f'Cost: {app.cabbagePult[0][2]}', font='Arial 11')
    #spikeweed#
    canvas.create_rectangle(app.width*4/5, app.height*4.5/8, app.width, \
        app.height*5.5/8, width = app.borderWidth/5, fill = f'{app.buyFill[3]}')
    canvas.create_image(app.width*8.5/10, app.height*5/8, \
        image=ImageTk.PhotoImage(app.swIntImg))
    canvas.create_text(app.width*9.5/10, app.height*4.8/8, text = 'Spikeweed',\
        font='Arial 11')
    canvas.create_text(app.width*9.5/10, app.height*5.2/8, \
        text = f'Cost: {app.spikeWeed[0][2]}', font='Arial 11')
    #puffshroom#
    canvas.create_rectangle(app.width*4/5, app.height*5.5/8, app.width, \
        app.height*6.5/8, width = app.borderWidth/5, fill = f'{app.buyFill[4]}')
    canvas.create_image(app.width*8.5/10, app.height*6/8, \
        image=ImageTk.PhotoImage(app.pusIntImg))
    canvas.create_text(app.width*9.5/10, app.height*5.8/8, \
        text = 'Puff-Shroom',\
        font='Arial 11')
    canvas.create_text(app.width*9.5/10, app.height*6.2/8, \
        text = f'Cost: {app.puffShroom[0][2]}', font='Arial 11')
    
#adds plant to cur list of plants#
def addplant(app, xcord, ycord, plant):
    if isLegalPlant(app, xcord, ycord, plant):
        index = len(app.plantList)
        if app.sun >= app.plantStatDict[f'{plant}'][2]:
            app.plantList.append([plant, xcord, ycord, index, 0])
            app.sun -= app.plantStatDict[f'{plant}'][2]
            app.plantClickList.append(False)

#checks if the place the player is trying to place the plant is legal#
def isLegalPlant(app, xcord, ycord, plant):
    if plant == 'spikeweed':
        for tile in app.trailList:
            if xcord > tile[0]*app.boxX and xcord < (tile[0]+1)*app.boxX:
                if ycord > tile[1] and ycord < tile[1] + app.boxY:
                    return True
        return False
    else:
        for tile in app.trailList:
            if xcord > tile[0]*app.boxX and xcord < (tile[0]+1)*app.boxX:
                if ycord > tile[1] and ycord < tile[1] + app.boxY:
                    return False
        return True

#draws the list of plants#
def drawPlants(app, canvas):
    for plant in app.plantList:
        canvas.create_image(plant[1]//(app.boxX)*app.boxX + app.boxX/2, \
            plant[2]//(app.boxY)*app.boxY + app.boxY/2, \
            image=ImageTk.PhotoImage(app.drawDict[plant[0]]))

#finds index of clicked plants#
def getIndex(app, xCord, yCord):
    for plant in app.plantList:
        if compare1(app, xCord, yCord, plant[1], plant[2]):
            return plant[3]
    return None

#helper for clicking plants#
def compare1(app, x0, y0, x1, y1):
    if x0 < app.width*4/5 and y0 > app.height*4/5:
        return False
    if x0 > x1//app.boxX*app.boxX and x0 < x1//app.boxX*app.boxX + app.boxX:
        if y0 > y1//app.boxY*app.boxY and y0 < y1//app.boxY*app.boxY + app.boxY:
            return True
    return False

#draws bottom interface#
def drawBottomInterface(app, canvas):
    if True in app.plantClickList:
        plantNum = app.plantClickList.index(True)
        plantType = app.plantList[plantNum][0]
        listOfStuff = app.plantStatDict[plantType]
        upgradePlant = app.plantUpgradeDict[plantType]
        if upgradePlant != plantType:
            canvas.create_text(app.width*4/10, app.height*9.0/10, \
            text = f'Upgrade Cost: {app.plantStatDict[upgradePlant][2]}', \
                font = 'Arial 12')
        else: 
            canvas.create_text(app.width*4/10, app.height*9.0/10, \
            text = f'Cost: {app.plantStatDict[upgradePlant][2]}', \
                font = 'Arial 12')
        canvas.create_text(app.width*.875/10, app.height*8.33/10, \
            text = f'{listOfStuff[0]}', font = 'Arial 12')
        canvas.create_image(app.width*.875/10, app.height*9.25/10, \
            image=ImageTk.PhotoImage(app.drawDict1[plantType]))
        canvas.create_text(app.width*5.5/10, app.height*8.33/10, \
            text = f'Sun Production: {app.plantStatDict[plantType][5]}', \
                font = 'Arial 12')
        canvas.create_text(app.width*5.5/10, app.height*9.0/10, \
            text = f'Projectile Number: {app.plantStatDict[plantType][6]}', \
                font = 'Arial 12')
        canvas.create_text(app.width*5.5/10, app.height*9.66/10, \
            text = f'Splash?: {app.plantStatDict[plantType][7]}', \
                font = 'Arial 12')
        canvas.create_text(app.width*4/10, app.height*8.33/10, \
            text = f'Damage: {app.plantStatDict[plantType][1]}', \
                font = 'Arial 12')
        canvas.create_text(app.width*4/10, app.height*9.66/10, \
            text = f'Range(tiles): {app.plantStatDict[plantType][3]}', \
                font = 'Arial 12')
        canvas.create_text(app.width*2.5/10, app.height*8.33/10, \
            text = f'Kills: {app.plantList[plantNum][4]}', font = 'Arial 12')
        canvas.create_text(app.width*2.5/10, app.height*9.33/10, \
            text = f'Sell for {app.plantStatDict[plantType][4]}?', \
                font = 'Arial 12')
        canvas.create_rectangle(app.width*2/10, app.height*9/10, \
            app.width*3/10, app.height*9.66/10, width = app.borderWidth/10)
        canvas.create_text(app.width*7.125/10, app.height*8.33/10, \
            text = f'{app.plantStatDict[plantType][8]}', font = 'Arial 12')
        canvas.create_image(app.width*7.125/10, app.height*9.25/10, \
            image=ImageTk.PhotoImage(app.plantStatDict[plantType][9]))
        #splitting Lines#
        canvas.create_rectangle(app.width*1.75/10, app.height*8/10, \
            app.width*1.75/10, app.height, width = app.borderWidth/10)
        canvas.create_rectangle(app.width*3.25/10, app.height*8/10, \
            app.width*3.25/10, app.height, width = app.borderWidth/10)
        canvas.create_rectangle(app.width*6.25/10, app.height*8/10, \
            app.width*6.25/10, app.height, width = app.borderWidth/10)

#draws range circle#
def drawPlantRange(app, canvas):
    if True in app.plantClickList:
        plantNum = app.plantClickList.index(True)
        plantName = app.plantList[plantNum][0]
        plantX = int(str(app.plantList[plantNum][1]))
        plantY = int(str(app.plantList[plantNum][2]))
        xCord = plantX//app.boxX*app.boxX + app.boxX/2
        yCord = plantY//app.boxY*app.boxY + app.boxY/2
        rangeDist = app.plantStatDict[plantName][3]*app.boxX
        canvas.create_oval(xCord - rangeDist,\
            yCord - rangeDist,\
            xCord + rangeDist,\
            yCord + rangeDist, width = app.borderWidth/3, outline = 'black')

#helper for buying/selling#
def getTrueIndex(app):
    return app.plantClickList.index(True)

#calls the waves#
def callNewWave(app):
    if app.zombieWaveList == []:
        app.wave += 1
        appendList = waveGenerator(app.wave)
        for entry in appendList:
            app.zombieWave.append([entry, app.startX, app.startY, 0,\
                app.zombieStatDict[entry][1]])
        
#recursive function to generate wave#b
def waveGenerator(wave):
    limit = 2*wave-1
    newList = ['flagZombie']
    curSum = 1
    zombieList = ['regularZombie', 'coneHead', 'bucketHead', 'imp',\
        'gargantuar', 'footballZombie', 'camelZombie', 'zombieBull',\
        'yetiZombie', 'zomBoss']
    waveDict = {'regularZombie': 1, 'coneHead': 1.5, 'bucketHead': 2,\
        'imp': 0.5, 'gargantuar': 12.5, 'footballZombie': 2.5,\
            'camelZombie': 2.5, 'zombieBull': 5, 'yetiZombie': 7.5,\
                'zomBoss': 100}
    if waveGeneratorHelper(limit, curSum, newList, zombieList, waveDict):
        return newList

#helper for wavegenerator#
def waveGeneratorHelper(limit, curSum, newList, zombieList, waveDict):
    if curSum == limit:
        return True
    foundOne = False
    while not foundOne:
        zombieNum = random.randint(0, 9)
        zombie = zombieList[zombieNum]
        zombieVal = waveDict[zombie]
        if curSum + zombieVal <= limit:
            newList.append(zombie)
            curSum += zombieVal
            foundOne = True
        continue
    return waveGeneratorHelper(limit, curSum, newList, zombieList, waveDict)

#moves the zombies#
def findZombiePath(app):
    length = len(app.moving) - 1
    for zombie in app.zombieWaveList:
        speed = app.zombieStatDict[zombie[0]][3]
        curSpot = int(length - zombie[3]*speed//(app.moveDiff))
        direction = app.moving[curSpot]
        if direction == 'up':
            zombie[2] -= speed*app.boxY/app.moveDiff
        if direction == 'down':
            zombie[2] += speed*app.boxY/app.moveDiff
        if direction == 'left':
            zombie[1] -= speed*app.boxX/app.moveDiff

#spawns zombies#
def drawInZombies(app):
    if app.zombieWave == []:
        return None
    if app.zombieWaveList == []:
        zombie = app.zombieWave[0]
        app.zombieWaveList.append(zombie)
        app.zombieWave.pop(0)
    else:
        if app.timer%app.delay == 0:
            app.timer = 0
            zombie = app.zombieWave[0]
            app.zombieWaveList.append(zombie)
            app.zombieWave.pop(0)

#draws zombies#
def drawZombies(app, canvas):
    for zombie in app.zombieWaveList:
        if zombie[1] + app.boxX/4 < app.boxX*19.75:
            canvas.create_image(zombie[1] + app.boxX/4, zombie[2] - app.boxY/2,\
            image=ImageTk.PhotoImage(app.drawDict2[zombie[0]]))

#deals damage when zombie reaches end#
def zombieDealDamage(app):   
    for zombie in app.zombieWaveList:
        if zombie[1] <= 0:
            app.health -= app.zombieStatDict[zombie[0]][0]
            app.zombieWaveList.pop(0)

#moves Zombies#
def moveZombies(app):
    for zombie in app.zombieWaveList:
            zombie[3] += 1

#generates sun#
def generateSun(app):
    newList = []
    for plant in app.plantList:
        newList.append(plant[0])
    sunflowerNum = newList.count('sunflower')
    twinNum = newList.count('twinsunflower')
    primalNum = newList.count('primalsunflower')
    sunGen = app.plantStatDict['sunflower'][5]
    twinGen = app.plantStatDict['twinsunflower'][5]
    primGen = app.plantStatDict['primalsunflower'][5]
    app.sun += sunGen*sunflowerNum + twinGen*twinNum + primGen*primalNum

#shoots zombies#           
def shooting(app):
    if app.shootTimer%10 == 0:
        #app.shootTimer = 0
        for plant in app.plantList:
            findFurthestZombie(app, plant)

#finds furthest zombie#
def findFurthestZombie(app, plant): 
    curZombie = [0, app.width, 0, 0]
    for zombie in app.zombieWaveList:
        if inRange(app, plant, zombie):
            if zombie[1] < curZombie[1]:
                curZombie = zombie
    if curZombie == [0, app.width, 0, 0]:
        return 
    fireProjectile(app, plant, curZombie)
    
#checks if in range#
def inRange(app, plant, zombie):
    plantName = plant[0]
    range = app.plantStatDict[plantName][3]*app.boxX
    plantDist = (zombie[1] - plant[1])**2 + (zombie[2] - plant[2])**2
    if plantDist <= range**2:
        return True
    return False

#adds projectile into the projList#
def fireProjectile(app, plant, zombie):
    projDist = ((plant[1]-zombie[1])**2 + (plant[2]-zombie[2])**2)**(1/2)
    app.projectileList.append([plant[0], plant[1], plant[2], \
        zombie, 0, projDist])

#moves projectiles#
def moveProjectile(app):
    for projectile in app.projectileList:
        for i in range (app.projMove):
            if projectile[3][-1] <= 0:
                app.projectileList.remove(projectile)
                break
            zombieX = projectile[3][1]
            zombieY = projectile[3][2]
            projX = projectile[1]
            projY = projectile[2]
            plantName = projectile[0]
            if plantName == 'spikeweed' or plantName == 'spikerock' or \
                plantName == 'iceweed':
                break
            plantDmg = app.plantStatDict[plantName][1]
            if projX >= 10**31:
                continue
            if ((zombieX - projX)//1)**2 + \
                ((zombieY - projY)//1)**2 <=\
                 (app.projMove)**2:
                if app.plantStatDict[plantName][7]:
                    zombIndex = projectile[3][3]
                    for zombie in app.zombieWaveList:
                        if abs(zombie[3] - zombIndex) <= 1:
                            zombie[-1] -= plantDmg
                else:
                    projectile[3][-1] -= plantDmg
                app.projectileList.remove(projectile)
                break   
            else:
                xDist = (zombieX - projX)
                yDist = (zombieY - projY)
                fracX = 1/2*xDist/abs(xDist+yDist)
                fracY = 1/2*yDist/abs(xDist+yDist)
                curDist = ((xDist//1)**2 + (yDist//1)**2)**(1/2)
                frac = curDist/projectile[-1] + .1
                projectile[1] += frac*3*fracX
                projectile[2] += frac*3*fracY

#draws projectiles#              
def drawProjectiles(app, canvas):
    for projectile in app.projectileList:
        projectileIm = app.projectileDict[projectile[0]]
        projX = projectile[1]
        projY = projectile[2]
        if projectileIm != None:
            canvas.create_image(projX, projY, \
                image=ImageTk.PhotoImage(projectileIm))

#increases timers by intervals#
def increaseTimers(app):
    app.timer += 1
    app.shootTimer += 1

#pops dead zombies#
def removeDeadZombies(app):
    for zombie in app.zombieWaveList:
            if zombie[4] <= 0:
                zombieName = zombie[0]
                app.sun += app.zombieStatDict[zombieName][4]
                app.zombieWaveList.remove(zombie)

#checks if the player is dead#
def checkIfDead(app):
    if app.health <= 0:
            app.dead = True 
        
#quits out of game#
def quitBoundsQuit(app, x, y):
    if x > app.width/6 and x < app.width/2.5:
            if y > app.height*7/12 and y < app.height*3/4:
                return True
    return False

#returns to game#
def quitBoundsReturn(app, x, y):
    if x > app.width*3/5 and x < app.width*5/6:
            if y > app.height*7/12 and y < app.height*3/4:
                return True
    return False

#reset variables for quitting out of game#
def quitGame(app):
    app.quitScreen = False
    app.homeScreen = True
    app.playScreen = False
    app.speed = False
    app.pause = False
    app.trailList = []
    app.noTrail = True
    app.plantList = []
    app.zombieWave = []
    app.projectileList = []
    app.sun = app.startSun
    app.zombieWaveList = []
    app.wave = 0
    app.health = app.startHealth
    app.speedFill = '#90EE90'
    app.pauseFill = '#add8e6'

#reset variables for returning to game#
def returnToGame(app):
    app.quitScreen = False
    app.playScreen = True

#bounds for play again#
def playAgainBounds(app, x, y):
    if x > app.width/6 and x < app.width/2.5:
        if y > app.height*7/12 and y < app.height*3/4:
            return True
    return False

#reset variables for play again#
def playAgain(app):
    app.wave = 0
    app.dead = False
    app.trailList = []
    app.noTrail = True
    app.plantList = []
    app.zombieWave = []
    app.projectileList = []
    app.sun = app.startSun
    app.zombieWaveList = []
    app.health = app.startHealth
    app.playScreen = True
    app.speed = False
    app.pause = False
    app.speedFill = '#90EE90'
    app.pauseFill = '#add8e6'
    createTrail(app)
    app.startX = app.trailList[-1][0]*app.boxX + app.boxX
    app.startY = app.trailList[-1][1] + app.boxY/2

#bounds for quit out after death#
def quitAfterDeadBounds(app, x, y):
    if x > app.width*3/5 and x < app.width*5/6:
            if y > app.height*7/12 and y < app.height*3/4:
                return True
    return False

#reset variables for quitting out after death#
def quitAfterDead(app):
    app.dead = False
    app.homeScreen = True
    app.playScreen = False
    app.trailList = []
    app.noTrail = True
    app.plantList = []
    app.zombieWave = []
    app.projectileList = []
    app.speedFill = '#90EE90'
    app.pauseFill = '#add8e6'
    app.sun = app.startSun
    app.zombieWaveList = []
    app.wave = 0
    app.health = app.startHealth
    app.speed = False
    app.pause = False

#resets plant indicies to false when click off plant#
def resetFalse(app, x, y):
    if x > 0 and x < app.width*4/5:
        if y > 0 and y < app.height*4/5:
            numPlants = len(app.plantClickList)
            app.plantClickList = [False]*numPlants

#changes shop color for click#
def pressingInShop(app, x, y):
    if x > app.width*4/5 and x < app.width:
            for j in range(5):
                if y > app.height*(1.5 + j)/8 and \
                    y < app.height*(2.5 + j)/8:
                    if app.buyFill[j] == 'green':
                        app.buyFill[j] = ''
                        app.buy[j] = False
                    else:
                        for i in range(5):
                            app.buyFill[i] = ''
                            app.buy[i] = False
                        app.buyFill[j] = 'green'
                        app.buy[j] = True

#buy plant#
def buying(app, x, y):
    for i in range(5):
        if app.buy[i]:
            if x > 0 and x < app.width*4/5:
                if y > 0 and y < app.height*4/5:
                    app.buy[i] = False
                    app.buyFill[i] = ''
                    if isBuyingLegal(app, x, y):
                        addplant(app, x, y, app.plant[i])

#helper for buying#
def isBuyingLegal(app, xcord, ycord):
    for plant in app.plantList:
        if xcord > plant[1]//app.boxX*app.boxX and \
            xcord < plant[1]//app.boxX*app.boxX + app.boxX:
            if ycord > plant[2]//app.boxY*app.boxY and \
                ycord < plant[2]//app.boxY*app.boxY + app.boxY:
                return False
    return True

#choosing a plant#
def choosing(app, x, y):
    if x < app.width*4/5 and y < app.height*4/5:
        if getIndex(app, x, y) != None:
            index = getIndex(app, x, y)
            app.plantClickList[index] = True   

#upgrading a plant#
def upgrading(app, x, y):
    if x > app.width*6.25/10 and x < app.width*8/10:
        if y > app.height*4/5 and y < app.height:
            if True in app.plantClickList:
                changeIndex = getTrueIndex(app)
                plant = app.plantList[changeIndex][0]
                newPlant = app.plantUpgradeDict[plant]
                if app.sun >= app.plantStatDict[f'{newPlant}'][2]:
                    app.plantList[changeIndex][0] = newPlant
                    app.sun -= app.plantStatDict[f'{newPlant}'][2]

#selling a plant#
def selling(app, x, y):
    if x > app.width*2/10 and x < app.width*3/10:
        if y > app.height*9/10 and y < app.height*9.66/10:
            if True in app.plantClickList:
                changeIndex = getTrueIndex(app)
                plant = app.plantList[changeIndex][0]
                app.plantList.pop(changeIndex)
                app.plantClickList.pop(changeIndex)
                app.sun += app.plantStatDict[f'{plant}'][4]

#spikes killing stuff#
def spikesDoDamage(app):
    if app.shootTimer% 2 == 0:
        for plant in app.plantList:
            if plant[0] == 'spikeweed':
                for zombie in app.zombieWaveList:
                    if inRange(app, plant, zombie):
                        zombie[-1] -= app.plantStatDict['spikeweed'][1]
            if plant[0] == 'spikerock':
                for zombie in app.zombieWaveList:
                    if inRange(app, plant, zombie):
                        zombie[-1] -= app.plantStatDict['spikerock'][1]
            if plant[0] == 'iceweed':
                for zombie in app.zombieWaveList:
                    if inRange(app, plant, zombie):
                        zombie[-1] -= app.plantStatDict['iceweed'][1]
                        
#scalar difficulty for zombies#
def buffZombies(app):
    if app.wave%10 != 0:
        app.buff = True
    if app.wave%10 == 0 and app.buff:
        app.buff = False
        for key in app.zombieStatDict:
            app.zombieStatDict[key][1] *= 2

runApp(width = 1280, height = 720)









