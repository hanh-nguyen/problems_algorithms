def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    sorted_arr = []
    count_zero = 0
    for i in input_list:
        if i == 0:
            sorted_arr = [i] + sorted_arr
            count_zero += 1
        elif i == 1:
            sorted_arr = sorted_arr[:count_zero] + [i] + sorted_arr[count_zero:] 
        else:
            sorted_arr.append(i)
    return sorted_arr

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([0, 1])
test_function([1, 0])

test_function([0])
test_function([1])
test_function([2])