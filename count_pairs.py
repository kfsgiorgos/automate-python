### How to count item frequency - dictionary
a_list = [1, 8, 3, 12, 6, 12, 15, 7, 100]

frequencies = {}

for item in a_list:
    if item in frequencies:
        frequencies[item] += 1
    else:
        frequencies[item] = 1



### Count pairs with given sum: Complexity O(N^2)
def getPairsCount(arr, n, sum):
 
    count = 0  # Initialize result
 
    # Consider all possible pairs
    # and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
 
### Count pairs with given sum: Complexity O(N)

import sys

def getPairsCountHaspMap(arr, n, sum):
    
    m = [0] * 1000

	# Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1
    
    twice_count = 0

	# Iterate through each element and increment
	# the count (Notice that every pair is
	# counted twice)
    for i in range(0, n):
        twice_count += m[sum - arr[i]]

		# if (arr[i], arr[i]) pair satisfies the
		# condition, then we need to ensure that
		# the count is decreased by one such
		# that the (arr[i], arr[i]) pair is not
		# considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

	# return the half of twice_count
    return int(twice_count / 2)


# Driver function

arr = [1, 5, 8, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs of brute force function is", getPairsCount(arr, n, sum))
print("Count of pairs of hash map function pairs is", getPairsCountHaspMap(arr,n, sum))

