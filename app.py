# Gregory-Leibniz Series
def pi_gls(p):
    q_pi = 0
    for i, n in enumerate(range(1, int(p*2), 2)):
        if i % 2 == 0:
            q_pi += 1/n
        else:
            q_pi -= 1/n
    return q_pi*4

# Nilakantha Series
def pi_ns(p):
    def f(x):
        return x*(x+1)*(x+2)
    pi = 3
    for i, n in enumerate(range(2, 2+p*2, 2)):
        if i % 2 == 0:
            pi += 4/f(n)
        else:
            pi -= 4/f(n)
    return pi

print(pi_gls(10**6))
print(pi_ns(10**6))
