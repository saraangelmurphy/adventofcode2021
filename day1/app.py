# As the submarine descends, its sonar sweep looks further and further away from the submarine.
# Each line in input.txt is a measurement of sea floor depth
# Create a program that counts the number of times that a depth measurement increases from the previous measurement.

# Read the input.txt file
# If the depth is greater than the previous depth, increase the count, unless there is no previous depth
# If the depth is less than the previous depth, do nothing
# return the count


# Open as text rather than binary
# We use read() to read the entire file, and split lines ourselves to avoid the extra newline inserted by readlines()
lines = open('input.txt', 'r').read().splitlines()
counter = 0
# If there is no previous depth, set the previous depth to the first depth
for (i, depth) in enumerate(lines):
    if i == 0:
        previous_depth = int(depth)
    else:
        if int(depth) > previous_depth:
            counter += 1
        previous_depth = int(depth)
print(counter)
