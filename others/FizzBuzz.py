"""
This code defines a function fizzBuzz that
takes an integer n as input and prints the 
numbers from 1 to n with the following rules:
For multiples of 3 and 5, print "FizzBuzz".
For multiples of 3, print "Fizz".
For multiples of 5, print "Buzz".
For all other numbers, print the number itself """
def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        if i % 3 == 0:
            print ("Fizz")
        if i % 5 == 0:
            print ("Buzz")
        else:
            print (i)

n = 10
fizzBuzz(n)