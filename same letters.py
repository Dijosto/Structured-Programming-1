# defining the function
# make sure to add the numbers as a list with [] or it wont work

def same_first_last(numbers):
  # sees if length is greater than 0 and if first number is equal to last number
  return len(numbers) > 0 and numbers[0] == numbers[-1]
