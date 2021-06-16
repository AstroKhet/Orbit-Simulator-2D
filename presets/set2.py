from classes.object import Object2D
from classes.vector import Vector2D

NAME = "Triple Star System"
TIME_DELTA = 1800
SPACE_SCALE = 5 * 10**6
BASE_SPACE_VECTOR = Vector2D(1.5 * 10**9, -2 * 10 ** 9)


object_list = [
    Object2D(
        name="Binary 0",
        mass=5.972 * 10 ** 24,
        radius=6.371 * 10 ** 6,
        scale=5,
        colour=(255, 255, 255),
        position=Vector2D(3 * 10 ** 8, 5 * 10 ** 8),
        velocity=Vector2D(0, 600)
    ),

    Object2D(
        name="Binary 1",
        mass=5.972 * 10 ** 24,
        radius=6.371 * 10 ** 6,
        scale=5,
        colour=(255, 255, 255),
        position=Vector2D(7 * 10 ** 8, 5 * 10 ** 8),
        velocity=Vector2D(0, -600)
    ),

    Object2D(
        name="Triplet",
        mass=5.972 * 10 ** 24,
        radius=6.371 * 10 ** 6,
        scale=5,
        colour=(255, 0, 0),
        position=Vector2D(18 * 10 ** 8, 18 * 10 ** 8),
        velocity=Vector2D(-450, 450)
    )
]