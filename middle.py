# You are going to be given a word. Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.


def get_middle(s):
    if (len(s)) % 2 == 0:
        a = s[:len(s) / 2]
        b = s[len(s) / 2:]
        mid = a[len(a) - 1] + b[0]
    else:
        mid = s[len(s) / 2]

    print mid

get_middle("testing")
get_middle("test")
get_middle("middle")
