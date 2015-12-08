# Overriding functions in the child class, replacing its functionality.
# Achieved through defining a function in the child class with the same
# name as the function in the parent class.

class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
