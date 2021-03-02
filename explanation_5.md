**The `suffixes` method**
Time complexity: O(n) for n is the number of characters
Space complexity: O(n)

Algorithm:
- initialize an empty array called results
- traverse through the node's children, if any child is a word, add it to the results.
- for each child, we apply the same function (recursion) to traverse through its children