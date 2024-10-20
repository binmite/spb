numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total_sum = 0

for i in numbers:
    if i is not None:
        total_sum += i

averageValue = total_sum / len(numbers)

for i, value in enumerate(numbers):
    if value is None:
        numbers[i] = averageValue

print("Измененный список:", numbers)