import array

def move_zeros(arr):
    zero_index = 0
    for index in range(len(arr)):
        n = arr[index]
        if n != 0:
            arr[zero_index] = n
            if zero_index != index:
                arr[index] = 0
            zero_index += 1
    return(arr)

arr = [99, 0, -7, 0, 16]
# arr = array.array("i", [99, 0, -7, 0, 16])

move_zeros(arr)
print(arr)
