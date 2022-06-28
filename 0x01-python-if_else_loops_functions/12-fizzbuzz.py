#!/usr/bin/python3
def fizzbuzz():
    """Fizz Buzz function

    Returns:
        Void
    """
    i = 1
    while i <= 100:
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        else:
            if i % 5 == 0:
                print("Buzz", end=" ")
            else:
                if i % 3 == 0:
                    print("Fizz", end=" ")
                else:
                    print(i, end=" ")
        i = i + 1
