"""Iterative approach"""
# def binary_search(arr, key):

#     arr.sort()
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low+high) // 2
#         if key == arr[mid]:
#             return mid
#         elif arr[mid] < key:
#             low = mid + 1
#         elif arr[mid] > key:
#             high = mid - 1
#     return -1

# arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# key = 141
# result = binary_search(arr, key)
# if result != -1:
#     print("Element is present at index", result)
# else:
#     print("Element is not present in array")


"""Recursive approach"""

def binary_search(arr, key, low, high):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr, key, mid + 1, high)
        else:
            return binary_search(arr, key, low, mid - 1)
    else:
        return -1


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
key = 141
result = binary_search(arr, key, 0, len(arr) - 1)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
