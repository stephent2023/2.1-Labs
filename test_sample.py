#1
def add_numbers(a, b):
    return a + b

def test1():
    assert add_numbers(4,5) == 9

#2
def is_even(number):
    return number % 2 == 0

def test2():
    assert is_even(5) == False

#3
def find_max(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num

def test3():
    assert find_max([5,6,7,8]) == 8

#4 
def filter_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

def test4():
    assert filter_even([1,2,3,4,5,6,7,8,9]) == [2,4,6,8]

#5
def longest_word_length(string):
    words = string.split()
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

def test5():
    assert longest_word_length("Hello my name is Stephen") == 7

# 5 passed in 0.09s
