# 2D Multi Object Simulator
 
A simple Multi-Object gravitational motion simulator made while learning about linear algebra & orbital mechanics

## How it works

Create a file in the folder `presets/` with the following variables:
  * **NAME**              : Name of simulation
  * **TIME_DELTA**        : Time passed per iteration
  * **SPACE_SCALE**       : Meters per pixel
  * **BASE_SPACE_VECTOR** : Position of bottom-left coordinate of window (in real scale)
  * **object_list**       : List of objects
 
This simulation uses [Newton's law of universal gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation) to calculate the acceleration of each object, then uses kinematics to simulate their corresponding velocity & displacement.

## Demo
Triple Star System
![Alt Text](https://github.com/AstroKhet/2D-Multi-Object-Simulator/blob/main/.demo/Triple%20Star%20System.gif)

Solar System
![Alt Text](https://github.com/AstroKhet/2D-Multi-Object-Simulator/blob/main/.demo/Solar%20System.gif)

## What can be improved/implemented
* Collision between objects
* Displaying vectors for each object's velocity and gravitational acceleration
* Displaying an orbit path
* Ability to add & drag objects using mouse button 
* Optimization in general
