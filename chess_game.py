import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))     # Vous définissez la taille de fenêtre de votre jeu
pygame.display.set_caption("Echecs")

board = pygame.Surface((480, 480))
board.fill((175, 141, 120))
for x in range(0, 8, 2):
    for y in range(0, 8, 2):
        pygame.draw.rect(board, (250, 240, 230), (x * 60, y * 60, 60, 60))
for x in range(1, 9, 2):
    for y in range(1, 9, 2):
        pygame.draw.rect(board, (250, 240, 230), (x * 60, y * 60, 60, 60))


while True:                           # C'est ce qu'on appelle une boucle de jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # L'utilisateur a cliqué sur le X de la fenêtre
            print("Bye bye")
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                print(chr(97 + (x // 60)), ((480 - y) // 60) + 1)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x, y = event.pos
                print(chr(97 + (x // 60)), ((480 - y) // 60) + 1)


    screen.fill((200, 200, 200))    # Vous définissez la couleur de fond ici
    screen.blit(board, board.get_rect())
    pygame.display.update()


sys.exit(0)