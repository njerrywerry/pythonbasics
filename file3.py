#copying one file to another
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Contents of %r:" %from_file
indata = open(from_file).read()
print indata

print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit ENTER to continue, CTRL-C to abort."
raw_input(">")

out_file = open(to_file, 'w').write(indata)

print "Contents of %r:" %to_file
outdata = open(to_file).read()
print outdata
