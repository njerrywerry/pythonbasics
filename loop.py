# usage of for loops and lists (Ruby arrays)
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#for loops that go through a list
for number in the_count:
    print "This is count %d" %number

for fruit in fruits:
    print "A fruit of type: %s" %fruit

#going through mixed lists.
#using %r since we aren't sure what's in the list.
for i in change:
    print "I got %r" %i

#building lists from empty ones
elements = []

#use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." %i
    #append (add) the elements to the list
    elements.append(i)

#print them out
for i in elements:
    print "Element was: %d" %i

#adding to an empty list without having to use a for loop
element_2 = []
element_2 = range(3)

#printing them out
for i in element_2:
    print "Element was: %d" %i
