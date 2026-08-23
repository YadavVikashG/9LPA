#Challenge 1 — Reverse a string
name="vikash"
print(name[::-1])
#Challenge 2 — Count vowels
vowels = "aeiou"
text = "this is vikash gajraj yadav.they are"
count = 0
for char in text:
    if char in vowels:
        count+=1
print("Number of vowels:", count)
#Challenge 3 — Find maximum
numbers = [15, 2, 89, 32, 7, 45]
def find_maximum(numbers):
    max_num=numbers[0]
    for num in numbers:
        if num>max_num:
            max_num=num
    return max_num
print("Maximum number:", find_maximum(numbers))
def find_second_maximum(numbers):
    max_num=numbers[0]
    second_max_num=numbers[0]
    for num in numbers:
        if num>max_num:
            second_max_num=max_num          
            max_num=num
    return second_max_num
print("Second maximum number:", find_second_maximum(numbers))
#Challenge 4 — Remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
uninumber=[]
for num in numbers:
    if num not in uninumber:
        uninumber.append(num)
print("Unique numbers:", uninumber)
#Challenge 5 — Frequency counter
text = "programming"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character frequency:", frequency)
#Challenge 6 — Palindrome check
def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome("madam"))

text = "ama"
ptext=text[::-1]
if text==ptext:
    print("it is palindrome")
else:
    print("it is not palindrome")     
      


