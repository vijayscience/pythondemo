# code
s="GFG"
s=iter(s)
print(s)
print(next(s))

def nextGen():
    yield 1
    yield 2
    yield 3

# for value in nextGen():
#     print(value)

x = nextGen()
print(next(x))
print(next(x))
print(next(x))
# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
	return text.upper() 

print(shout('Hello')) 

yell = shout 

print(yell('Hello')) 

# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
	return text.upper() 

def whisper(text): 
	return text.lower() 

def greet(func): 
	# storing the function in a variable 
	greeting = func("""Hi, I am created by a function passed as an argument.""") 
	print (greeting) 

greet(shout)
greet(whisper) 

# Python program to illustrate functions 
# Functions can return another function 

def create_adder(x): 
	def adder(y): 
		return x+y 

	return adder 

add_15 = create_adder(15) 

print(add_15(10)) 

# Python code to illustrate
# Decorators basic in Python
def decorator_fun1(func):
	print("Inside decorator")
	def inner(*args,**kwargs):
		print("Inside inner function")
		print("Decorated the function")
		# do operations with func
		func()
	return inner()
@decorator_fun1
def func_to():
	print("Inside actual function")
func_to


# Python code to illustrate 
# Decorators with parameters in Python 

def decorator_fun(func):
	print("Inside decorator") 


def func_to(): 
	print("Inside actual function") 

def inner(*args, **kwargs): 
	print("Inside inner function") 
	print("Decorated the function") 
	func_to()
	return inner 


# another way of using decorators
decorator_fun(func_to)

