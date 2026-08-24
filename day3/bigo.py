#the below is O(1) — Constant time
numbers = [10, 20, 30, 40, 50]
print(numbers[2])
#O(n) — Linear time
def print_numbers(numbers):
    for number in numbers:
        print(number)
#O(n²) — Quadratic time
def pairs(numbers):
    for i in numbers:
        for j in numbers:
            print(i, j)       
#O(log n)This is the idea behind binary search.
             