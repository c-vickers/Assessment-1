"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    # all_odd = []
    # for number in number_list:
    #     if number % 2 > 0:
    #         all_odd.append(number)
    # return all_odd
    all_odd = [number for number in number_list if number % 2 > 0]
    return all_odd

def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    # all_even = []
    # for number in number_list:
    #     if number % 2 == 0:
    #         all_even.append(number)
    # return all_even
    all_even = [number for number in number_list if number % 2 == 0]
    return all_even

def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    for item in my_list:
        print my_list.index(item), item


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    # long_words = []
    # for word in word_list:
    #     if len(word) > 4:
    #         long_words.append(word)
    # return long_words

    long_words = [word for word in word_list if len(word) > 4]
    return long_words


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    # smallest = None
    # start = 0
    # end = len(number_list) - 1
    # while start < end:
    #     if number_list[start] < number_list[start + 1]:
    #         smallest = number_list[start]
    #         start += 1
    #     elif number_list[start] > number_list[start + 1]:
    #         smallest = number_list[start +1]
    #         start += 1
    # return smallest
    if number_list == []:
        return None
    else:
        number_list.sort()
        return number_list[0]

def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    if number_list == []:
        return None
    else:
        number_list.sort()
        number_list.reverse()
        return number_list[0]


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    # halvesies = []
    # for number in number_list:
    #     half = float(number) / 2
    #     halvesies.append(half)
    # return halvesies

    halvesies = [float(number) / 2 for number in number_list]
    return halvesies

def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    # word_length = []
    # for word in word_list:
    #     length = len(word)
    #     word_length.append(length)
    # return word_length

    word_length = [len(word) for word in word_list]
    return word_length


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    total = 0
    for number in number_list:
        total += number
    return total


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    total = 1
    for number in number_list:
        total *= number
    return total


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    string = ""
    for word in word_list:
        string += word
    return string



def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    total = 0
    for number in number_list:
        total += number
        average = float(total) / len(number_list)
    return average


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """
    string = ''
    start = 0
    end = len(list_of_words) -1
    while start <= end:
        for word in list_of_words:
            if start < end:
                string += word + ', '
                start += 1
            else:
                string += word
                start += 1
    return string


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
