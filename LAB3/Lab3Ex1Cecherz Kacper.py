import pygame
import math

pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab3Ex1 Cecherz Kacper")

YELLOW = (252, 248, 53)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
GRAY = (156, 154, 154)

center_x = WIDTH // 2
center_y = HEIGHT // 2
initial_radius = 150
sides = 11
radius = initial_radius
angle_offset = 0
scale_x = 1
shear_x = 0
mirrored = False

def draw_polygon():
    screen.fill(YELLOW)
    points = []
    
    for i in range(sides + 1):
        angle = (i * 2 * math.pi) / sides + angle_offset - math.pi / 2
        x = center_x + (radius * scale_x) * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        x += shear_x * (y - center_y) / radius
        
        if mirrored:
            x = 2 * center_x - x
            
        points.append((x, y))
    
    pygame.draw.polygon(screen, PURPLE, points)
    pygame.draw.polygon(screen, BLACK, points, 2)

def reset_polygon():
    global radius, angle_offset, scale_x, shear_x, mirrored, center_x, center_y
    radius = initial_radius
    angle_offset = 0
    scale_x = 1
    shear_x = 0
    mirrored = False
    center_y = HEIGHT // 2
    center_x = WIDTH // 2

draw_polygon()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                radius /= 2
            elif event.key == pygame.K_2:
                angle_offset += math.pi / 4
            elif event.key == pygame.K_3:
                angle_offset += math.pi
                scale_x /= 2
            elif event.key == pygame.K_4:
                shear_x += 20
            elif event.key == pygame.K_5:
                center_y = radius
                scale_x *= 1.5
            elif event.key == pygame.K_6:
                angle_offset += math.pi / 2
                shear_x += 20
            elif event.key == pygame.K_7:
                mirrored = not mirrored
                scale_x /= 2
            elif event.key == pygame.K_8:
                center_y = 3 * radius
                angle_offset += math.pi / 4
            elif event.key == pygame.K_9:
                angle_offset += math.pi
                center_x = 3 * radius
            elif event.key == pygame.K_r:
                reset_polygon()
            draw_polygon()

    pygame.display.flip()

pygame.quit()
