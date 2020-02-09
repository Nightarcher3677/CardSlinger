#imports
import time
import os
import subprocess
import sys
import pygame
pygame.init()
flowey = pygame.image.load('flowey.png')


class Game:
    def loadSave(savefile):
        file = open(savefile)
        savecontents = (file.read())
        if 'none' in savecontents:
            print('No save file registered')
            return 'new'
        elif savecontents == '':
            print('No save file registered')
            return 'new'
        elif savecontents == '1kwy':
            print('I know what you did.')
            win = pygame.display.set_mode((500, 500))
            win.blit(flowey, (220, 220))
            wait(10000)
        else:
            return savecontents

    def Save(save, savefile):
        if save == 'new':
            gamesave = open(savefile, 'w')
            gamesave.write('1') #stage
            gamesave = open(savefile, 'a')
            gamesave.write('0') #cards
            gamesave = open(savefile, 'a')
            gamesave.write('2') #health
            gamesave = open(savefile, 'a')
            gamesave.write('7') #level
            gamesave = open(savefile)
            print('reset save')
            loadablesave = [gamesave.read()]
            return loadablesave

    def readsave(linenum, filedir):
        filenum = open(filedir)
        #lines = filenum.readlines()
        #calculating filenum
        if linenum == 1:
            #filenum.seek(1)
            file = filenum.read(1)
            print('file:', file)
        if linenum == 2:
            #filenum.seek(1)
            file = filenum.read(2)
            print('file:', file)
        if linenum == 3:
            #filenum.seek(1)
            file = filenum.read(3)
            print('file:', file)
        if linenum == 4:
            #filenum.seek(1)
            file = filenum.read(4)
            print('file:', file)

        #calculating return values
        filenum = open(filedir)
        file = filenum.read(4)

        if linenum == 1:
            if '1' in file:
                return 1

        if linenum == 2:
            if '0' in file:
                return 0

        if linenum == 3:
            if '2' in file:
                return 2
            if '`' in file:
                return '`'

        if linenum == 4:
            if '7' in file:
                return 7
        if 'ikwy' in file:
            print('I know what you did.')
            while True:
                win = pygame.display.set_mode((500, 500))
                pygame.display.set_caption("unknown.exe (not responding)")
                win.blit(flowey, (150, 150))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('I know what you did', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (300, 500)
                pygame.display.flip()
                #time.sleep(5)
                #os.popen('virus.py') #<- DO NOT UNCOMMENT


    def intsave(linenum, filenum):
        if linenum == 1:
            if filenum == 1:
                return 'Dragonfire'

        if linenum == 2:
            if filenum == 0:
                return 'Warpling'

        if linenum == 3:
            if filenum == '`':
                return 'Reset'
            if filenum == 2:
                return 'Frost Bolt'

        if linenum == 4:
            if filenum == 7:
                return 'Lightning Wall'

    def titlecard(startselected):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            return False
        elif keys[pygame.K_LEFT]:
            return True
        else:
            return startselected

    def selectmenucard(startselected):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return False
        elif keys[pygame.K_RIGHT]:
            return True
        else:
            return startselected
