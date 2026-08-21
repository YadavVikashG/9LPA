name=input("enter your name:")
math=int(input("enter your Math marks:"))
Programming=int(input("enter your Programming marks:"))
Database=int(input("enter your Database marks:"))
English=int(input("enter your English marks:"))
print(name)
print(math)
print(Programming)
print(Database)
print(English)
total=math+Programming+Database+English
percent=total/400*100
print(total)
print(percent)