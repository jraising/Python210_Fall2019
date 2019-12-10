#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 10:25:56 2019

@author: jraising
"""
from math import pi
class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    @property
    def area_circle(self):
         return (f'{(pi * self.radius * self.radius):.2f}')
     
    @area_circle.setter  # Only for practice. Not real world case
    def area_circle(self, area):
        self.radius = area/ (self.radius * pi)
        return self.radius
     
    @classmethod 
    def from_diameter(cls, diameter):
        cls.radius = diameter/2
        return cls.radius
    
    @property
    def diameter(self):
        return 2*self.radius
    
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2
    
    def __lt__(self,other):
        if (self.radius < other.radius):
            print("Other circle is bigger")
            return True 
        
    
    def __add__(self, other):
         try:
            return (self.radius + other.radius)
         except AttributeError:
            return (self.radius + other)
        
    def __radd__(self, other):
         return Circle.__add__(self, other)
    
    def __repr__(self):
        return (f'(radius of circle is {self.radius})')
    
    def __str__(self):
        return(f'{self.radius}')

#class Sphere(Circle):
#    def       

        
c1 = Circle(4)
c2 = Circle(5)
print (c1.area_circle())
print (Circle.area_circle(c1))
Circle.print_circle(c1)
Circle.compare_circles(c1, 3)
 x=Circle.diameter(4)

        