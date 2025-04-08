import pygame
import sys

pygame.init()

screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Centered Blue Shapes')

blue = (0, 0, 255)
background_color = (255, 255, 255)

screen.fill(background_color)

vertical_offset_triangle = 200
vertical_offset_rectangle = vertical_offset_triangle + 50
vertical_offset_second_triangle = vertical_offset_rectangle + 50

triangle1_points = [(250, vertical_offset_triangle), (350, vertical_offset_triangle), (300, vertical_offset_triangle + 50)]

rectangle_y = vertical_offset_rectangle
rectangle = (250, rectangle_y, 100, 50)

triangle2_points = [(250, vertical_offset_second_triangle + 50), (350, vertical_offset_second_triangle + 50), (300, vertical_offset_second_triangle)]

pygame.draw.polygon(screen, blue, triangle1_points)
pygame.draw.rect(screen, blue, rectangle)
pygame.draw.polygon(screen, blue, triangle2_points)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
