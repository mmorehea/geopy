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

totalDists = open('totalDists_' + folderName + '.txt', 'w')

for ii, each in enumerate(listOfDists):
	with open('temp.txt', 'w') as w:
		for line in each:
			w.write(line)
	s = '(cat ../prelude.ps; cat ./temp.txt | ../efst | ../bb) > ./' + folderName + '/' + str(ii) + '.ps'
	subprocess.call(s, shell=True)
	with open('./' + folderName + '/' + str(ii) + '.ps', 'r') as r:
		lines = r.readlines()
	for line in lines:
		if '(Euclidean SMT:' in line:
			totalDists.write(line)

totalDists.close()



code.interact(local=locals())
