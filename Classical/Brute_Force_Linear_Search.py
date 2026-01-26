
def index_of(arr, target):
    
    """
    NAME:
        Linear Search - find the first index of a target in a list (linear scan).

    SYNOPSIS:
        index = index_of(arr, target)

    DESCRIPTION:
        Checks elements from left to right until the target is found or the sequence ends. Works on unsorted data.
        Scans arr from left to right, comparing each element to target using ==.
        Stops at the first match.

    PARAMETERS:
        arr
            Sequence to search (e.g., list). Elements must be comparable to target
            via ==.
            
        target
            Value to locate in arr.

    RETURN VALUE:
        Returns the zero-based index of the first matching element.
        Returns -1 if target is not found.

    NOTES:
        If arr is empty, -1 is returned.

    TIME COMPLEXITY:
        O(n)
        Tells you how long it takes. Gets slower as the list gets bigger.
        In the worst case, the target is not present or is the last element.
        The algorithm checks every element once. Number of comparisons grows linearly with n.
        Best case: O(1) (first element matches)
        Average case: O(n)
        Worst case: O(n)

    EXAMPLES:
        numbers = [5, 3, 8, 1, 9]
        index of(numbers, 8)  # Output index 2
    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


numbers = [5, 3, 8, 1, 9]
print(index_of(numbers, 8))
