Time complexity: O(log n)
Space complexity: O(1)

Algorithm
- The array is split by the middle point. For each half, we check if it is sorted. If yes, we use binary search to find the number and return the index. If not, we apply recursion -> time complexity is 0(log n)
- No extra data structure