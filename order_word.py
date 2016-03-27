# Given a string, you need to write a method that order every letter in this string in ascending order.
# Also, you should validate that the given string is not empty or null. If so, the method should return:
# "Invalid String!"

def order_word(s):
    if s == '':
        print "Invalid String!"
    else:
        print ''.join(sorted(s))


order_word("Hello, World!")
order_word("bobby")
order_word("")
