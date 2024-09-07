



import pygame
import time

pygame.init()

# Carrega e toca o arquivo de música
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

# Aguarda enquanto a música está tocando
while pygame.mixer.music.get_busy():
    time.sleep(1)  # Espera 1 segundo antes de verificar novamente
