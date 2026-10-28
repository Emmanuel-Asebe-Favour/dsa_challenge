def list_sum(numbers):
    count = 0

    for number in numbers:

        count += number

    return count


print(list_sum([2, 4, 6, 8]))
print(list_sum([-5, 10, -2]))
print(list_sum([]))