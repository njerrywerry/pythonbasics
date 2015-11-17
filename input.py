print "How old are you?",
#converts string input to integer
age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "You are %d years old, %s inches tall and %s kgs heavy." %(age, height, weight)
age = age + 2
print "You will be %d years old in two years." %age

#another way to get user input
age = int(raw_input("How old are you? "))
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "You are %d years old, %s inches tall and %s kgs heavy" %(age, height, weight)
