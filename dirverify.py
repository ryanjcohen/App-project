import os
import re

def dir_verify(file_list, directory, regex = ".*"):
	""" Checks that all files in the input list file_list are in the input 
	directory string. Then uses input regex string to find matching filenames 
	in directory and checks that all matching filenames are in the input 
	file_list.

	Args:
		file_list (list of str): List of filenames
		directory (str): Directory containing files to be veried
		regex (str): Regular expression to be used, defaults to ".*"
	"""
	
	# extract list of files in the input directory
	file_names = os.listdir(directory)
	
	# check that each file in file_list is in the input directory, adding its 
	# name to first_error if it is not
	first_error = ("Files in the input list are not all in the directory. " + 
					"Missing files:")
	for file in file_list:
		if file not in file_names:
			first_error = first_error + "\n" + file
	
	# check whether the original first_error string has been added to, raising 
	# an error with the new first_error string if so
	if first_error != ("Files in the input list are not all in the directory. " 
					+ "Missing files:"):
		raise ValueError(first_error)
	
	# populate an array with filenames in the directory matching input regex
	regex_matches = []
	for file in file_names:
		if re.search(regex, file):
			regex_matches.append(file)

	# check if all files with the names matching the regex are found in the 
	# input file_list
	if sorted(file_list) != sorted(regex_matches):
			# report an error with the filenames matching the regex that are 
			# not in the input file_list
		second_error = ("Files matching the regex and files in the input fil "
						+ " list are not the same. Files not in both lists:")
		for file in regex_matches:
			if file not in file_list:
				second_error = second_error + "\n" + file 
				print second_error
		for file in file_list:
			if file not in regex_matches:
				second_error = second_error + "\n" + file
		raise ValueError(second_error)

files = [ 
			"test1.txt", "test1.pdf", "tester.txt"]
directory = "dirverify tests"
regex = "test"

dir_verify(files, directory, regex)
