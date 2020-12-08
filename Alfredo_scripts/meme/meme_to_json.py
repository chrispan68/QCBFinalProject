#! /usr/bin/python3
# Author: Alfredo Velasco

import glob
from collections import Counter

file_list = glob.glob("*/meme.txt")

for file in file_list:
	print(file)
	out_f = open(file.split(".")[0] + ".json", "w")
	with open(file) as f:
		read_data = []
		for line in f:
			read_data.append(line.strip())
	for i in range(len(read_data)):
		if "position-specific probability matrix" in read_data[i]:
			break
	motif_length = int(read_data[i + 2].split()[5])
	prob_matrix = read_data[i + 3:i + 3 + motif_length]
	out_f.write("[\n")
	for prob in prob_matrix:
		prob_list = prob.split()
		out_f.write("\t{\n")
		out_f.write("\t\t\"A\": ")
		out_f.write(prob_list[0])
		out_f.write(",\n")

		out_f.write("\t\t\"C\": ")
		out_f.write(prob_list[1])
		out_f.write(",\n")

		out_f.write("\t\t\"G\": ")
		out_f.write(prob_list[2])
		out_f.write(",\n")

		out_f.write("\t\t\"T\": ")
		out_f.write(prob_list[3])
		out_f.write("\n")

		if prob == prob_matrix[-1]:
			out_f.write("\t}\n")
		else:
			out_f.write("\t},\n")
	out_f.write("]\n")
	out_f.close()

