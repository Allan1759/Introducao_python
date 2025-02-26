import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill('#bafc8b')

pygame.display.set_caption('FistGame')
velocidade = 15
person_color = ('#77a6f2')
l = 10
a = 10
x = 80
y = 80


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    screen.fill('#bafc8b')
        
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_s]:
        y+= velocidade
    if teclas[pygame.K_w]:
        y-= velocidade
    if teclas[pygame.K_a]:
        x-= velocidade
    if teclas[pygame.K_d]:
        x+= velocidade  

    pygame.draw.rect(screen,person_color,(x,y,l,a))
    pygame.display.flip()
    pygame.time.Clock().tick(30)
    