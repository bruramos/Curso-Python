def fizzbuzz(n):
    if (n % 3 == 0 and n % 5 == 0):
        return "FizzBuzz"
    if (n % 3 == 0 and n % 5 != 0):
        return "Fizz"
    if (n % 3 != 0 and n % 5 == 0):
        return "Buzz"
    else:
        return n

def test_fizzbuzz():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(12) == "Fizz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(20) == "Buzz"
    assert fizzbuzz(22) == 22
