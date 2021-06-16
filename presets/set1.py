from classes.object import Object2D
from classes.vector import Vector2D

NAME = "Solar System"
TIME_DELTA = 43210
SPACE_SCALE = 12 * 10 ** 9
BASE_SPACE_VECTOR = Vector2D(0, 0)


object_list = [
    Object2D(
        name="Sun",
        mass=1.989 * 10**30,
        radius=6.957 * 10**8,
        scale=25,
        colour=(252, 186, 3),
        position=Vector2D(6 * 10**12, 6 * 10**12),
        velocity=Vector2D(0, 0)
    ),

    Object2D(
        name="Mecury",
        mass=3.285 * 10**23,
        radius=2.4397 * 10**6,
        scale=1000,
        colour=(180, 180, 180),
        position=Vector2D(6 * 10**12 + 57.9 * 10**9, 6 * 10**12),
        velocity=Vector2D(0, 47.36 * 10**3)
    ),

    Object2D(
        name="Venus",
        mass=4.867 * 10**24,
        radius=6.0518 * 10**6,
        scale=1000,
        colour=(187, 183, 171),
        position=Vector2D(6 * 10**12 - 107.48 * 10**9, 6 * 10**12),
        velocity=Vector2D(0, -35.02 * 10**3)
    ),

    Object2D(
        name="Earth",
        mass=5.9724 * 10**24,
        radius=6.356 * 10**6,
        scale=1000,
        colour=(11, 227, 195),
        position=Vector2D(6 * 10**12 + 151.96 * 10**9, 6 * 10**12),
        velocity=Vector2D(0, 29.78 * 10**3)
    ),

    Object2D(
        name="Mars",
        mass=64171 * 10**23,
        radius=3.3895 * 10**6,
        scale=1000,
        colour=(193, 68, 14),
        position=Vector2D(6 * 10**12 - 250.17 * 10**9, 6 * 10**12),
        velocity=Vector2D(0, -24.07 * 10**3)
    ),

    Object2D(
        name="Jupiter",
        mass=1.89819 * 10**27,
        radius=6.9911 * 10**7,
        scale=200,
        colour=(211, 156, 126),
        position=Vector2D(6 * 10**12 + 754.87 * 10**9, 6 * 10**12),
        velocity=Vector2D(0, 13.06 * 10**3)
    ),

    Object2D(
        name="Saturn",
        mass=5.6834 * 10**26,
        radius=5.4364 * 10**7,
        scale=200,
        colour=(197, 171, 110),
        position=Vector2D(6 * 10 ** 12 - 1.4872 * 10**12, 6 * 10 ** 12),
        velocity=Vector2D(0, -9.68 * 10**3)
    ),

    Object2D(
        name="Uranus",
        mass=8.6813 * 10**25,
        radius=2.4973 * 10**7,
        scale=600,
        colour=(187, 225, 228),
        position=Vector2D(6 * 10 ** 12 + 2.9541 * 10**12, 6 * 10 ** 12),
        velocity=Vector2D(0, 6.80 * 10**3)
    ),

    Object2D(
        name="Neptune",
        mass=1.02413 * 10**26,
        radius=2.4341 * 10**7,
        scale=600,
        colour=(62, 84, 232),
        position=Vector2D(6 * 10 ** 12 - 4.495 * 10**12, 6 * 10 ** 12),
        velocity=Vector2D(0, -5.43 * 10**3)
    ),

    Object2D(
        name="Pluto",
        mass=1.303 * 10**22,
        radius=1.188 * 10**6,
        scale=1000,
        colour=(150, 133, 112),
        position=Vector2D(6 * 10 ** 12 + 5.90538 * 10**12, 6 * 10 ** 12),
        velocity=Vector2D(0, 4.67 * 10**3)
    ),
]
