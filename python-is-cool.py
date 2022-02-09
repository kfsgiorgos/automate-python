# lamda, filter, map, reduce

# Assert that square function & lambda function are identical 
def square_fn(x):
    return x * x

square_ld = lambda x: x * x

for i in range(10):
    assert square_fn(i) == square_ld(i)

# List comprehension
nums = [1/3, 333/7, 2323/2230, 40/34, 2/3]
nums_squared = [num * num for num in nums]

# We use the map function to get identical results
# map(function, iterable, ...)
nums_squared_1 = map(square_fn, nums)
nums_squared_2 = map(lambda x: x * x, nums)

assert list(nums_squared_1) == nums_squared


