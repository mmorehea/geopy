#                              _
#                             | |
#  __ _  ___  ___  _ __  _   _| |
# / _` |/ _ \/ _ \| '_ \| | | | |
#| (_| |  __/ (_) | |_) | |_| |_|
# \__, |\___|\___/| .__/ \__, (_)
#  __/ |          | |     __/ |
# |___/           |_|    |___/


import os
import sys
import code
import subprocess
import re
import glob

if len(sys.argv) < 1:
	print 'geopy!'
	print 'usage: python geopy.py [path/to/dist/set]'
	sys.exit(1)

infile = sys.argv[1]

listOfFiles = glob.glob(infile + '/*.ps')
print listOfFiles

fileToWrite = open(infile + 'ratios', 'w')
for each in listOfFiles:
	f = open(each, 'r')
	lines = f.readlines()
	f.close()
	for line in lines:
		if '@2' in line:
			l = line.split()
			print l[-1]
			fileToWrite.write(str(l[-1]) + '\n')
	

fileToWrite.close()

			

