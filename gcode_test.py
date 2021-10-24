# https://github.com/MoonCactus/gcode_postprocessors/blob/master/wood/testing/wood_cylinder_source.gcode

from gcode import *

gcode.runTests([
"""
G20 X1 Y2 ; Initial Setup
M10 Z123.1 Y-10.2 ; Position it
; line comment
A1
""",
"""
; comment
; nog een
; en nog een


    

G1 A1.2123 *31 ; caas
"""
])
