def get_even(numbers):
    even_nums = [num for num in numbers if num%2==1 ]
    return even_nums
print(get_even([1, 2, 3, 4, 5, 6]))