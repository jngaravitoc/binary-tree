import numpy as np
import sys
import pandas


data = pandas.read_csv("Ejem_newick.csv")

dim = np.shape(data)
lev = dim[1]-1
sp = dim[0]

print "Your tree have", sp, "species" 
print "your tree have", lev, "levels."

#print type(data)

#for i in range(1,lev):
d = np.array(data)
l=[]
indexes = []
n_groups = 0
#indexes = np.zeros()
for i in range(1, lev):
	index = np.where(d[:,i]==1)
	indexes.append(len(index[0]))
	if i>1:
		if (len(index[0])>indexes[i-1]):
			print "hola"
	#f (len(index)>0):	
	#l.append("(")
print indexes
