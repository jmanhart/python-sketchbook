# x = int(input("Please enter an integer: "))
#
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# words = ['cat', 'window', 'defensetrate']

# for w in words:
#     print(w, len(w))

# for w in words[:]:
#     if len(w) > 6:
#         words.insert(0,w)
# print words



# for i in range(5, 10, 2, ):
#     print i


# a = ['Mary', 'had', 'a', 'little' , 'lamb']
#
# for i in range(len(a)):
#     print(i, a[i])


# for n in range(2, 100):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')


# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found a number", num)



# Functions

# def fib(n):
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a)
#         a, b = b, a+b
#     print()
#
# fib(10)


# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result
#
# f100 = fib2(100)
#
# print f100

#
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')



# i = 5
#
# def f(arg=i):
#     print(arg)
#
# i = 6
#
# f()


# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(2))


# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
#
# print f(3)



# def parrot(voltage, state='a stiff', action='voom', type='Swedish'):
#     print("-- This parrot wouldn't", action)


# def function(a):
#     pass
#
# print function(0, a=0)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you habe any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
