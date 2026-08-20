#Problem 1
age=int(input("enter your age:"))
if age<13:
    print("you are teenager")
elif age>=20:
    print("you are adult ")
#Problem 2
num=int(input("enter your number to know is odd or evern:"))
if num%2==0:
    print("your number evern")
else:
    print("your number odd ")
#Problem 3  for eveen== for odd !=
for i in range(1,101):
    if i % 2 != 0 :
        print(i)
#Problem 4 find largest numbre
numbers = [10, 25, 3, 48, 17, 92, 6]
largest=numbers[0]
for number in numbers:
    if number > largest:
        largest=number
        print(number)
#Problem 4

def cal_salary(basic_salary):
        hra =basic_salary *.20
        da =basic_salary *.10
        total_salary =basic_salary + hra+ da
        return total_salary
mysalary=cal_salary(25000)  
print(mysalary)      

