from dirverify import dir_verify
import unittest
import os

class TestDirVerify(unittest.TestCase):

	# testing dir_verify with a file_list, directory, and regex that should 
	# result in no errors
	def test_no_error(self):
		self.assertEqual(dir_verify(["festive.pdf", "festive.txt", "test1.txt", 
			"test1.pdf", "tester.txt"], "dirverify_tests", "est"), None)

	# testing dir_verify with a file_list and directory that should result in 
	# no errors
	def test_no_regex(self):
		self.assertEqual(dir_verify(["festive.txt", ".DS_Store", "test1.txt",
			"goodbye.txt", "festive.pdf", "test1.pdf", "tester.txt", 
			"hello2.txt", "hello.txt"], "dirverify_tests"), None)

	# testing dir_verify with a file_list, directory, and regex that should 
	# result in the first error being raised
	def test_first_error(self):
		self.assertRaises(ValueError, dir_verify, ["festiv.pdf", "festive.txt", 
			"test1.txt", "test1.pdf", "tester.txt"], "dirverify_tests", "test")

	# testing dir_verify with a file_list, directory, and regex that should
	# result in the second error being raised
	def test_second_error(self):
		self.assertRaises(ValueError, dir_verify, ["festive.pdf", "test1.txt", 
			"test1.pdf", "tester.txt"], "dirverify_tests", "est")

if __name__ == '__main__':
	unittest.main()
