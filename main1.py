import math
import random

import pygame


def draw(screen: pygame.Surface):
   # font = pygame.font.Font('C://WINDOWS//Fonts//segoeuil.ttf', 36)
   # text = font.render('Hello!', True, (12, 34, 56))
   # text_x = w // 2 - text.get_width() // 2
   # text_y = h // 2 - text.get_height() // 2
   # screen.blit(text, (text_x, text_y))
  # rect = pygame.Rect(w // 2,h //2,70,30)
  # screen.fill((34,56,67), (w // 2,h //2,30,70))
 # for _ in range(10):
     # screen.fill((255, 56, 89), (random.random() * w, random.random() * h, 3, 3))
     #pygame.draw.rect(screen, (255, 56, 89), (0, 0, 80, 90))
     #pygame.draw.rect(screen, (255, 56, 89), (45, 67, 100, 50), 3)
     pygame.draw.circle(screen, (0, 0, 0), (w // 2.2, h // 5), 5)
     pygame.draw.circle(screen, (0, 0, 0), (w // 1.8, h // 5), 5)
     pygame.draw.circle(screen, (0, 0, 0), (w // 2, h // 2), 100, 3)
     pygame.draw.circle(screen, (0, 0, 0), (w // 2, h // 4), 65, 3)
     #pygame.draw.ellipse(screen, (222, 33, 56), (45, 67, 100, 50))
     pygame.draw.arc(screen, (0, 0, 0), (270, 90, 70, 100), math.pi, 0, 3)
     pygame.draw.polygon(screen, pygame.Color('orange'), [(300, 125), (280, 150), (320, 150)])
     #pygame.draw.line(screen, (0, 0, 0), (-100, 2000), (100, 200), 5)
     pygame.draw.aaline(screen, (0, 0, 0), (50, 180), (250, 270), 100)
     pygame.draw.aaline(screen, (0, 0, 0), (500, 180), (350, 270), 100)


if __name__ == '__main__':
    pygame.init()
    size = w, h = 600, 600
    screen = pygame.display.set_mode(size)
    color = pygame.Color(251, 255, 254)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2], hsv[3])
    screen.fill(color)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
