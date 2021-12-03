# PROMPT:
# As the submarine descends, its sonar sweep looks further and further away from the submarine.
# Each line in input.txt is a measurement of sea floor depth
# Create a program that counts the number of times that a depth measurement increases from the previous measurement.

# PSEUDO CODE:
# Read the input.txt file
# If the depth is greater than the previous depth, increase the count, unless there is no previous depth
# If the depth is less than the previous depth, do nothing
# return the count

# We need to do this to make the VS Code debugger happy
import os
file_path = os.path.join(os.path.expanduser('~'), 'github', 'adventofcode2021', 'day1', 'input.txt')
class Solution1:
    def __init__(self):
        self.counter = 0
        self.previous_depth = 0
        self.test_case()
    def count_increases(self, lines):
        for (i, depth) in enumerate(lines):
            if i == 0:
                self.previous_depth = int(depth)
            else:
                if int(depth) > self.previous_depth:
                    self.counter += 1
                self.previous_depth = int(depth)
        return self.counter
    
    def test_case(self):
        test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        assert self.count_increases(test_input) == 7
        print('Test case passed')


# Instantiate the class
submarine = Solution1()

# Read the entire file
input = open(file_path, 'r').read().splitlines()
print(submarine.count_increases(input))

# Solution Part 2
# For every 3 measurements in the list, sum the measurements and compare to the previous sum.
# If the sum is greater than the previous sum, increase the count
# Regardless of whether it is greater or not, set previous_sum to the new sum

class solution2:
    def __init__(self):
        self.counter = 0
        self.previous_sum = 0
        self.window_num = 3
        self.window_sum = 0
        self.test_case()

    def count_increases(self, lines):
        for (i, depth) in enumerate(lines):
            # We don't want to do anything until we have at least one complete sliding window
            if i >= 2:
                self.window_sum = int(lines[i]) + int(lines[i-1]) + int(lines[i-2])
                # The sum of first sliding window should be greater than 0, so we get +1 for the first window
                if self.window_sum > self.previous_sum and self.previous_sum != 0:
                    self.counter += 1
                self.previous_sum = self.window_sum
        return self.counter
    
    def test_case(self):
        test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        assert self.count_increases(test_input) == 5
        print('Test case passed')

# Instantiate the class
submarine = solution2()

# Test Case
print(submarine.count_increases(input))