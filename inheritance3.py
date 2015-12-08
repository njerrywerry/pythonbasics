# overriding the child function but using the Python
# function 'super'to get the parent version to call
# before/after.

class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

# instantiating objects
dad = Parent()
son = Child()

# calling functions on objects
dad.altered()
son.altered()
