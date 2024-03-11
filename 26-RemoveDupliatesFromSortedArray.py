# -------------------------------------------------------------------------------------------------------------------------- #
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
# -------------------------------------------------------------------------------------------------------------------------- #

# Array test cases
nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

numOfUniques = 0
result = []


def removeDupes(arr):
    x = 0
    size = len(arr)
    for x in range(len(arr) - 1):
        if arr[x] == arr[x + 1]:
            arr[x] = '_'

    for x in range(len(arr)):
        if type(arr[x]) == int:
            result.append(arr[x])

    uniques = len(result)

    for x in range(size - len(result) - 1, size - 1):
        result.append('_')

    print(uniques)
    print(result)


removeDupes(nums1)
