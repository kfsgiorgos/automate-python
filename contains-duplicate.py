# Contains Duplicate - Leetcode 217
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums) -> bool:
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False    


print(containsDuplicate([1,2,3,4,9,8,11]))