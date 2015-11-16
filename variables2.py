#embedded variables, ie. how you would do #{name} in Ruby
my_name = 'Sylvia Kieha'
my_age = 21
my_height = 73.6 #inches
my_weight = 65 #kgs
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'red'

print "Lets talk about %s." %my_name
print "She's %r inches tall." %my_height
print "She's %d kgs heavy." %my_weight
print "She's got %s eyes and %s hair." %(my_eyes, my_hair)
print "Her flawless %s teeth are always dazzling." %my_teeth

#god-status
print "If I add %d, %r, and %d I get %r." %(my_age, my_height, my_weight, my_age + my_height + my_weight)
