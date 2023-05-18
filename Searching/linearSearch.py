def linearSearch(array: list[int], target: int) -> bool:
    # Time Complexity: O(n)
    arrayLen = len(array)
    for i in range(arrayLen):
        if array[i] == target:
            return True
    return False