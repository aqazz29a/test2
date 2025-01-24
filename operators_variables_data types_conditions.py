# C:\Users\user\PycharmProjects\md-automation\.venv\Scripts\python.exe "C:/Program Files/JetBrains/PyCharm Community Edition 2024.3/plugins/python-ce/helpers/pydev/pydevconsole.py" --mode=client --host=127.0.0.1 --port=57911
#
# import sys; print('Python %s on %s' % (sys.version, sys.platform))
# sys.path.extend(['C:\\Users\\user\\PycharmProjects\\PythonProject1'])
#
# PyDev console: starting.
#
# Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
# >>> runfile('C:\\Users\\user\\PycharmProjects\\PythonProject1\\test\\tst1.py', wdir='C:\\Users\\user\\PycharmProjects\\PythonProject1\\test')
# >>> 2+5
# 7
# >>> 10-5
# 5
# >>> 6*7
# 42
# >>> 12345678 * 987654328765432318765
# 12193262318244164938266047670
# >>> 3+5*4
# 23
# >>> (3+5)*4
# 32
# >>> 11111 * 1111111
# 12345554321
# >>> 40 / 8
# 5.0
# >>> 42 // 8
# 5
# >>> 42 % 8
# 2
# >>> 42 / (4+2*(-2))
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>> 239 % 10
# 9
# >>> 239 // 10
# 23
# >>> 2 ** 5
# 32
# >>> 2014 ** 14
# 18064773765607550801425251468864907833685590016
# >>> -42
# -42
# >>> +42
# 42
# >>> +-+42
# -42
# >>> *-42
# Traceback (most recent call last):
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\code.py", line 63, in runsource
#     code = self.compile(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 153, in __call__
#     return _maybe_compile(self.compiler, source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 73, in _maybe_compile
#     return compiler(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 118, in __call__
#     codeob = compile(source, filename, symbol, self.flags, True)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<input>", line 1
# SyntaxError: can't use starred expression here
# >>> print ("test")
# test
# >>> print ("test")
# ... *23
# Traceback (most recent call last):
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\code.py", line 63, in runsource
#     code = self.compile(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 153, in __call__
#     return _maybe_compile(self.compiler, source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 73, in _maybe_compile
#     return compiler(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 118, in __call__
#     codeob = compile(source, filename, symbol, self.flags, True)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<input>", line 2
# SyntaxError: can't use starred expression here
# >>> 5 // 0
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# ZeroDivisionError: integer division or modulo by zero
# >>> 0.5
# 0.5
# >>> 0,5
# (0, 5)
# >>> 0.5 + 0.3
# 0.8
# >>> 5 / 2
# 2.5
# >>> 5 // 2
# 2
# >>> 1/3
# 0.3333333333333333
# >>> 0.3 + 0.3 +0.3
# 0.8999999999999999
# >>> 2 ** 5
# 32
# >>> 9 ** 0.5
# 3.0
# >>> 5e-1
# 0.5
# >>> 1234e-2
# 12.34
# >>> 1234e2
# 123400.0
# >>> 1.2345e-3
# 0.0012345
# >>> 2014.0**14
# 1.806477376560755e+46
# >>> 7/3
# 2.3333333333333335
# >>> 7//3
# 2
# >>> int(2.3)
# 2
# >>> float(5)
# 5.0
# >>> int(2.99)
# 2
# >>> int(-1.6)
# -1
# >>> 9**19 - int(float(9**19))
# 89
# >>> float(9**19)
# 1.350851717672992e+18
# >>> int(float(9**19))
# 1350851717672992000
# >>> 9**19
# 1350851717672992089
# >>> 1350851717672992089 - 1350851717672992000
# 89
# >>> type(7)
# <class 'int'>
# >>> type(7.0)
# <class 'float'>
# >>> a=2
# >>> b=3
# >>> print(a+b)
# 5
# >>> a=6
# >>> print(a+b)
# 9
# >>> b=b+2
# >>> print(b)
# 5
# >>> print(c)
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# NameError: name 'c' is not defined
# >>> a=2
# >>> from traceback import print_tb
# ...
# ... print(a)
# 2
# >>> a=5
# >>> print(a)
# 5
# >>> 2=a
# Traceback (most recent call last):
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\code.py", line 63, in runsource
#     code = self.compile(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 153, in __call__
#     return _maybe_compile(self.compiler, source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 73, in _maybe_compile
#     return compiler(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 118, in __call__
#     codeob = compile(source, filename, symbol, self.flags, True)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<input>", line 1
#     2=a
#     ^
# SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
# >>> a=2
# >>> a+=3
# >>> print(a)
# 5
# >>> print(A)
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# NameError: name 'A' is not defined. Did you mean: 'a'?
# >>> a=2
# >>> a='abacaba'
# >>> type(a)
# <class 'str'>
# >>> a=3
# >>> a
# 3
# >>> a+=4
# >>> a
# 7
# >>> a
# ... a*2
# >>> a
# ... a*2
# >>> a
# ... 2 *a
# >>> a
# ... 2 * a
# >>> a
# 7
# >>> a 2+a
# Traceback (most recent call last):
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\code.py", line 63, in runsource
#     code = self.compile(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 153, in __call__
#     return _maybe_compile(self.compiler, source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 73, in _maybe_compile
#     return compiler(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 118, in __call__
#     codeob = compile(source, filename, symbol, self.flags, True)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<input>", line 1
#     a 2+a
#       ^
# SyntaxError: invalid syntax
# >>> a
# ... 2+a
# >>> print(a) print(2 *a)
# Traceback (most recent call last):
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\code.py", line 63, in runsource
#     code = self.compile(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 153, in __call__
#     return _maybe_compile(self.compiler, source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 73, in _maybe_compile
#     return compiler(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 118, in __call__
#     codeob = compile(source, filename, symbol, self.flags, True)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<input>", line 1
#     print(a) print(2 *a)
#              ^^^^^
# SyntaxError: invalid syntax
# >>> print(a)
# ... print(2 *a)
# 7
# 14
# >>> a
# 7
# >>> a
# ... a*2
# >>> a
# ... 2*a
# >>>
# >>> name = input()
# >? Андрей
# >>> name = input()
# ... print("Hello", name)
# >? Андрей
# Hello Андрей
# >>> name = input('Enter your name')
# ... print("Hello", name)
# Enter your name>? Андрей
# Hello Андрей
# >>> a=int(input())
# ... print(a *2)
# >? 12
# 24
# >>> a= int(intput())
# ... b=int(input())
# ... print(a*b)
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# NameError: name 'intput' is not defined. Did you mean: 'input'?
# >>> 5
# 5
# >>> a= int(intput())
# ... b=int(input())
# ... print(a*b)
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# NameError: name 'intput' is not defined. Did you mean: 'input'?
# >>> a= int(input())
# ... b=int(input())
# ... print(a*b)
# >? 5
# >? 7
# 35
# >>> X = int(input())
# ... Y = int(input())
# ... print(X*60 + Y)
# >? 10
# >? 1
# 601
# >>> x=int(input())
# ... y=int(input())
# ... print(x:y)
# Traceback (most recent call last):
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\code.py", line 63, in runsource
#     code = self.compile(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 153, in __call__
#     return _maybe_compile(self.compiler, source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 73, in _maybe_compile
#     return compiler(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 118, in __call__
#     codeob = compile(source, filename, symbol, self.flags, True)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<input>", line 3
#     print(x:y)
#            ^
# SyntaxError: invalid syntax
# >>> x=int(input())
# ... y=int(input())
# ... print(x, y)
# >? 10
# >? 30
# 10 30
# >>> x=int(input())
# ... y=int(input())
# ... z=x*60+y
# ... print(x, z)
# >? 300
# >? 20
# 300 18020
# >>> x=int(input())
# ... print(x // 60)
# >? 430
# 7
# >>> x=int(input())
# ... print(x // 60)
# ... print(x % 60)
# >? 300
# 5
# 0
# >>> x=int(input())
# ... print(x // 60)
# ... print(x % 60)
# >? 43
# 0
# 43
# >>> x=int(input())
# ... print(x // 60)
# ... print(x % 60)
# >? 330
# 5
# 30
# >>> 5+7
# 12
# >>> 5+7
# 12
# >>> 5<7
# True
# >>> 5==2+3
# True
# >>> a=int(input())
# ... print a > 0
# Traceback (most recent call last):
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\code.py", line 63, in runsource
#     code = self.compile(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 153, in __call__
#     return _maybe_compile(self.compiler, source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 73, in _maybe_compile
#     return compiler(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 118, in __call__
#     codeob = compile(source, filename, symbol, self.flags, True)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<input>", line 2
#     print a > 0
#     ^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# >>> a=int(input())
# ... print(a > 0)
# >? 44
# True
# >>> a=int(input())
# ... print(a > 0)
# >? -4
# False
# >>> a=int(input())
# ... print(a > 0)
# >? 0
# False
# >>> a=int(input())
# ... print(a>=10 and a<100)
# >? 5
# False
# >>> a=int(input())
# ... print(a>=10 and a<100)
# >? 54
# True
# >>> a=int(input())
# ... print(a>=10 and a<100)
# >? 504
# False
# >>> a=int(input())
# ... print(a>=10 and a<100)
# >? 100
# False
# >>> a=int(input())
# ... print(a>=10 and a<100)
# >? 10
# True
# >>> a=int(input())
# ... print(10<=a<100)
# >? 43
# True
# >>> a=int(input())
# ... print(10<=a<100)
# >? -2
# False
# >>> a=int(input())
# ... print(10<=a<100)
# >? 192
# False
# >>> x1, x2, x3 = False, True, False
# ... not x1 or x2 and x3
# >>> not x1 or x2 and x3
# True
# >>> ((not x1) or x2) and x3
# False
# >>> ((a and b) or (not a)) and (not b)
# False
# >>> ((a and b) or (not a) and (not b)))
# Traceback (most recent call last):
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\code.py", line 63, in runsource
#     code = self.compile(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 153, in __call__
#     return _maybe_compile(self.compiler, source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 73, in _maybe_compile
#     return compiler(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 118, in __call__
#     codeob = compile(source, filename, symbol, self.flags, True)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<input>", line 1
#     ((a and b) or (not a) and (not b)))
#                                       ^
# SyntaxError: unmatched ')'
# >>> ((a and b) or ((not a) and (not b)))
# 7
# >>> x = 5
# >>> y = 10
# >>> y > x * x or y >= 2 * x and x < y
# True
# >>> y > x * x or y >= 2 * x and x < y
# True
# >>> print(False or True)
# True
# >>> x=int(input())
# ... y=int(input())
# >? print (y > x * x or y >= 2 * x and x < y)
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'print (y > x * x or y >= 2 * x and x < y)'
# >>> x=int(input())
# ... y=int(input())
# ... print(y > x * x or y >= 2 * x and x < y)
# >? 5
# >? 10
# True
# >>> a=True
# ... b=False
# ... print(a and b ar not a not b)
# Traceback (most recent call last):
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\code.py", line 63, in runsource
#     code = self.compile(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 153, in __call__
#     return _maybe_compile(self.compiler, source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 73, in _maybe_compile
#     return compiler(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 118, in __call__
#     codeob = compile(source, filename, symbol, self.flags, True)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<input>", line 3
#     print(a and b ar not a not b)
#           ^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>> a=True
# ... b=False
# ... print(a and b or not a not b)
# Traceback (most recent call last):
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\code.py", line 63, in runsource
#     code = self.compile(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 153, in __call__
#     return _maybe_compile(self.compiler, source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 73, in _maybe_compile
#     return compiler(source, filename, symbol)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\user\.pyenv\pyenv-win\versions\3.11.2\Lib\codeop.py", line 118, in __call__
#     codeob = compile(source, filename, symbol, self.flags, True)
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<input>", line 3
#     print(a and b or not a not b)
#           ^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>> a=True
# ... b=False
# ... print(((a and b) or (not a) (not b)))
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 3, in <module>
# TypeError: 'bool' object is not callable
# >>> a=True
# ... b=False
# ... print((a and b) or (not a) (not b))
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 3, in <module>
# TypeError: 'bool' object is not callable
# >>> a=True
# ... b=False
# ... print((a and b) or (not a) (not b))
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 3, in <module>
# TypeError: 'bool' object is not callable
