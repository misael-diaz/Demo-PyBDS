#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyBDS                                             May 05, 2024

source: main.py
author: @misael-diaz

Synopsis:
Implements a minimal Brownian Dynamics Simulator for spheres.

Copyright (c) 2024 Misael Díaz-Maldonado
Copyright (c) 2024 UCF-Research Group
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

References:
[0] R Johansson, Numerical Python: Scientific Computing and Data
    Science Applications with NumPy, SciPy, and Matplotlib, 2nd edition.
[1] MP Allen and DJ Tildesley, Computer Simulation of Liquids.
[2] S Kim and S Karrila, Microhydrodynamics.
"""

# imports a normally distributed pseudo-random number generator to conduct our simulation
from numpy.random import normal
# we need the squared root function to simulate Brownian motion
from numpy import sqrt

# initializes the position vector components of the sphere
x = 0
y = 0
z = 0

# initializes the Brownian force acting on the sphere
F_x = 0
F_y = 0
F_z = 0

# simulation start and end times
time_start = 0.0
time_end = 1.0
# simulation time-step (a base-two number because it has an exact binary representation)
dt = time_step = 2**-16

# determines the number of time steps needed to reach the end-time
num_steps = int((time_end - time_start) / time_step)

# defines the "mobility" of the sphere when subjected to Brownian forces
mob = sqrt(2 * dt)

step = 0
# simulates Brownian motion of the sphere
while (step != num_steps):

    F_x = normal()
    F_y = normal()
    F_z = normal()

    x += mob * F_x
    y += mob * F_y
    z += mob * F_z

    step += 1
