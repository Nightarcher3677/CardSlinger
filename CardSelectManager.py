#imports
import time
import os
import subprocess
import sys
import pygame
pygame.init()

class card:
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

        def selectdeckcard(startselected, prev):
            time.sleep(0.1)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if startselected == 1:
                    return 2

                if startselected == 2:
                    return 3

                if startselected == 3:
                    return 4

            elif keys[pygame.K_LEFT]:
                if startselected == 2:
                    return 1

                if startselected == 3:

                    return 2
                if startselected == 4:

                    return 3
            else:
                return startselected

            if not startselected == 1 or not startselected == 2 or not startselected == 3 or not startselected == 4:
                return prev
