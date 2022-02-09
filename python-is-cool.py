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

# We use map with more than one iterable.
# We calculate the mean squared error of a simple linear function f(x) = ax + b using the true label labels
a, b = 3, -0.5
xs = [2, 3, 4, 5]
labels = [6.4, 8.9, 10.9, 15.3]

# Method 1: using a loop
errors = []
for i, x in enumerate(xs):
    errors.append((a * x + b - labels[i]) ** 2)
result1 = sum(errors) ** 0.5 / len(xs)

# Method 2: using map
diffs = map(lambda x, y: (a * x + b - y) ** 2, xs, labels)
result2 = sum(diffs) ** 0.5 / len(xs)

assert result1 == result2, "result1 != result2"

# filter function 
# Objects returned by map and filter are iterators, which means that their values aren't stored but generated as needed. 
# After we've called sum(diffs), diffs becomes empty.  
# If we want to keep all elements in diffs ==> We have to convert it to a list using list(diffs)

# filter(fn, iterable) works the same way as map, except that fn returns a boolean value and 
# filter returns all the elements of the iterable for which the fn returns True.
print("Errors")
print(errors)
bad_preds = filter(lambda x: x > 0.5, errors)
print("Bad predictions")
print(list(bad_preds))


# reduce function reduce(fn, iterable, initializer)
product = 1
for num in nums:
    product *= num

from functools import reduce
product1 = reduce(lambda x, y: x * y, nums)

assert product == product1 , "product != product1"






