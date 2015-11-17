#functions
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

#function with two arguments
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)

#function with one argument
def print_one(arg1):
    print "arg1: %r" %arg1

#function with no arguments
def print_none():
    print "Nothing to see."

print_two("Sly", "Njeri")
print_two_again("Sly", "Njeri")
print_one("Sly")
print_none()
