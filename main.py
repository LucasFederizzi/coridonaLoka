import os, pygame
pygame.init()

clock = pygame.time.Clock()
tamanhoTela = (1000,592)
screen = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("corridaMaluka_MK1")


bg = pygame.image.load("assets/fundo.png")
carro1 = pygame.image.load("assets/carro1.png")

branco = (255,255,255)
preto = (0,0,0,)


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    screen.fill(branco)
    screen.blit(bg, (0,0))
    pygame.display.update()



