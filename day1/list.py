books= ["hindi","english","maths","science"]
print(books[0])
books.append("social")
print(books)
books.remove("maths")
print(books)
books.insert(2,"computer")
print(books)
books.sort()
print(books)
books.reverse()
print(books)
books.pop()#it will remove last element of list
print(books)
books.clear()#it will remove all elements of list
print(books)
books1= ["hindi","english","maths","science"]
books2= ["social","computer"]
books1.extend(books2)
print(books1)


