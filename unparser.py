#!/usr/bin/python
import os
import sys
import re

eq_root = -1;
inverse_eq  = {};


def find_ast_root(of, ast):
	if of is None: return;
	if ast is None: return;
	# Look for first node
	for key in ast:
		if ast[key][0]=='GETS': 
			global eq_root;
			eq_root=key;
			break;

def unparse_output(of, ast, node_id):
	node = ast[node_id];
	if node[0]=='FOR':
		print '';

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
	find_ast_root(f, ast);
	ast_id=eq_root+1;
	# do something
	# ...
	f = open('%s.output' % basename, 'w');
	unparse_output(f, ast, eq_root);
	f.close();
	inverse_eq_dot_file = "%s.inverse_eq.dot" % basename;
	inverse_eq_pdf_file = "%s.inverse_eq.pdf" % basename;
	linearized_output_file = "%s.inverse_eq" % basename;
	f = open(inverse_eq_dot_file, 'w');
	f.write('digraph {\n');
	for key in inverse_eq:
		print "asf";
		node = inverse_eq[key];
		if node[1]=='':
			f.write('%d[label="%d: %s"]\n' % (key, key, node[0]));
		else:
			f.write('%d[label="%d: %s(%s)"]\n' % (key, key, node[0], node[1]));
		for successor in node[2]:
			f.write('%d -> %d\n' % (key,successor));
	f.write('}\n');
	f.close();
	if os.stat(inverse_eq_dot_file).st_size/1024 < 1024:
		cmd = "dot -Tpdf %s > %s" % (inverse_eq_dot_file, inverse_eq_pdf_file);
		os.system(cmd);

sys.exit(0);
