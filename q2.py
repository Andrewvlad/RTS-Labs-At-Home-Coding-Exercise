# O(n+k) time complexity (Worst time complexity - O(2n-1)):
#   O(k) (Get Slice 1)
#   O(n-k) (Get Slice 2)
#   O(k) (Concatenate Slices)
#   CPython time-complexity - https://wiki.python.org/moin/TimeComplexity
# O(1) space complexity

# Rotates the characters in a string by a given input and have the overflow appear at the beginning.
def rotated_string(input_string, input_number):
    input_number = input_number % len(input_string)  # in case input_number > len(input_string)
    print(input_string[-input_number:] + input_string[:-input_number])
    return input_string[-input_number:] + input_string[:-input_number]


# Tests the 'rotated_string' method.
def test_rotated_string():
    assert rotated_string("MyString", 2) == 'ngMyStri', "Should be \"ngMyStri\""
    # Corner-case tests
    assert rotated_string("MyString", 10) == 'ngMyStri', "Should be \"ngMyStri\""
    assert rotated_string("MyString", -6) == 'ngMyStri', "Should be \"ngMyStri\""
    assert rotated_string("MyString", -8) == 'MyString', "Should be \"MyString\""
    assert rotated_string("MyString", 0) == 'MyString', "Should be \"MyString\""
    assert rotated_string("MyString", 8) == 'MyString', "Should be \"MyString\""


if __name__ == '__main__':
    test_rotated_string()
    print("Everything passed")
