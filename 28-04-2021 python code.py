Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:22:44) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #hello
>>> print("hello, world"*10)
hello, worldhello, worldhello, worldhello, worldhello, worldhello, worldhello, worldhello, worldhello, worldhello, world
>>> print("hello, world"*10,"\n")
hello, worldhello, worldhello, worldhello, worldhello, worldhello, worldhello, worldhello, worldhello, worldhello, world 

>>> print("hello,world"*10,sep"__")
SyntaxError: invalid syntax
>>> print("hello,world"*10,sep'__')
SyntaxError: invalid syntax
>>> print("hello,world",sep"&")
SyntaxError: invalid syntax
>>> print("hello,world"*10,sep="&")
hello,worldhello,worldhello,worldhello,worldhello,worldhello,worldhello,worldhello,worldhello,worldhello,world
>>> print("hello,world",sep="&")
hello,world
>>> print("hello,world hello,world",sep="&")
hello,world hello,world
>>> print(23434234,sep="&")
23434234
>>> print(1,2,3,4,5,6,7,8,9,sep="&")
1&2&3&4&5&6&7&8&9
>>> print(1,2,3,4,5,6,7,8,9,"\n")
1 2 3 4 5 6 7 8 9 

>>> 