import pygame


pygame.init()

window_size = (900, 900)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('3x3 Grid')



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the current state
    screen.fill((155, 200, 255))  # Fill the screen with white

    # Draw grid lines
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (900, 300), 10)
    pygame.draw.line(screen, (0, 0, 0), (0, 600), (900, 600), 10)
    pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 900), 10)
    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 900), 10)
    #pygame.draw.line(screen, (0, 0, 0), (50, 50), (255,255), 20)
    #pygame.draw.line(screen, (0, 0, 0), (255, 50), (50,255), 20)
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos
        print(f"Mouse clicked at ({mouse_x}, {mouse_y})" )
        if mouse_x <= 300 and mouse_y <= 300:
            pygame.draw.circle(screen, (0, 0, 0), (150, 150), 120, width=20, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    # Refresh the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()