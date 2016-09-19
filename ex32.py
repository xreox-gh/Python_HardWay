#ex32

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dines', 3, 'quarters']

for i in the_count:
    print "This is count %d" % i

for i in fruits:
    print "A fruit of type: %s" % i

for i in change:
    print "I got %r" % i

element = []

for i in range(0,6):
    print "Adding %d to the list." % i
    element.append(i)

element = range(0,9)

print "1 appears %d time" % element.count(i)

New_element = range(11,15)
element.extend(New_element)
for i in element:
    print "2.Element was: %d" % i


element.insert(1, 10)
for i in element:
    print "4.Element was: %d" % i
element.reverse()
for i in element:
    print "5.Element was: %d" % i

element.sort(cmp=lambda x,y:cmp(x[1], y[1]))
for i in element:
    print "6.Element was: %d" % i
