#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:43:11 2021

@author: maryamali
"""

                        #Planning for drunks
                            #Maryam Ali
                  
# This is the drunk framework, this module helps to establish a framework 
#           for this model by creating a drunks class. 
# This module will also introduce and build new functions (walkhome,record)
# This module will work alongside the 'model.py' to build a successful model
#                           Thank you 


import random

#Set a random seed to obtain the same number , assign as 1 
random.seed(1)


# 
class drunks ():
    
    def __init__ (self, i, Town, drunks, house, pub, density):
        self.Town = Town
        self.drunks = drunks
        self.house = house
        self.i  = i
        self.x = 148
        self.y = 158
        self.pub = pub
        self.density = density
        
        
#Make a move() method with the Drunks Class
    
    def walkhome(self):
         if random.random() < 0.5:
             self.y = (self.y + 1) % 300
         else:
             self.y = (self.y - 1) % 300

         if random.random() < 0.5:
             self.x = ( self.x + 1) % 300
         else:
              self.x = (self.x - 1) % 300

    def record(self):
        
        self.density[self.y][self.x] += 1 
              
             

  # Information on the drunks, and their location 
# Use the _str_ function
        
    # def __str__(self):
    #     return "i=" + str(self.i) \
    #         + ", x=" + str(self.x) \
    #         + ", y=" + str(self.y) 

    
    # def walkhome(self):
    #     if random.random() < 0.5:
    #         self.y = (self.y + 1) % len(self.Town)
    #     else:
    #         self.y = (self.y - 1) % len(self.Town )

    #     if random.random() < 0.5:
    #           self.x = ( self.x + 1) % len(self.Town [0])
    #     else:
    #           self.x = (self.x - 1) % len(self.Town[0])
              
              
   



