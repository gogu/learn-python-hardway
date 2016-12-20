from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the file again:"
file_agian = raw_input("> ")

txt_again = open(file_agian)

print txt_again.read()
txt_again.close()
