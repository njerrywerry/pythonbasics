print "Mary had a little lamb."
print "It's fleece was white as %s." %'snow'
print "And everywhere that Mary went."
print "." * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12


#MORE printing
formatter = "%r %r %r %r"
print formatter %(1, 2, 3, 4)
print formatter %("one", "two", "three", "four")
print formatter %(True, False, True, False)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
                "I had this thing.",
                "That you could type up right.",
                "But it didn't sing.",
                "So I said goodnight."
                )

#EVEN MORE printing

#printing in one line
days = "Mon Tue Wed Thur Fri Sat Sun"
#printing things on a new line
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Days of the week:", days
print "Months of the year:", months

#three double quotes allow as much typing as possible
print """
There's a mystery here.
What's going on?
This is magic.
Dare i call this sorcery???
"""
