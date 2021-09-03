Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:22:44) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input("enter any number:")
enter any number:123
>>> b=input("enter any number:")
enter any number:456
>>> a
'123'
>>> b
'456'
>>> a+b
'123456'
>>> a=10
>>> b=20
>>> a+b
30
>>> x=1
>>> y=3
>>> z=x+y
>>> z
4
>>> x*y
3
>>> x/y
0.3333333333333333
>>> _
0.3333333333333333
>>> a=6
>>> _
0.3333333333333333
>>> b=9
>>> b
9
>>> _
9
>>> _+_
18
>>> _-_
0
>>> _=
SyntaxError: invalid syntax
>>> _+_
0
>>> import os
>>> os.getcwt()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    os.getcwt()
AttributeError: module 'os' has no attribute 'getcwt'
>>> os.getcwd()
'C:\\Users\\BHANU VENKATESH\\AppData\\Local\\Programs\\Python\\Python39-32'
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> import sys
>>> sys.platform
'win32'
>>> import platform
>>> platform.python_version()
'3.9.4'