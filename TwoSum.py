# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# array = [2, 7, 11, 15]
array = [3, 2, 4]


def twoSum(nums, target):
    for x in range(0, len(nums)):
        if (nums[x] + nums[x + 1] == target):
            print(x, x + 1)
            break


twoSum(array, 6)
