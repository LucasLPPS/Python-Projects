# existem várias bibliotecas para importar e tocar músicas, cabe ao
# desenvolvedor escolher a que ele prefere.
# o arquivo de som deve ser colado na mesma pasta onde estará o código solicitando que ele toque.
# para copiar, basta copiar o arquivo e colar no próprio pycharm.
import pygame # não consegui instalar o módulo pygame
pygame.init()
pygame.mixer.music.load("nome do arquivo.mp3")
pygame.mixer.music.play()
pygame.event.wait()
#thelukelp15@penguin:~$ cd PycharmProjects/
#thelukelp15@penguin:~/PycharmProjects$ ls
#pythonProject
#thelukelp15@penguin:~/PycharmProjects$ cd pythonProject/
#thelukelp15@penguin:~/PycharmProjects/pythonProject$ ls
#'Parte 1'  'Parte 2'   venv
#thelukelp15@penguin:~/PycharmProjects/pythonProject$ source venv/bin/activate
#deactivate
