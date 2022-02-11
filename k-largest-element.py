from ast import List
from audioop import reverse


def findKthLargest(nums, k):
    nums.sort()
    return(nums[len(nums) - k])

def findKthSmallest(nums, k):
    nums.sort(reverse = True)
    return(nums[len(nums) - k])


arr = [7, 10, 4, 3, 20, 15, 76, 12, 28]
k = 6

print(f"The {k}th largest value is the element: {findKthLargest(nums=arr, k=k)} ")
print(f"The {k}th smallest value is the element: {findKthSmallest(nums=arr, k=k)} ")
print("The complexity of the algorithm is O(N Log N) ")
