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


