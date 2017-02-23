from decimal import *
getcontext().prec = 100

# Gregory-Leibniz Series
def pi_gls(o):
    q_pi = 0
    for i, n in enumerate(range(1, int(o*2), 2)):
        r = Decimal(1/n)
        q_pi = q_pi+r if i % 2 == 0 else q_pi-r
    return q_pi*4

# first arg = factorial number
# optional second arg = amount of numbers to include in the factorial
def factorial(*args):
    n, i = args[0], args[0] if len(args) != 2 else args[1]
    return 1 if n < 1 or i < 1 else n*factorial(n-1, i-1)

# same usage as above, except this one is not restricted by recursion
def factorial_(*args):
    x, o = 1, args[0] if len(args) < 2 else args[1]
    for i, n in enumerate(range(args[0], 0, -1)):
        if i == o:
            break
        x *= n
    return x

# Nilakantha Series
def pi_ns(o):
    pi = 3
    for i, n in enumerate(range(2, 2+o*2, 2)):
        r = Decimal(4/factorial(n+2, 3))
        pi = pi+r if i % 2 == 0 else pi-r
    return pi

# Binomial Expansion
def e_be(*args):
    n = 10**12 if len(args) < 1 else args[0]
    return (1+(1/Decimal(n)))**n

# Newton's Series
def e_ns(o):
    return sum([Decimal(1/factorial_(i)) for i in range(o)])

print('pi, Gregory-Leibniz Series:', pi_gls(10**6))
print('pi, Nilakantha Series:', pi_ns(10**6))
print('e, Newton\'s Series:', e_ns(10**3))
print('e, Binomial Expansion:', e_be())
