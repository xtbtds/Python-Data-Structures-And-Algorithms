def selection_sort(array):
    """
    arr - array need to be sorted
    min_index - on each step of external loop we "select" the smaller element,
        then we swap it with the first element
    """
    length = len(array)
    for i in range(length-1):
        min_index = i
        for j in range(i+1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == "__main__":
    arr = [283,4,6,67,4,3,6,67,56,45,67,65,5,67]
    arr = selection_sort(arr)
    print(arr)
