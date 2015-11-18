def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d boxes of crackers!" %boxes_of_crackers
    print "Total number of cheese and crackers:", cheese_count + boxes_of_crackers
    print "That's enough for a party!\n"

print "We can just give the function numbres directly:"
cheese_and_crackers(20, 30)

print "OR we can use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math"
cheese_and_crackers(10 + 20, 5 + 6)

print "we can combine variables and math"
cheese_and_crackers(amount_of_cheese + 3, amount_of_crackers + 5)
