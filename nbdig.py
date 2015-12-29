# Take an integer n and a digit d as an integer.
# Square all numbers k between 0 and n.
# Count the numbers of digits d used in the writing of all the k**2.
# Call the function taking n and d as parameters and returning this count.

def nb_dig(n, d):
    string1 = ''
    d = str(d)
    for i in range(0, (n + 1)):
        square = i * i
        string1 += str(square)
    print string1.count(d)

nb_dig(10, 1)
nb_dig(5750, 0)
nb_dig(11011, 2)
nb_dig(12224, 8)
nb_dig(11549, 1)
