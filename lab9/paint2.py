import pygame

mode = 'blue'

def main():
    pygame.init()

    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    #setup fonts
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)

    #setup texts
    text1 = font_small.render("RED", True, (255, 0, 0))
    text2 = font_small.render("GREEN", True, (0, 255, 0))
    text3 = font_small.render("BLUE", True, (0, 0, 255))
    
    FPS = 60
    FramePerSec = pygame.time.Clock()

    radius = 15
    global mode
    points = []
    rectangles = []
    circles = []
    rightTriangles = []
    equilateralTriangles = []
    rombs = []
    erasing = False

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_t:
                    rectangles.append((pygame.mouse.get_pos()))
                elif event.key == pygame.K_y:
                    circles.append((pygame.mouse.get_pos()))
                elif event.key == pygame.K_u:
                    rightTriangles.append((pygame.mouse.get_pos()))
                elif event.key == pygame.K_i:
                    equilateralTriangles.append((pygame.mouse.get_pos()))
                elif event.key == pygame.K_o:
                    rombs.append((pygame.mouse.get_pos()))
                elif event.key == pygame.K_e:
                    erasing = not erasing  

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    radius = min(200, radius + 5)
                elif event.button == 3:  
                    radius = max(5, radius - 5)

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if erasing:
                    points = [p for p in points if not is_colliding(p, position, radius)]
                    rectangles = [r for r in rectangles if not is_colliding(r, position, radius)]
                    circles = [c for c in circles if not is_colliding(c, position, radius)]
                    rightTriangles = [c for c in circles if not is_colliding(c, position, radius)]
                    equilateralTriangles = [c for c in circles if not is_colliding(c, position, radius)]
                    rombs = [c for c in circles if not is_colliding(c, position, radius)]
                else:
                    points.append(position)
                    points = points[-256:]






        screen.fill(BLACK)
        drawSelection(screen, WHITE, text1, text2, text3)

        for i in range(len(points) - 1):
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)

        for pos in rectangles:
            drawRectangle(screen, mode, pos)

        for pos in circles:
            drawCircle(screen, mode, pos, radius)

        for pos in rightTriangles:
            drawRightTriangle(screen, mode, pos)
        
        for pos in equilateralTriangles:
            drawEquilateralTriangle(screen, mode, pos)
        
        for pos in rombs:
            drawRhombus(screen, mode, pos)

        pygame.display.flip()
        FramePerSec.tick(FPS)

def drawSelection(screen, border_color, text1, text2, text3):
    global mode
    screen.blit(text1, (80, 0))
    screen.blit(text2, (280, 0))
    screen.blit(text3, (480, 0))
    pygame.draw.rect(screen, border_color, (0, 0, 200, 30), 2)
    pygame.draw.rect(screen, border_color, (200, 0, 200, 30), 2)
    pygame.draw.rect(screen, border_color, (400, 0, 200, 30), 2)

    if(pygame.mouse.get_pos()[1] > 0 and pygame.mouse.get_pos()[1] < 30):
        if(pygame.mouse.get_pos()[0] > 0 and pygame.mouse.get_pos()[0] < 200):
            mode = 'red'
        elif(pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 400):
            mode = 'green'
        elif(pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 600):
            mode = 'blue'

def is_colliding(pos1, pos2, radius):
    return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 < radius ** 2

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, color, position):
    color_map = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}
    pygame.draw.rect(screen, color_map[color], (position[0], position[1], 50, 50), 5)

def drawCircle(screen, color, position, radius):
    color_map = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}
    pygame.draw.circle(screen, color_map[color], position, radius, 5)

def drawRightTriangle(screen, color, position):
    color_map = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}
    points = [position, (position[0] + 50, position[1]), (position[0], position[1] + 50)]
    pygame.draw.polygon(screen, color_map[color], points, 5)

def drawEquilateralTriangle(screen, color, position):
    color_map = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}
    points = [position, (position[0] - 25, position[1] + 50), (position[0] + 25, position[1] + 50)]
    pygame.draw.polygon(screen, color_map[color], points, 5)

def drawRhombus(screen, color, position):
    color_map = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}
    points = [(position[0], position[1] - 30), (position[0] - 30, position[1]), 
              (position[0], position[1] + 30), (position[0] + 30, position[1])]
    pygame.draw.polygon(screen, color_map[color], points, 5)

main()