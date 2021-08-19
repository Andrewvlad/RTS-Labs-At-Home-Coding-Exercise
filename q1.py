# O(n) time complexity
# O(1) space complexity


# Prints and returns the number of integers in an array that are above the given input and the number that are below.
def above_and_below(input_array, input_number):
    above, below = 0, 0
    for val in input_array:
        if val > input_number:  # checks if the val is above input_number
            above += 1
        elif val < input_number:  # checks if the val is below input_number
            below += 1
    print(f'above: {above}, below: {below}')
    return f'above: {above}, below: {below}'


# Tests the 'above_and_below' method.
def test_above_and_below():
    assert above_and_below([1, 5, 2, 1, 10], 6) == (val := 'above: 1, below: 4'), f'Should be \"{val}\"'
    # Corner-case tests
    assert above_and_below([1, 5, 2, 1, 10], -1) == (val := 'above: 5, below: 0'), f'Should be \"{val}\"'
    assert above_and_below([1, 5, 2, 1, 10], 11) == (val := 'above: 0, below: 5'), f'Should be \"{val}\"'
    assert above_and_below([1, 5, 2, 1, 10], 1) == (val := 'above: 3, below: 0'), f'Should be \"{val}\"'
    assert above_and_below([], 1) == (val := 'above: 0, below: 0'), f'Should be \"{val}\"'


if __name__ == '__main__':
    test_above_and_below()
    print("Everything passed")
