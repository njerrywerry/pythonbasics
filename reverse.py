# You are going to be given a string. Your job is to return that string in a certain order that I will explain below:
# Let's say you start with this: 012345
# The first thing you do is reverse it:543210
# Then you will take the string from the 1st position and reverse it again:501234
# Then you will take the string from the 2nd position and reverse it again:504321
# Then you will take the string from the 3rd position and reverse it again:504123
# Continue this pattern until you have done every single position, and then you will return the string you have created.
# For this particular number, you would return:504132

def reverse_fun(n):
    list1 = []
    list2 = list(n)

    i = len(list2)
    while i > 0:
        list2 = list2[::-1]
        list1.append(list2.pop(0))
        i -= 1

    print "".join(list1)


reverse_fun("012345")
reverse_fun("jointhedarkside")
