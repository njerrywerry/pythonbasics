#usage of import modules
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "First variable:", first
print "Second variable:", second
print "Third variable:", third

fourth = raw_input("Name? ")
print "Your name is %s" %fourth
