from decimal import *
getcontext().prec = 100

# Gregory-Leibniz Series
def pi_gls(o=10**6):
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
def pi_ns(o=10**6):
    pi = 3
    for i, n in enumerate(range(2, 2+o*2, 2)):
        r = Decimal(4/factorial(n+2, 3))
        pi = pi+r if i % 2 == 0 else pi-r
    return pi

# Binomial Expansion
def e_be(n=10**12):
    return (1+(1/Decimal(n)))**n

# Another Expansion, small n
def e_se(n=10**-12):
    return (1+Decimal(n))**Decimal(1/n)

# Newton's Series
def e_ns(o=10**3):
    return sum([Decimal(1/factorial_(i)) for i in range(o)])

# Brothers' Formulae
def e_bf(o=7):
    return sum([(2*Decimal(i)+2)/factorial_(2*i+1) for i in range(o)])

# Babylonian Square Root Algorithm
def b_sqrt(n):
    if n == 0:
        return 0
    a = Decimal(n)/2
    b = a+1
    while a != b:
        b = a
        a = (a + n/a)/2
    return a

# Square Root of 2
def pythagoras_constant():
    return b_sqrt(2)

print('pi, Gregory-Leibniz Series:', pi_gls())
print('pi, Nilakantha Series:', pi_ns())
print('e, Newton\'s Series:', e_ns())
print('e, Binomial Expansion:', e_be())
print('e, Small n Expansion:', e_se())
print('e, Brother\'s Formulae:', e_bf())
print('Pythagoras Constant, Babylonian Square Root Algorithm:', pythagoras_constant())
