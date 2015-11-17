#reading from files
from sys import argv

script, filename = argv

#opening the file
txt = open(filename)
print "Here's your file %r:" %filename
#reading from the file
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

#opening the file
txt_again = open(file_again)
#reading from the file
print txt_again.read()

#closing the file
txt.close()
txt_again.close()
