Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add_numbers(a,b):
	print(a+b)

	
>>> add_numbers(1,2)
3
>>> add_numbers(1,"shekar")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    add_numbers(1,"shekar")
  File "<pyshell#2>", line 2, in add_numbers
    print(a+b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> add_numbers("Shekar","gadamoni")
Shekargadamoni
>>> add_numbers()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    add_numbers()
TypeError: add_numbers() missing 2 required positional arguments: 'a' and 'b'
>>> def add_num(a:int,b:int) ->int:
	return a+b

>>> add_num(1,2)
3
>>> add_num(23,"shekar)
	
SyntaxError: EOL while scanning string literal
>>> print('Hello'=="Hello"=="""Hello""")
True
>>> 
