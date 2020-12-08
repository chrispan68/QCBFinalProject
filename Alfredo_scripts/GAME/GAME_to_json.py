#! /usr/bin/python3
# Author: Alfredo Velasco

import glob
from collections import Counter

file_list = glob.glob("*txt")

for file in file_list:
	print(file)
	with open(file) as f:
		read_data = []
		for line in f:
			read_data.append(line.strip())
	# print(read_data)
	for i in range(len(read_data)):
		if "Motif #1:" in read_data[i]:
			break
	# No motif was found
	if(len(read_data) <= i + 3):
		continue
	num_sites = int(read_data[i+3].split()[3][:-1])
	motif_w = int(read_data[i+3].split()[1][:-1])
	column_counter = [Counter() for i in range(motif_w)]
	site_list = [read_data[i + 6 + 2 * j] for j in range(num_sites)]
	i = 0
	for site in site_list:
		for j in range(motif_w):
			column_counter[j][site[j]] += 1
		i += 1

	out_f = open(file.split(".")[0] + ".json", "w")
	out_f.write("[")
	out_f.write("\n")
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
