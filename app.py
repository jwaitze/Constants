# Gregory-Leibniz Series
def pi_gls(p):
    q_pi = 0
    for i, n in enumerate(range(1, int(p*2), 2)):
        if i % 2 == 0:
            q_pi += 1/n
        else:
            q_pi -= 1/n
    return q_pi*4

# first arg = factorial number
# optional second arg = amount of numbers to include in the factorial
def factorial(*args):
    n, i = args[0], 1 if len(args) != 2 else args[1]
    return 1 if n < 1 or i < 1 else n*factorial(n-1, i-1)

# Nilakantha Series
def pi_ns(p):
    pi = 3
    for i, n in enumerate(range(2, 2+p*2, 2)):
        if i % 2 == 0:
            pi += 4/factorial(n+2, 3)
        else:
            pi -= 4/factorial(n+2, 3)
    return pi

print(pi_gls(10**6))
print(pi_ns(10**6))
