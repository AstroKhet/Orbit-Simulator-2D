from classes.vector import Vector2D
from constants import WIN_WIDTH, WIN_HEIGHT
from functions import update_objects, sim_time
import pygame

# choose name of preset by changing the line below witth presets.<preset_name>
from presets.set0 import NAME, TIME_DELTA, SPACE_SCALE, BASE_SPACE_VECTOR, object_list


pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont('Courier', 12)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(NAME)


time_elapsed = 0

# For moving simulation space
mouse = None
SPACE_VECTOR = Vector2D(*BASE_SPACE_VECTOR.Args)

clock = pygame.time.Clock()
# Simulation :)
running = True
while running:
    clock.tick(240)
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        # x-button
        if event.type == pygame.QUIT:
            running = False
            continue

        # Zooming in and out
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            delta_space = (0.05 * SPACE_SCALE) * Vector2D(pos[0], -pos[1])

            if event.button == 4:
                SPACE_SCALE *= 0.95
                SPACE_VECTOR -= delta_space

            if event.button == 5:
                SPACE_SCALE *= 1.0526
                SPACE_VECTOR += delta_space

    # Moving simulation space
    if pygame.mouse.get_pressed(3)[0]:
        pos = pygame.mouse.get_pos()
        moving = True
        if mouse is None:
            mouse = pos
        else:
            SPACE_CHANGE = SPACE_SCALE * (Vector2D(*pos) - Vector2D(*mouse))
            SPACE_VECTOR = BASE_SPACE_VECTOR + SPACE_CHANGE

    else:
        BASE_SPACE_VECTOR = Vector2D(*SPACE_VECTOR.Args)
        mouse = None

    # Displaying objects
    for obj in object_list:
        obj.initialize(SPACE_SCALE, SPACE_VECTOR)
        obj.draw(window)
        if obj.label:
            label_x, label_y = obj.display_pos.Args
            label = FONT.render(obj.name, False, obj.colour)
            label_rect = label.get_rect(center=(label_x, label_y+obj.display_radius+10))
            window.blit(label, label_rect)

    object_list = update_objects(object_list, TIME_DELTA)

    # Time elapsed since beginning
    time_elapsed += TIME_DELTA
    time_elapsed_text = FONT.render(sim_time(time_elapsed), False, (255, 255, 255))

    window.blit(time_elapsed_text, (10, 960))

    # Displaying map scales
    map_scale = FONT.render(f"{int(SPACE_SCALE/10):,} KM", False, (255, 255, 255))
    window.blit(map_scale, (120, 925))

    pygame.draw.line(window, (255, 255, 255), (10, 925), (10, 935))
    pygame.draw.line(window, (255, 255, 255), (110, 925), (110, 935))
    pygame.draw.line(window, (255, 255, 255), (10, 930), (110, 930))

    pygame.display.update()
