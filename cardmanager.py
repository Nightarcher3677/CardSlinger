#imports
import pygame
import time
import os
import subprocess

def titleswitch():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        return False
    if keys[pygame.K_LEFT]:
        return True
