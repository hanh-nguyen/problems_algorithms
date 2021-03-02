def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rotated_array_search_recursion(input_list, number, 0, len(input_list) -1)

def rotated_array_search_recursion(input_list, number, start, end):
    if len(input_list) <= 0: return -1
    if start >= end:
        return start if number == input_list[start] else -1
        
    mid = (start + end) // 2
    if input_list[mid] >= input_list[start]: # first half is sorted
        if (number >= input_list[start]) and (number <= input_list[mid]):
            return binary_search(input_list, number, start, mid)
        else:
            return rotated_array_search_recursion(input_list, number, mid + 1, end)
    elif input_list[mid] <= input_list[end]: # second half is sorted
        if (number >= input_list[mid]) and (number <= input_list[end]):
            return binary_search(input_list, number, mid, end)
        else:
            return rotated_array_search_recursion(input_list, number, start, mid)

def binary_search(sorted_list, number, start, end):
    if start >= end:
        return start if number == sorted_list[start] else -1
    mid = (start + end) // 2
    if sorted_list[mid] == number: 
        return mid
    elif sorted_list[mid] > number: 
        return binary_search(sorted_list, number, start, mid-1)
    else:
        return binary_search(sorted_list, number, mid+1, end)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# All the tests should print Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[4, 5, 6, 7, 0, 1, 2], 0])
test_function([[2, 3], 0])
test_function([[2, 3], 2])
test_function([[2, 3], 3])
test_function([[2, 3], 4])
test_function([[0], 0])
test_function([[0], 1])
test_function([[], 1])
