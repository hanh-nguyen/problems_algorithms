def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0: 
        return None
    if number <= 1: 
        return number
    low = 0
    high = number
    results = {}
    while low <= high:
        result = (low+high) // 2
        dif = number - result ** 2
        if result in results: 
            break
        if dif == 0: 
            return result
        elif dif > 0:
            low = result
            results[result] = dif
        else:
            high = result
            results[result] = dif
    # find the smallest positive difference
    for k, v in results.items():
        if (v >= 0) & (v < dif):
            result = k
            dif = v
    return result

print ("Pass" if  (None == sqrt(-1)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (12 == sqrt(144)) else "Fail")
print ("Pass" if  (11 == sqrt(143)) else "Fail")