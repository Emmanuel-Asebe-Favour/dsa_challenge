def first_duplicates(numbers):

    seen = set()

    for number in numbers:
        if number in seen:
           return number
        seen.add(number)

    return None

print(first_duplicates([4, 7, 2, 7, 5, 4]))
print(first_duplicates([1, 2, 3, 4]))
print(first_duplicates([5, 5, 3]))