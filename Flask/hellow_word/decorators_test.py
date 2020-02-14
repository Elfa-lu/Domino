# https://www.youtube.com/watch?v=r7Dtus7N4pI
# decorators are a way to change or modify the behavior of any of your functions or methods
# without directly changing any of the code


# ==================== 1.====================
def f1():
    print("call f1")
print(f1)
# f1 as an object and can be passed around our program
# output function f1 at...


# ==================== 2.====================
def f2(f):
    f()
f2(f1)
# output: call f1


# ==================== 3. wrapper functions ====================
def f1(func):
    def wrapper():
        print("started")
        func()
        print("end")
    return wrapper

def f():
    print("hello")

f1(f)()
# f1(f) will return the function, not calling it
# output: started end hello
# this will allow us to decorate a function

# same output:
x = f1(f)
x()


# ==================== 4. decorators ====================
def f1(func):
    def wrapper():
        print("started")
        func()
        print("end")
    return wrapper

# x = f1(f)
# everytime we call f, we pass the function f as a parameter to f1
@f1
def f():
    print("hello")

# can get the same result and no longer need to include that line
f()


# ==================== 5. args kwargs ====================
def f1(func):
    # this wrapper function will have certain amount of parameters
    def wrapper(*args, **kwargs):
        print("started")
        func(*args, **kwargs)
        print("end")
    return wrapper

@f1
def f(a):
    print(a)

f("hi")


# ==================== 5. return values from decorated funtions ====================
def f1(func):
    def wrapper(*args, **kwargs):
        print("start")
        val = func(*args, **kwargs)
        print("end")
        return val
    return wrapper

@f1
def add(x,y):
    return x+y
print(add(4,5))


# ==================== 6. Example - authorization ====================
# https://www.runoob.com/w3cnote/python-func-decorators.html]

# If I don not want to change the function, while I want to add more function to them. use decorator
from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)

    return decorated