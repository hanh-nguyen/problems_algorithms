**The `lookup` method**
Time complexity: O(n)
Space complexity: O(n)

Algorithm:
- split the path using `split_path` method and store all the parts in an array -> time complexity is O(n), space complexity is O(n)
- apply the `find` method to identify the node and return its handler -> time complexity is O(n), space complexity is O(1)