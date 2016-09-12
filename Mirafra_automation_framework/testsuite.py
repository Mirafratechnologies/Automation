#!/usr/bin/python

import unittest   # second test
import sys   # second test
import os
#from dummy import ConfigTestCase
#import testcases

import importlib

if (not sys.argv[1:]):
	print "Missing : List of testcases file\n"
	print "Usage:\n"
	print sys.argv[0] + " <List_of_testcases>\n"
	print "where List_of_testcases is a file having the testcases to be executed\n"
	sys.exit(2)

print str(sys.argv[1])

if (os.path.isfile("Result.txt")):
        os.remove("Result.txt")
f = open("Result.txt", "w+")
f.write("Status(0-pass/1-fail) Execution_Time Testcase\n")
f.close()

def load_class(module_path, class_str):
    """
    dynamically load a class from a string
    """
    module = importlib.import_module(module_path)
    # Finally, we retrieve the Class
    return getattr(module, class_str)

#from test_sample1.test_sample1 import ConfigTestCase
#from test_sample2.test_sample1 import ConfigTestCase2
#from ssh_paramiko.ssh_paramiko import ConfigTestCase

#class ConfigTestCase(unittest.TestCase):
#	def setUp(self):
#		print 'stp'
###set up code
#
#	def runTest(self):
#
##runs test
#		print 'stp'
#
def suite():
	"""
	Gather all the tests from this module in a test suite.
	"""
#	test_suite = unittest.TestLoader()
#	test_suite.loadTestsFromTestCase(ConfigTestCase)
#	test_suite.loadTestsFromTestCase(ConfigTestCase2)
	test_suite = unittest.TestSuite()
	#f = open('testcases.py')
	testlist = open(str(sys.argv[1]))
	for line in testlist.readlines():
		a = line.split(" ")
		module = a[0]
		class1 = a[-1]
		#load_class(module,class1.rstrip("\n"))
		test_suite.addTest(unittest.makeSuite(load_class(module,class1.rstrip("\n"))))
	testlist.close()

#	test_suite.addTest(unittest.makeSuite(ConfigTestCase))
#	test_suite.addTest(unittest.makeSuite(ConfigTestCase2))
	return test_suite

mySuit=suite()

#runner=unittest.TestLoader().loadTestsFromTestCase(ConfigTestCase)
runner=unittest.TextTestRunner(verbosity=2)

runner.run(mySuit)
