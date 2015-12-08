# In a language of your choosing, write a program that sums all numbers within the range 1-1000 inclusive.
# If that number is a multiple of 3 or 5, double it and add it to the sum. For example, i = 1-10, the answer is 88.

def summation(num):
    i = 0
    summ = 0
    multiple = 0

    for i in range(num + 1):
        if ((i % 3) == 0) or ((i % 5) == 0):
            multiple = i * 2
            summ = summ + multiple
        else:
            summ = summ + i

    print summ

summation(1000)
