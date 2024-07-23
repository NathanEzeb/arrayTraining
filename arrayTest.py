def filter_even_numbers(arr):
    return [num for num in arr if num % 2 == 0]

# Test the method
my_array = [1, 2, 3, 4, 5]
even_numbers = filter_even_numbers(my_array)
print(even_numbers)