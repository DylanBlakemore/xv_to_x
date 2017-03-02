#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 12:36:49 2017

@author: Dylan Blakemore

A short script to read a dsv file of format (x y z vx vy vz) and
simplify the data to output only (x y z) position values
"""
import numpy as np

input_file = "mayaAttrib_0001.attr"
input_data = np.genfromtxt(input_file, dtype=None, delimiter='\t', usecols=(1,2,3))

output_file = "/home/user/Work/Blender/Tumbling Mill/input/mayaPos_0001.dsv"
np.savetxt(output_file,input_data,delimiter=',')
print(input_data.shape)
