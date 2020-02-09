#imports
import pygame
import time
import os
import subprocess
from filemanager import Game
#from cardmanager import Cardpicker

#initialsiation
print('Initialising...')
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
clock = pygame.time.Clock()
#display setup
#win = pygame.display.set_mode((500, 500))
#pygame.display.set_caption("still in progress")

print('Loading Images...')
start = pygame.image.load('startbutton.png')
cursor = pygame.image.load('cursor.png')
exit = pygame.image.load('exitbutton.png')
titlebg = pygame.image.load('titlebg.png')
battleimg = pygame.image.load('battle.png')
deckimg = pygame.image.load('deck.png')

    #card images
lightningwall = pygame.image.load('cards\\lightningwall.png')
frostbolt = pygame.image.load('cards\\frostbolt.png')
reset = pygame.image.load('cards\\reset.png')
warpling = pygame.image.load('cards\\warpling.png')
dragonfire = pygame.image.load('cards\\dragonfire.png')

print('Images Loaded!')

#checking save
save = Game.loadSave('save.txt')

#save initialisation (resets if empty, returns the save translation if not)
savecontent = Game.Save(save, 'save.txt')

print('Save Content:')
print(savecontent)

print('Linking...')
#linking save files to variables
stagenum = Game.readsave(1,'save.txt')
cardnum = Game.readsave(2,'save.txt')
healthnum = Game.readsave(3,'save.txt')
levelnum = Game.readsave(4,'save.txt')
print('Linked!')
print('Encoded values:')
print(stagenum)
print(cardnum)
print(healthnum)
print(levelnum)

print('Decoding...')
card1 = Game.intsave(1, stagenum)
card2 = Game.intsave(2, cardnum)
card3 = Game.intsave(3, healthnum)
card4 = Game.intsave(4, levelnum)
print('Decoded!')
print('Save files(decoded): \n')
print(card1)
print(card2)
print(card3)
print(card4)
print('')
if card1 == 'None' or card2 == 'None' or card3 == 'None' or card4 == 'None':
    print('Initialisation Failed.')
else:
    print('Initialisation Complete!')

print('Loading game...')
run = True
title = True
startselected = True
battle = False
deck = False
deckselected = False
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Cardslinger")
pygame.mouse.set_visible(False)
print('Game loaded!')
while run:
    #set the images depending on the Cards
    if card1 == 'Dragonfire':
        card1img = dragonfire

    if card2 == 'Warpling':
        card2img = warpling

    if card3 == 'Frost Bolt':
        card3img = frostbolt
    elif card3 == 'Reset':
        card3img = reset

    if card4 == 'lightning Wall':
        card4img = lightningwall

    clock.tick(20)
    win.blit(titlebg, (0, 0))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print('Game Exited')
    if title:
        font = pygame.font.Font('munro\munro.ttf', 45)
        text = font.render('CardSlinger', True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (250, 80)
        win.blit(text, textRect)
        startselected = Game.titlecard(startselected)
        #title = Game.titlepick(startselected)
        if startselected:
            win.blit(start, (20, 120))
            win.blit(exit, (300, 140))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                title = False
                battle = False
                deck = False
                deckselected = False
                time.sleep(0.2)
        else:
            win.blit(start, (20, 140))
            win.blit(exit, (300, 120))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                run = False
        pygame.display.flip()
    else:
        if not battle and not deck:
            deckselected = Game.selectmenucard(deckselected)
            if deckselected:
                win.blit(battleimg, (20, 140))
                win.blit(deckimg, (300, 120))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    deck = True
                    wait = True

            else:
                win.blit(battleimg, (20, 120))
                win.blit(deckimg, (300, 140))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    battle = True
                    placeholder = True
        deckselection = 1
        if deck:
            text = font.render('Deck', True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (250, 80)
            win.blit(text, textRect)

            if deckselection == 1:
                win.blit(card1img, (50, 280))
                win.blit(card3img, (150, 300))
                keys = pygame.key.get_pressed()
                if not wait:
                    if keys[pygame.K_RETURN]:
                        Placeholder = True
                wait = False
            elif deckselection == 2:
                win.blit(card1img, (20, 140))
                win.blit(card3img, (300, 120))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    placeholder = True

        elif battle:
            placeholder = True
    pygame.display.update()
