import pyfits
import numpy

CUBES = range(1, 58, 1)
cubes = map(str, CUBES)

direction = range(1868, 2135, 1)
average_list = []
for k in range(len(cubes)):
  cubeimage = pyfits.open('131048_cube_30obs_'+cubes[k]+'.fits')
  cubedata = cubeimage[0].data
  cubedata2 = cubedata[0,0]
  list_2degrees = []
  for i in range(len(direction)):
    for j in range(len(direction)):
       number1 = cubedata2[i,j]
       print number1
       list_2degrees.append(number1)
  mean1 = numpy.mean(list_2degrees)
  average_list.append(mean1)
with open('30obs_cube_2deg_avg_cube.txt','w') as file:
     for item in average_list:
        print>>file, item
