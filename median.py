"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if len(numbers) % 2 == 1:
            median = numbers[int((len(numbers)-1)/2)]
        else:
            index = int(len(numbers)/2)
            m1 = numbers[index - 1]
            m2 = numbers[index]
            median = (m1 + m2)/2
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
