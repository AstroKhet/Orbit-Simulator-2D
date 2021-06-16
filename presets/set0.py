from classes.object import Object2D
from classes.vector import Vector2D

# Name of preset
NAME = "Earth & Moon"

# time interval used in calculations
TIME_DELTA = 10

# Each pixel represents SCALE meters
SPACE_SCALE = 1 * 10**6

# Initial coordinate of bottom-left (0, 0) pixel
BASE_SPACE_VECTOR = Vector2D(0, 0)


object_list = [
    Object2D(
        name="Earth",
        mass=5.972 * 10 ** 24,
        radius=6.371 * 10 ** 6,
        scale=3,
        colour=(68, 167, 196),
        position=Vector2D(5 * 10**8, 5 * 10**8),
        velocity=Vector2D(0, 0)
    ),

    Object2D(
        name="Moon",
        mass=7.342 * 10 ** 22,
        radius=1.737 * 10 ** 6,
        scale=3,
        colour=(180, 180, 180),
        position=Vector2D(8.992 * 10 ** 8, 5 * 10 ** 8),
        velocity=Vector2D(0, 1022)
    ),
]
