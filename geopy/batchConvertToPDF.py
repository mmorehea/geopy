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

for each in listOfFiles:
	s = "ps2pdf " + each + " " + each[:-2] + 'pdf'
	print s
	subprocess.call(s, shell=True)

