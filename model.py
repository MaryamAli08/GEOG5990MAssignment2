#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:42:40 2021

@author: maryamali
"""

                       #Planning for drunks
                            #Maryam Ali
                  

# This program is aims to exempify 25 drunks jounrey home from the pub.
#      This will implemented utilising a data file (town plan), which
#            consist of the town , the pub and houses. the program
#            will highlight each step in assisting the drunks home. 
#              for the Full information on project , see Github
#                           Thank you 



import matplotlib.pyplot # For Data visualisation (producing figures, plotting)
import Drunkframework # This Module consists of the drunk class & this will be
                      # examined longside the model.py to produce the the program
import csv               # This functions enables to import text files
import time              # function will help to examine the execution time



# 1. Create the Environment for the drunks 
# this will be implemented by installing the drunk plan.txt using the import csv function 
# Pull in data file 

#Install drunk plan (Town Plan) 
# Town = Environment

Town = []
f = open('drunk.plan', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
     # print(value) 
        rowlist.append(value)
    Town.append(rowlist) 
f.close()

#Examine the density. Create a function to open
density = []
a = open(r'drunk.plan') 
reader = csv.reader(a, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
    # print(value) 
        rowlist.append(value)
    density.append(rowlist) 
a.close()

# To examine whether town plan works (print)
print (Town)

# Produce a data visualisation of the town plan
matplotlib.pyplot.imshow(Town)
matplotlib.pyplot.show ()

'''
# Invesigate the length , rows , cols of the town plan
# rows = len(Town)
# cols = len(Town[0])
# print("rows", rows)
# print("cols", cols)

# for rows in range(rows):
#     if (len(Town[rows]) != cols):
#         print("home")
'''


# Create variables 
# Also, empty variables list will be produced using the bulit in function and 
# Square Brackets []

num_of_drunks = 25
num_of_iterations = 10000000
drunks = []
pub = []

# 2. Identify and illustrate the pub points and home points


# Make the Drunks.
for i in range(num_of_drunks):
     house = ( i + 1 )*10
    # print ("house", house)
     drunks.append(Drunkframework.drunks(i, Town, drunks, house, pub, density))

 
# Locate the Pub , the starting location 
# Use the enumerate to 
 
#the pub is denoted by 1  
  
for i, row in enumerate(Town):
    for j, num in enumerate(row):
          if num == 1:
            pub = j, i 
           
            
# for i in range(num_of_drunks):
#     house = ( i + 1 )*10
#     # print ("house", house)

#examine Time
start = time.time()
end = time.time()

# 3. Move the Drunks and record their movements on their way home
# 4. Exemplify the density of drunks passing though each point
# Make the agents move by creating a loop 
# Assign the drunks to their houses
# for j in range(num_of_iterations):
     
for i in range (num_of_drunks):
    drunk = drunks[i]
    start = time.time()
    for j in range(num_of_iterations):
        if Town [drunk.y][drunk.x] != drunk.house: 
            #Make the drunk walk home
            drunks[i].walkhome()
            #Examine whether walkhome is working (print)
            # print(drunks[i].walkhome)
            #Examine the density ...
            drunks[i].record()
            print(f"{drunk.house} homesweethome!")
    end = time.time() 
    print (time.time())
# print statement ' homesweethome' to show when the drunks are home.

   
    
#Create a visualisation of the plots (drunks) (density)
matplotlib.pyplot.xlim(0,300)
matplotlib.pyplot.ylim(0,300)
matplotlib.pyplot.imshow(density)
for i in range(num_of_drunks):
      matplotlib.pyplot.scatter(drunks[i].x, drunks[i].y)
      # matplotlib.pyplot.scatter(pub, color = 'red')
matplotlib.pyplot.show()
 

# 5. Save the density map to a file as text
with open('density.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in density:
        csvwriter.writerow(row)


# This drunkmodel is complete









#Animation 
# fig = matplotlib.pyplot.figure(figsize=(15, 15))
# ax = fig.add_axes([0, 0, 1, 1])
# animation = matplotlib.animation


   
# print (drunks)
# for i in range (num_of_drunks):
#     print(drunks[i])


