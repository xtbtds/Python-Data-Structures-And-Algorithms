def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        prev = i-1
        key = array[i]
        while prev >= 0 and array[prev] > key:
            array[prev+1] = array[prev]
            prev -= 1
        array[prev+1] = key

    return array

if __name__ == "__main__":
    array = [3,4,6,2,8,4,9,1,5,6,7,3]
    print(array)
    res = insertion_sort(array)
    print(res)
        
