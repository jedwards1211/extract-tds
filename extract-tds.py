#!/usr/bin/env python

import csv
import argparse

parser = argparse.ArgumentParser(description='Reads water quality data and outputs total dissolved solids rows as CSV')
parser.add_argument('inputfile', metavar='input file', nargs='+', help='the input file(s)')
parser.add_argument('-o', metavar='output file', help='the output file')

args = parser.parse_args()

with open(args.o, 'wb') as outfile:
	outputLineNumber = 0
	csvwriter = csv.writer(outfile)
	for inputfile in args.inputfile:
		with open(inputfile) as f:
			lineNumber = 0
			columnIndices = {}
			for line in f:
				columns = line.rstrip().split('|')
				if lineNumber == 0:
					for i in range(len(columns)):
						columnIndices[columns[i]] = i
					if outputLineNumber == 0:
						csvwriter.writerow(columns)
						outputLineNumber = outputLineNumber + 1
				else:
					if columns[columnIndices['ParameterCode']] == '70301':
						csvwriter.writerow(columns)
						outputLineNumber = outputLineNumber + 1
				lineNumber = lineNumber + 1