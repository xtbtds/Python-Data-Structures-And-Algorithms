def bubble_sort(arr):
    """
    arr - array need to be sorted
    IsSorted - if after one pass through the array we haven't found at least one 
        bigger element standing before smaller element, the array is already sorted
        and we can finish the algorithm.
    """
    IsSorted = True
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                IsSorted = False
        if IsSorted:
            break
    return arr

if __name__ == "__main__":
    arr = [283,4,6,67,4,3,6,67,56,45,67,65,5,67]
    arr = bubble_sort(arr)
    print(arr)