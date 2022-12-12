# Generated via ChatGPT
# Uses a recursive function to solve

# define the denominations of the coins
denominations = [1, 2, 5, 10, 20, 50, 100, 200]

# define the target amount that we want to make
target = 200

# define a function that takes the current sum and the next coin to use as arguments
# and returns the total number of ways to make the target amount
def ways(current_sum, next_coin):
  # if the current sum is equal to the target amount, we have found one valid way to make the target amount
  if current_sum == target:
    return 1
  # if the current sum is greater than the target amount, we have gone over the target and cannot use this combination
  elif current_sum > target:
    return 0
  # if we have not reached the target amount yet, we can try using the next coin in the denominations
  else:
    # initialize the number of ways to make the target amount to 0
    ways_to_make_target = 0
    # loop through the denominations starting from the next coin
    for i in range(next_coin, len(denominations)):
      # add the number of ways to make the target amount by using the current coin to the total number of ways
      ways_to_make_target += ways(current_sum + denominations[i], i)
    return ways_to_make_target

# call the ways function with 0 as the current sum and 0 as the next coin to use,
# which will give us the total number of ways to make the target amount of £2
print(ways(0, 0))
