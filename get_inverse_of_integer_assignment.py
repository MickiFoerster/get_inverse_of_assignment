#!/usr/bin/env python
import re
import sys
import os

####################    MAIN    ###############################
if len(sys.argv[1:])==0:
	print "Give generated ast files as paramter.";
	sys.exit(1);

for arg in sys.argv[1:]:
	if not os.path.isfile(arg): 
		print "%s is not a file." % arg;
		continue;
	# Read in AST data from file given as parameter.
	f = open(arg, 'r');
	s = '';
	for l in f.readlines():
		s+=l.replace('\n', '');
	f.close();
	ast=eval(s);
	basename , extension = os.path.splitext(arg);
