#def fibonacci(x):
   # print(count(1,5))
   # """
   # Ex. fibonacci(5) returns "1 1 2 3 5 "
   # :param number: The number of Fibonacci terms to return
    #:return: A string consisting of a number of terms of the Fibonacci sequence.
   # """
    #return

def fib(number):
    a = 1
    b = 1

    list = "1 1 "

    for x in range(number):
        c = a + b
        list += str(c) + " "
        a = b
        b = c
    print(list)
    return


fib(number)


def neg(number):
    a = 1
    b = 1

    list ="1 1 "

    for x in range(number):
        c = a + b
        list += str(c) +" "
        a = b
        b = c
    print(list)
    return
fib()
