# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
# of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.


def minSubArrayLen(target:int, nums):
    l, total = 0,0 
    res = len(nums) + 10 # We give a number greater then the length 

    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(r - l + 1, res)
            total -= nums[l]
            l += 1

    return 0 if res == len(nums)+10 else res

# Driver function to check the above function
a = [5,1,3,5,7,7,4,9,2,8]
print("Minimum Size Subarray Sum is" , minSubArrayLen(15, a))

