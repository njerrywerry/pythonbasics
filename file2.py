#reading and writing files
from sys import argv

script, filename = argv

target = open(filename)
print "Contents of %r" %filename
print target.read()

print ".............................................."

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit ENTER."

raw_input("?")

print ".............................................."

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print ".............................................."

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ".............................................."

print "New contents of %r:" %filename
target = open(filename)
print target.read()

print ".............................................."

print "And finally, we close it."
target.close()
