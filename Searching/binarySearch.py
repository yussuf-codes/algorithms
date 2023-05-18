def binarySearch(sortedArray: list[int], beg: int, end: int, target: int) -> bool:
    # Time Complexity: O(log(n))
    if beg > end:
        return False
    
    midPointIndex = (beg + end) // 2
    
    midPoint = sortedArray[midPointIndex]
    
    if midPoint > target:
        return binarySearch(sortedArray, beg, midPointIndex - 1, target)
    elif midPoint < target:
        return binarySearch(sortedArray, midPointIndex + 1, end, target)
    else:
        return True