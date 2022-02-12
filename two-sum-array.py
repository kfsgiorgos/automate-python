# We are going to solve Leetcode 1 - Given a target value (sum) can we find a pair in the array that sums to the target?


from ast import List


def twoSum(nums, target:int):
    prevMap = {} # val : index

    for i, arraynumber in enumerate(nums):
        diff = target - arraynumber
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[arraynumber] = i


print(twoSum([2,7,11,15], 18))
