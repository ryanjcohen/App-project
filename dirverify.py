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
	
	# check whether files have been added to first_error_files, raising 
	# an error with the names of the files if so
	first_error = ("Files in the input list are not all in the directory. " + 
					"Missing files:")
	first_error_files = []
	for file in file_list:
		if file not in file_names:
			first_error_files.append(file)
	
	# check whether the original first_error string has been added to, raising 
	# an error with the new first_error string if so
	if len(first_error_files) != 0:
		first_error = first_error
		first_error_names = "\n".join(first_error_files)
		raise ValueError(first_error + "\n" + file_names)
	
	# populate an array with filenames in the directory matching input regex
	regex_matches = []
	for file in file_names:
		if re.search(regex, file):
			regex_matches.append(file)

	# check if all files with the names matching the regex are found in the 
	# input file_list
	if sorted(file_list) != sorted(regex_matches):
			# report an error with the filenames matching the regex that are 
			# not in the input file_list and the filenames in the fie_list
			# that are not in regex_matches
		second_error = ("Files matching the regex and files in the input fil "
						+ " list are not the same. Files not in both lists:")
		second_error_files = []
		for file in regex_matches:
			if file not in file_list:
				second_error_files.append(file)
		for file in file_list:
			if file not in regex_matches:
				second_error_files.append(file)
		second_error_names = "\n".join(second_error_files)
		raise ValueError(second_error + "\n" + second_error_names)
