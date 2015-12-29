# Create a function that takes a number and finds the factors of it,
# listing them in descending order in an array.
# If the parameter is not an integer or less than 1, return -1.
# For Example: factors(54) should return [54, 27, 18, 9, 6, 3, 2, 1]

def factors(n):
    list1 = []
    if (isinstance(n, int) == False) or n < 1:
        print -1
    else:
        list1 = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
        list2 = list(set(list1))
        list2.sort(reverse=True)
        print list2

factors(54)
factors(49)
factors(-4)
factors('a')
