from sys import argv

script, filename = argv

#txt = open(filename)
txt = open('ex15.txt')

print "Here is your file %r:" % filename

print txt.read()

print "Type the file name again:"

file_again = raw_input(">")

#txt_again = open(file_again)
txt_again = open('ex15.txt')

print txt_again.read()

txt.close()

txt_again.close()





