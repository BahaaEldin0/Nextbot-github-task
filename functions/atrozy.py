def add_numbers(num1, num2):
  """
  This function adds two numbers and returns the sum.

  Args:
      num1: The first number.
      num2: The second number.

  Returns:
      The sum of num1 and num2.
  """
  sum = num1 + num2
  return sum

# Get the numbers
num1 = 1.5
num2 = 6.3

# Add the numbers using the function
sum = add_numbers(num1, num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))