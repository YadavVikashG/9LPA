numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.append(40)
numbers.insert(1, 15)
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers)
squares = []

for number in numbers:
    squares.append(number ** 2)

squares = [number ** 2 for number in numbers]

even_numbers = [x for x in numbers if x % 2 == 0]

#[result for item in collection if condition]
    
