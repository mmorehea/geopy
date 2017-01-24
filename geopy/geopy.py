import os
import sys
import code
import subprocess



if len(sys.argv) < 2:
	print 'geopy!'
	print 'usage: python geopy.py [path/to/dist/set] [folder/to/make]'
	sys.exit(1)

infile = sys.argv[1]
folderName = sys.argv[2]

if not os.path.isdir(folderName):
	os.mkdir(folderName)

with open(infile, 'r') as f:
	lines = f.readlines()



listOfDists = []
dists = []
for each in lines:
	if each.strip() == '100':
		if dists:
			listOfDists.append(dists)
			dists = []
	else:
		dists.append(each)

listOfDists.append(dists)


code.interact(local=locals())
