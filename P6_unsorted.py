def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0: return (None, None)
    low = ints[0]
    high = ints[0]
    for i in ints:
        if i < low:
            low = i
        elif i > high:
            high = i
    return (low, high)

## Example Test Case of Ten Integers
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = []
print ("Pass" if ((None, None) == get_min_max(l)) else "Fail")

l = [1]
print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")