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

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b
    print()

fib(1000)
