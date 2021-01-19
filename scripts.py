import numpy as np


def next_point(num_cycles=12,start_points=[0.1,.1],i=1,points=[]):
  cc = np.array([[1,1],[-1,1],[-1,-1],[1,-1]])
  if len(points) == 0:
    points = cc
  if num_cycles == 0:
    return(points[8:])

  #Start points
  new_points = (np.array([start_points]) * cc) * i
  
  #New starting place for next iteration.
  new_start = new_points[-1]
  
  #Add new points to previous ones
  points = np.concatenate((points,new_points))
  #print(points)
  
  #Iteratively drop each cycle until zero.
  num_cycles -= 1
  
  #Iteratively add 1 for later caluclations
  i += .1 # add 1 
  return(next_point(num_cycles,new_start,i,points=points))
