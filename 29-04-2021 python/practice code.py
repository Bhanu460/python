Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:22:44) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(1,2,3,4,5,6,7,8,9,end="\n")
1 2 3 4 5 6 7 8 9
>>> print(1,2,3,4,5,6,7,8,9,sep='&',end='\n')
1&2&3&4&5&6&7&8&9
>>> print('deep learning is the subset of 'mechine' learning')
SyntaxError: invalid syntax
>>> print('deep learning is the subset of \'mechine\' learning)
      
SyntaxError: EOL while scanning string literal
>>> print('deep learning is the subset of \'meching\' learning')
deep learning is the subset of 'meching' learning
>>> print("deep learning is the subset of """meching""" learning")
SyntaxError: invalid syntax
>>> print("deep learning is the subset of \"""mechine\""" learning")
deep learning is the subset of "mechine" learning
>>> print("welcome", "to", "the", "python", "coding")
welcome to the python coding
>>> print("welcome to the \
python coding")
welcome to the python coding
>>> print("welcome to the python
      
SyntaxError: EOL while scanning string literal
>>> print("""python is trendy
programming in the industry.it supports
all latest environments in the industry""")
python is trendy
programming in the industry.it supports
all latest environments in the industry
>>> print("python is trendy
      
SyntaxError: EOL while scanning string literal
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> keywords
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    keywords
NameError: name 'keywords' is not defined
>>> print(1,2,3,4,5,5,6,7,8,9,sep="\t")
1	2	3	4	5	5	6	7	8	9
>>> print(1,2,3,4,5,6,7,8,9,sep="\n")
1
2
3
4
5
6
7
8
9
>>> print(1,2,3,4,5,6,7,8,9sep="\n",end="complet")
SyntaxError: invalid syntax
>>> print(1,2,3,4,5,6,7,8,9,sep="\n",end="complet")
1
2
3
4
5
6
7
8
9complet
>>> print(1,2,3,4,5,6,7,8,9,sep="\n",sep"__",end="complet")
SyntaxError: positional argument follows keyword argument
>>> 