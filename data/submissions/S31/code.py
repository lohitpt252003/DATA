# Read a line of input, split it by spaces, and convert the parts to integers.
# The map() function applies the int() function to each item of the split input.
a, b = map(int, input().split())

# Print the sum of the two numbers.
print(a + b)