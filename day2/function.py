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