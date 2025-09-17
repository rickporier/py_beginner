# The outer loop begins its first iteration.
# It sets `num_1` to the first value in the range (0 in this case).
for num_1 in range(2):
    
    # For every single iteration of the outer loop, the inner loop starts.
    # The inner loop will run completely for each value of `num_1`.
    # It sets `num_2` to the first value in the range (0 in this case).
    for num_2 in range(2):
        
        # During each iteration of the inner loop, the current values of `num_1`
        # (from the outer loop) and `num_2` (from the inner loop) are printed.
        print(num_1, num_2)
    
    
    # After the inner loop finishes all its iterations for a single value of `num_1`,
    # the outer loop proceeds to the next value of `num_1`.

# Once the outer loop has iterated through all its values, the program ends.
