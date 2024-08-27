
# Error and Exception

try:
    a=40/0
except Exception as e:
    print(e)
else:
    print("A value:",a)
finally:
    print("Thank You")
print("--------------------")
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))
print("--------------------")
# Name Error Exception
try:
    print(a)
except NameError as e:
    print("a is not defined")
else:
    print("Ok It's Working")
finally:
    print("Thank You")
print("---------------")
# Zero by Division Error
try:
    a=40/0
except ZeroDivisionError as e:
    print("Dinominator can't Divided by Zero")
else:
    print("Ok It's Working")
finally:
    print("Thank You")
print("---------------")
# Value Error
try:
    a=("Dhivakar")
    print(int(a))
except ValueError as e:
    print("This Value Can't Change Intiger")
else:
    print("Ok It's Working")
finally:
    print("Thank You")
print("---------------")

try:
    a=[24,34,14,22,15]
    print(a[10])
except IndexError as e:
    print("Invalid Index")
else:
    print("Ok It's Working")
finally:
    print("Thank You")
print("---------------")

# File Not Found Exception
try:
    f=open("input.py")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())
finally:
    print("Thank You")
print("--------------------")
# Multiple Exception
try:
    a=10/0
    print(b)
    c=[12,15,24,22]
    print(c[10])
    d="Dhivakar"
    print(int(d))
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
else:
    print("Ok It's Working")
finally:
    print("Thank You")
print("--------------------")
