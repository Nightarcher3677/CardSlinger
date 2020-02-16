#imports
import pygame
import time
import os
import subprocess
from filemanager import Game
from CardSelectManager import card
#from socketconnect import s_func
import sys
import socket
#from cardmanager import Cardpicker

#initialsiation
print('Initialising...')
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
clock = pygame.time.Clock()
#display setup
#win = pygame.display.set_mode((500, 500))
#pygame.display.set_caption("still in progress")
print('setting up socket...')
import socket
import select
import errno

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = 'client'

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port


# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well

print('Loading Images...')
    #selection images
start = pygame.image.load('startbutton.png')
exit = pygame.image.load('exitbutton.png')
battleimg = pygame.image.load('battle.png')
deckimg = pygame.image.load('deck.png')
onlineimg = pygame.image.load('online.png')
offlineimg = pygame.image.load('offline.png')

    #card images
card1img = pygame.image.load('cards\\error.png')
card2img = pygame.image.load('cards\\error.png')
card3img = pygame.image.load('cards\\error.png')
card4img = pygame.image.load('cards\\error.png')
lightningwall = pygame.image.load('cards\\lightningwall.png')
frostbolt = pygame.image.load('cards\\frostbolt.png')
reset = pygame.image.load('cards\\reset.png')
warpling = pygame.image.load('cards\\warpling.png')
dragonfire = pygame.image.load('cards\\dragonfire.png')

    #other (backgrounds, ai sprites, etc, etc...)
titlebg = pygame.image.load('titlebg.png')

print('Images Loaded!')

#checking save
save = Game.loadSave('save.txt')
savecheck = str(save)
print('savecheck: ',savecheck)
#initialising valid saves
if '1' in savecheck or '2' in savecheck or '0' in savecheck or '7' in savecheck or '`' in savecheck or 'ikwy' in savecheck or 'new' in savecheck:
    placeholder = 1
else:
    print('ERROR: INVALID SAVE CONTENTS.')
    print('RESETTING...')
    save = 'new'

#save initialisation (resets if empty or 'new', returns the save translation if not)
savecontent = Game.Save(save, 'save.txt')

print('New Save Content:')
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
deckselection = 1
battletype = True
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

    if card4 == 'Lightning Wall':
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
        startselected = card.titlecard(startselected)
        #title = card.titlepick(startselected)
        if startselected:
            win.blit(start, (20, 120))
            win.blit(exit, (300, 140))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                pygame.mixer.music.load('card-2.mp3')
                pygame.mixer.music.play(0)
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
                pygame.mixer.music.load('card-2.mp3')
                pygame.mixer.music.play(0)
                run = False
        pygame.display.flip()
    else:
        if not battle and not deck:
            deckselected = card.selectmenucard(deckselected)
            if deckselected:
                win.blit(battleimg, (20, 140))
                win.blit(deckimg, (300, 120))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    pygame.mixer.music.load('card-2.mp3')
                    pygame.mixer.music.play(0)
                    deck = True
                    wait = True

            else:
                win.blit(battleimg, (20, 120))
                win.blit(deckimg, (300, 140))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    pygame.mixer.music.load('card-2.mp3')
                    pygame.mixer.music.play(0)
                    battle = True
                    placeholder = True
                    time.sleep(0.1)
        prev = deckselection
        deckselection = card.selectdeckcard(deckselection, prev)
        #print('deckselection: ', deckselection)
        if deck:
            text = font.render('Deck', True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (250, 80)
            win.blit(text, textRect)

            if deckselection == 1:
                win.blit(card1img, (50, 280))
                win.blit(card2img, (150, 300))
                win.blit(card3img, (250, 300))
                win.blit(card4img, (350, 300))
                keys = pygame.key.get_pressed()
                if not wait:
                    if keys[pygame.K_RETURN]:
                        pygame.mixer.music.load('card-2.mp3')
                        pygame.mixer.music.play(0)
                        Placeholder = True
                wait = False
            elif deckselection == 2:
                win.blit(card1img, (50, 300))
                win.blit(card2img, (150, 280))
                win.blit(card3img, (250, 300))
                win.blit(card4img, (350, 300))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    pygame.mixer.music.load('card-2.mp3')
                    pygame.mixer.music.play(0)
                    placeholder = True
            elif deckselection == 3:
                win.blit(card1img, (50, 300))
                win.blit(card2img, (150, 300))
                win.blit(card3img, (250, 280))
                win.blit(card4img, (350, 300))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    pygame.mixer.music.load('card-2.mp3')
                    pygame.mixer.music.play(0)

                    #dev test program
                    password = input('please enter dev code: ')
                    if password == '2219':
                        choice = input('decoded card name: ')
                        if choice == 'Reset':
                            card3 = 'Reset'
                            print('success')
                        elif choice == 'Frost Bolt':
                            card3 = 'Frost Bolt'
                            print('success')
                        elif choice == 'shell':
                            os.system('powershell')
                        else:
                            print('invalid card name for dev entry')

                    placeholder = True

            elif deckselection == 4:
                win.blit(card1img, (50, 300))
                win.blit(card2img, (150, 300))
                win.blit(card3img, (250, 300))
                win.blit(card4img, (350, 280))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    pygame.mixer.music.load('card-2.mp3')
                    pygame.mixer.music.play(0)
                    placeholder = True

        elif battle:
            text = font.render('Battle', True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (250, 80)
            win.blit(text, textRect)

            #text = font.render('Still in developement', True, (255, 255, 255))
            #textRect = text.get_rect()
            #textRect.center = (250, 250)
            #win.blit(text, textRect)
            placeholder = True
            battletype = card.selectmenucard(battletype)
            if battletype:
                win.blit(onlineimg, (20, 140))
                win.blit(offlineimg, (300, 120))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    #pygame.mixer.music.load('card-2.mp3')
                    #pygame.mixer.music.play(0)
                    #deck = True
                    #wait = True
                    placeholder = True
                    text = font.render("NOT AVAILABLE", True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (250, 250)
                    win.blit(text, textRect)

            else:
                win.blit(onlineimg, (20, 120))
                win.blit(offlineimg, (300, 140))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    #pygame.mixer.music.load('card-2.mp3')
                    #pygame.mixer.music.play(0)
                    #battle = True
                    placeholder = True
                    text = font.render("LOCAL MULTIPLAYER ONLY", True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (250, 250)
                    win.blit(text, textRect)
                    onlinebattle = True
                    IP = "127.0.0.1"
                    #client_socket.connect((IP, PORT))
                    # Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
                    #client_socket.setblocking(False)
                    while onlinebattle:
                        battle = False
                        onlinebattle = False



    pygame.display.update()
