#!/usr/bin/python3

import sys
import operator
import argparse

def add_lines(tab):
	chain = ""
	for i in tab:
		chain += i[:-1]

	return chain
	
def rm_spaces(text):
	text2 = ""
	for i in text:
		if i != " ":
			text2 += i
	return text2

def create_chain(line, n, j):
	chain = ""
	
	for k in range(n):
		chain += line[k*j]
	return chain 

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of the file to analize")
parser.add_argument("n", help="count groups of n characters", type=int, choices=[1, 2, 3])
parser.add_argument("-j", "--jump", help="count every j character", type=int)
parser.add_argument("-k", "--keep", help="print only the first k results", type=int)
parser.add_argument("-s", "--start", help="start at a defined place", type=int)
parser.add_argument("-e", "--end", help="stop at a defined place", type=int)
parser.add_argument("--short", help="disable bars", action="store_true")
args = parser.parse_args()
	
if args.jump == None:
	j = 1
else:
	j = args.jump
	
if args.start == None:
	start = 0
else:
	start = args.start - 1


f = open(args.filename, "r")
dictionnary = {}

text = add_lines(f.readlines())
text = rm_spaces(text)

if args.end == None:
	stop = len(text) - args.n +1
else:
	stop = args.end

for i in range(start, stop, j):
	chain = create_chain(text[i:], args.n, j)
			
	if chain in dictionnary:
		dictionnary[chain] += 1
	else:
		dictionnary[chain] = 1
					
sorted_dict = sorted(dictionnary.items(), key=operator.itemgetter(1), reverse=True)
		
if args.keep == None:
	m = len(sorted_dict)
else:
	m = args.keep

for j in range(m):
	if args.short:
		l = ""
	else:
		l = int(round(float(sorted_dict[j][1])/sorted_dict[0][1]*100))*"|"
	print(sorted_dict[j][0]+" : "+str(sorted_dict[j][1])+(7-len(str(sorted_dict[j][1])))*" "+l)
