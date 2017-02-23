# Gregory-Leibniz Series
def pi_gls(o):
    q_pi = 0
    for i, n in enumerate(range(1, int(o*2), 2)):
        if i % 2 == 0:
            q_pi += 1/n
        else:
            q_pi -= 1/n
    return q_pi*4

# first arg = factorial number
# optional second arg = amount of numbers to include in the factorial
def factorial(*args):
    n, i = args[0], args[0] if len(args) != 2 else args[1]
    return 1 if n < 1 or i < 1 else n*factorial(n-1, i-1)

# Nilakantha Series
def pi_ns(o):
    pi = 3
    for i, n in enumerate(range(2, 2+o*2, 2)):
        if i % 2 == 0:
            pi += 4/factorial(n+2, 3)
        else:
            pi -= 4/factorial(n+2, 3)
    return pi

# Newton's Series
def e_ns(o):
    return sum([1/factorial(i) for i in range(o)])

#print(pi_gls(10**6))
#print(pi_ns(10**6))
print(e_ns(100))
