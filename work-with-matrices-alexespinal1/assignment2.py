#-------------------------------------
#Alex Espinal programming assignment 2
#-------------------------------------
# import numpy
import numpy as nump

#create the array list and filled it with numbers
b = nump.array([[1,2,3,4],[2,4,6,8],[3,6,9,12],[10,20,30,40],[5,10,15,20]])

#prints out the array list
print(b)

#using your hint by uing a loop

for column in b:
    print(column)

#prints out columns
print (b[:,0])
print (b[:,1])
print (b[:,2])
print (b[:,3])
