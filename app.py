def pi(p):
    q_pi = 0
    for i, n in enumerate(range(1, int(p*2), 2)):
        if i % 2 == 0:
            q_pi += 1/n
        else:
            q_pi -= 1/n
    return q_pi*4

print(pi(10**6))
