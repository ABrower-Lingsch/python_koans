#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if a == b == c:
        return 'equilateral'
        # all equal sides make an equalateral triangle
    elif a == b or b == c or c == a:
        return 'isosceles'
        # two equal sides and one non-equal side makes an isosceles
    return 'scalene'
    # anthing else would be scalene
    # source: basic geometry...

# Error class used in part 2.  No need to change this code.


class TriangleError(Exception):
    pass
