#!/usr/bin/env python3

import csv
import os
import re

main_path = os.environ["HOME"] + "/Desktop/GRE/gre/vocabulary/barrons/"
file_name = main_path + "barrons800_mnemonics2.txt"
output_file = main_path + "sheet.csv"

if __name__ == '__main__':
	start_word_def, start_syn_def, start_example = False, False, False
	word, synonyms, word_def, syn_def, example_sentences = "", "", "", "", ""

	#open files
	file1 = open(file_name,"r")
	
	with open(output_file, "w") as csv_file:
		csv_reader = csv.writer(csv_file, delimiter=',')
		for line in file1:
			line = line.lstrip().rstrip("\n")
			# line = line.replace(" ","")
			if line[0:3] == "$@#":
				if word != "":
					print(word)
					# row = [word, word_def, synonyms.lstrip(" "), syn_def, example_sentences]
					row = [word, word_def]
					csv_reader.writerow(row)
					synonyms, word_def, syn_def, example_sentences = "", "", "", ""
					start_example = False

				word = line[3:]
				start_word_def = True

			if start_word_def and line[0:len("Definition ")] == "Definition ":
				word_def = line[len("Definition :")-1:]
				start_word_def = False

			if line[0:len("Synonyms :")] == "Synonyms :":
				# line = line.replace(" ","")
				synonyms += re.sub(' +', ' ', line[len("Synonyms :"):]).replace(' ,', ',')
				start_syn_def = True

			if start_syn_def and line[0:len("Definition ")] == "Definition ":
				syn_def = line[len("Definition :")-1:]
				start_syn_def = False

			if start_example:
				if len(line) != 0:
					example_sentences += line.lstrip(' ') + "\n"
					# print("Example: " + example_sentences)

			if line[0:len("Example Sentence")] == "Example Sentence":
				start_example = True





	## Sample
	# $@#abate

	# Definition (verb) make less active or intense
	                              
	# Synonyms :             slack  ,              slake 
	# Definition (verb) become less in amount or intensity
	                              
	# Synonyms :             die away  ,              let up  ,              slack  ,              slack off 
	# Example Sentence 


	#                 The storm abated
	              

	#                 The rain let up after a few hours
	              




	#             rebate means discount... i.e reducing the price..
	# abate and rebate are rhyming words

