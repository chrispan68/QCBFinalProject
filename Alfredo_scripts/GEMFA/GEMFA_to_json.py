#! /usr/bin/python3
# Author: Alfredo Velasco

import glob
from collections import Counter

file_list = glob.glob("*txt")

for file in file_list:
	print(file)
	out_f = open(file.split(".")[0] + ".json", "w")
	out_f.write("[")
	out_f.write("\n")
	with open(file) as f:
		read_data = []
		for line in f:
			if (line.startswith('seq')):
				read_data.append(line.split()[-1])
	if len(read_data) == 0:
		continue
	column_counter = [Counter() for i in range(len(read_data[0]))]
	i = 0
	for line in read_data:
		for j in range(len(line)):
			column_counter[j][line[j]] += 1
		i += 1
	for counter in column_counter:
		out_f.write("\t{")
		out_f.write("\n")
		out_f.write("\t\t\"A\": ")
		out_f.write(str(counter['A'] / (1.0 * i)))
		out_f.write(",\n")
		out_f.write("\t\t\"T\": ")
		out_f.write(str(counter['T'] / (1.0 * i)))
		out_f.write(",\n")
		out_f.write("\t\t\"C\": ")
		out_f.write(str(counter['C'] / (1.0 * i)))
		out_f.write(",\n")
		out_f.write("\t\t\"G\": ")
		out_f.write(str(counter['G'] / (1.0 * i)))
		out_f.write("\n")
		if counter == column_counter[-1]:
			out_f.write("\t}")
			out_f.write("\n")
		else:
			out_f.write("\t},")
			out_f.write("\n")
	out_f.write("]")
	out_f.write("\n")
	out_f.close()
