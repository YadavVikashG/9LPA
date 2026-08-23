def user(name):
    return("hello " + name)

userName=input("please enter your name :")
print(user(userName))

#above is given an scope of the variable above userName is global varible but 
#below is local variable for funtion

def add():
    userName="radha"#Prefer local variables and avoid unnecessary global state.
    print(userName)
add()    
# print(userName)    

def add1(a,b):
    
    return a+b
add1(10,20)     #it will display the sum of 10 and 20 but it will not return the value to the main program so we can store it in a variable and print it
result=add1(30,20) #it will return the value to the main program and we can store it in a variable and print it
print(result)





