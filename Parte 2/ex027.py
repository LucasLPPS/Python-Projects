# existem várias bibliotecas para importar e tocar músicas, cabe ao
# desenvolvedor escolher a que ele prefere.
# o arquivo de som deve ser colado na mesma pasta onde estará o código solicitando que ele toque.
# para copiar, basta copiar o arquivo e colar no próprio pycharm.
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("som.mp3")
pygame.mixer.music.play(loops=0,start=0)
pygame.event.wait()
