# Leetcode 53
def maxSubArraySum(a,size):
	
	max_so_far = a[0]
	max_ending_here = 0
	
	for i in range(0, size):
		max_ending_here = max_ending_here + a[i]
		if max_ending_here < 0:
			max_ending_here = 0
		
		# Do not compare for all elements. Compare only
		# when max_ending_here > 0
		max_so_far = max(max_ending_here, max_so_far)
	return max_so_far

# Driver function to check the above function
a = [-2, -3, 4, -1, -2, 1, 9, -3]
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))

