def merge(lArray: list[int], rArray: list[int]) -> list[int]:
    mergedArray = []

    lPointer = 0
    rPointer = 0
    
    lArrayLen = len(lArray)
    rArrayLen = len(rArray)
    
    while lArrayLen > lPointer and rArrayLen > rPointer:
        if lArray[lPointer] < rArray[rPointer]:
            mergedArray.append(lArray[lPointer])
            lPointer += 1
        elif lArray[lPointer] > rArray[rPointer]:
            mergedArray.append(rArray[rPointer])
            rPointer += 1
        else:
            mergedArray.append(lArray[lPointer])
            mergedArray.append(rArray[rPointer])
            lPointer += 1
            rPointer += 1

    while lArrayLen > lPointer:
        mergedArray.append(lArray[lPointer])
        lPointer += 1
        
    while rArrayLen > rPointer:
        mergedArray.append(rArray[rPointer])
        rPointer += 1

    return mergedArray


def mergeSort(unsortedArray: list[int]) -> list[int]:
    # Time Complexity: O(n log(n))
    if len(unsortedArray) == 1:
        return unsortedArray

    midPointIndex = len(unsortedArray) // 2

    lArray = unsortedArray[:midPointIndex]
    rArray = unsortedArray[midPointIndex:]

    return merge(mergeSort(lArray), mergeSort(rArray))