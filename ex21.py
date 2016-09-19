#ex21 - return value of function

def add(a, b):
    print "adding %d + %d" % (a, b)
    return a+b

def substract(a, b):
    print "substracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "dividing %d / %d" % (a, b)
    return a/b

print "Let's do some math with just functions"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq =  divide(100, 2)

print "Age: %d; height: %d; weight: %d; IQ: %d" % (age, height, weight, iq)

print "here a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"
