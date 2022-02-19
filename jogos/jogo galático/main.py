import pygame
import random
from random import randint

def main():
    x = 240
    y = 470
    velocidade = 10
    pontos = 0
    pos_y_meteoro = -200
    pos_x_meteoro = x
    pos_y_meteoro2 = -200
    pos_x_meteoro2 = random.randint(0, 300)
    pos_y_meteoro3 = -200
    pos_x_meteoro3 = random.randint(300, 500)
    pos_x_o2 = random.randint(100, 500)
    pos_y_o2 = random.randint(200, 550)

    pygame.init()

    fundo = pygame.image.load('fundo.jpg')
    astronauta = pygame.image.load('astronauta.png')
    asteroide = pygame.image.load('meteoro.png')
    asteroide2 = pygame.image.load('meteoro2.png')
    asteroide3 = pygame.image.load('meteoro3.png')
    gas_o2 = pygame.image.load('gas_oxigênio.png')
    branco = (255, 255, 255)
    game_over = pygame.image.load('game_over.jpg')

    popup = pygame.display.set_mode((600, 600))
    nome_do_jogo = pygame.display.set_caption('Jogo galático')
    fonte = pygame.font.SysFont('notosanscondensed', 30)
    texto = fonte.render('Pontos: ', True, (255, 255, 255), (0, 0, 0))
    pos_texto = texto.get_rect()
    pos_texto.center = (65, 50)

    mostrar_popup = True
    while mostrar_popup is True:
        delay = pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mostrar_popup = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            if y >= 0:
                y -= velocidade * 3
        if teclas[pygame.K_s]:
            if y <= 500:
                y += velocidade * 3
        if teclas[pygame.K_a]:
            if x >= 0:
                x -= velocidade * 3
        if teclas[pygame.K_d]:
            if x <= 500:
                x += velocidade * 3

        preencher = popup.blit(fundo, (0, 0))
        oxigenio = popup.blit(gas_o2, (pos_x_o2, pos_y_o2))
        boneco = popup.blit(astronauta, (x, y))
        cronometragem = popup.blit(texto, pos_texto)

        meteoro = popup.blit(asteroide, (pos_x_meteoro, pos_y_meteoro))
        meteoro2 = popup.blit(asteroide2, (pos_x_meteoro2, pos_y_meteoro2))
        meteoro3 = popup.blit(asteroide3, (pos_x_meteoro3, pos_y_meteoro3))

        pos_y_meteoro += velocidade*2
        pos_y_meteoro2 += velocidade*3
        pos_y_meteoro3 += velocidade*4

        #para resetar a posição Y e X dos meteoros
        if pos_y_meteoro == 800:
            pos_y_meteoro = -200
        #por que 1000???
        if pos_y_meteoro2 == 1000:
            pos_y_meteoro2 = -200
            pos_x_meteoro2 = random.randint(0, 300)
        if pos_y_meteoro3 == 800:
            pos_y_meteoro3 = -200
            pos_x_meteoro3 = random.randint(300, 500)

        #pegar oxigênio para marcar pontos
        diferenca_x_o2 = abs(x - pos_x_o2)
        diferenca_y_o2 = abs(y - pos_y_o2)
        if (diferenca_x_o2 > 0 and diferenca_x_o2 < 45):
            if (diferenca_y_o2 > 0 and diferenca_y_o2 < 45):
                pos_x_o2 = random.randint(100, 500)
                pos_y_o2 = random.randint(200, 550)
                pontos += 1

        diferenca_x_meteoro1 = abs(x - pos_x_meteoro)
        diferenca_y_meteoro1 = abs(y - pos_y_meteoro)
        if (diferenca_x_meteoro1 > 0 and diferenca_x_meteoro1 < 50):
            if (diferenca_y_meteoro1 > 0 and diferenca_y_meteoro1 < 50):
                preencher = popup.blit(game_over, (0, 0))
                mostrar_popup = False

        diferenca_x_meteoro2 = abs(x - pos_x_meteoro2)
        diferenca_y_meteoro2 = abs(y - pos_y_meteoro2)
        if (diferenca_x_meteoro2 > 0 and diferenca_x_meteoro2 < 50):
            if (diferenca_y_meteoro2 > 0 and diferenca_y_meteoro2 < 50):
                preencher = popup.blit(game_over, (0, 0))
                mostrar_popup = False

        diferenca_x_meteoro3 = abs(x - pos_x_meteoro3)
        diferenca_y_meteoro3 = abs(y - pos_y_meteoro3)
        if (diferenca_x_meteoro3 > 0 and diferenca_x_meteoro3 < 50):
            if (diferenca_y_meteoro3 > 0 and diferenca_y_meteoro3 < 50):
                preencher = popup.blit(game_over, (0, 0))
                mostrar_popup = False

        texto = fonte.render('Pontos: ' + str(pontos), True, (255, 255, 255), (0, 0, 0))
        pygame.display.update()
    pygame.time.delay(1000)
    pygame.quit()
main()