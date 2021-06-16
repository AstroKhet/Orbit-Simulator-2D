from math import sin, cos, atan2
from classes.vector import Vector2D
from constants import G
from copy import deepcopy


def update_objects(objects_list, TIME_DELTA):
    new_obj_list = []

    for i in range(len(objects_list)):
        obj_i = deepcopy(objects_list[i])
        acc_i = Vector2D(0, 0)

        for j in range(len(objects_list)):
            # obj_j refers to all objects that isnt obj_i
            if i == j:
                continue

            # Getting position values
            obj_j = deepcopy(objects_list[j])
            obj_i_pos = obj_i.Position
            obj_j_pos = obj_j.Position

            # Calculating accelaration using Newton's law of gravity
            dis_i_j = obj_j_pos - obj_i_pos
            acc_i_j_mag = (G * obj_j.mass) / (dis_i_j.Magnitude**2)
            acc_theta = atan2(dis_i_j.y, dis_i_j.x)

            # Calculating & adding acceleration vector in 2D space to total acceleration of obj_i
            acc_i_j = Vector2D(acc_i_j_mag*cos(acc_theta), acc_i_j_mag*sin(acc_theta))
            acc_i += acc_i_j

        # Kinematics
        obj_i.Velocity += TIME_DELTA * acc_i
        obj_i.Position += TIME_DELTA * obj_i.Velocity

        new_obj_list.append(obj_i)

    return new_obj_list


def sim_time(seconds):
    years, seconds = divmod(seconds, 31536000)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"Time Elapsed: {years:,} Years {days:<3} Days {hours:<2} Hours {minutes:<2} Minutes {seconds:<2} Seconds"
