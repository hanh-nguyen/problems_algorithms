Time complexity: O(log n)
Space complexity: O(log n)

Algorithm:
- The initial guess is the middle number and updated based on whether the result is too high or too low -> time complexity is O(log n)
- We keep track of the guesses and differences in a dictionary called results -> space complexity is 0(log n)
- If we found a square root of a number as an integer, we return it
- If not, we loop through all the guesses in results to find which one has smallest positive difference -> time complexity is O(log n)