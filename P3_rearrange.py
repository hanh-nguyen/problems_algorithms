def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1: return input_list
    quicksort_descending(input_list)
    num_one = ''
    num_two = ''
    for i in range(0, len(input_list), 2):
        num_one += str(input_list[i])
        if i + 1 < len(input_list):
            num_two += str(input_list[i+1])
    return [int(num_one), int(num_two)]

def quicksort_descending(arr):
    if len(arr) <= 1: 
        return
    front_index = 0
    pivot_index = len(arr) -1
    pivot = arr[pivot_index]
    while front_index < pivot_index:
        if arr[front_index] < pivot:
            arr[pivot_index] = arr[front_index]
            arr[front_index] = arr[pivot_index -1]
            arr[pivot_index -1] = pivot
            pivot_index -= 1
        else:
            front_index += 1
    left = quicksort_descending(arr[:pivot_index])
    right = quicksort_descending(arr[pivot_index + 1:])


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[0, 2, 1], [20, 1]]
test_function(test_case)

test_case = [[1], [1]]
test_function(test_case)

test_case = [[0], [0]]
test_function(test_case)

test_case = [[], []]
test_function(test_case)