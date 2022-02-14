def removeDuplicates(nums):
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    return nums[:l]


print(removeDuplicates([1,2,3,3,4]))