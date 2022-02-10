# You are given a string s. You need to reverse the string.

s = "Hello World" 
print(s[::-1]) 


### Find subarray with given sum | Set 1 (Nonnegative Numbers)

def subArraySum(arr, n, sum_):
    # Initialize curr_sum as value of first element and starting point as 0
    curr_sum = arr[0]
    start = 0
    # # Add elements one by one to curr_sum and if the curr_sum exceeds the sum, then remove starting element
    i = 1
    while i <= n:
        # If curr_sum exceeds the sum, then remove the starting elements
        while curr_sum > sum_ and start < i-1:
            
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum_:
            print ("Sum found between indexes")
            print ("% d and % d"%(start, i-1))
            return 1
        
        # Add this element to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
    
    print ("No subarray found")
    return 0

arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 15
 
print(subArraySum(arr, n, sum_))






