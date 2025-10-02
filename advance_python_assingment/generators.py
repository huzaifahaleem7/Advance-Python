def next_sqr():
    i = 1
    while True:
        yield i * i
        i += 1
for n in next_sqr():
    if n > 25:
        break
    print(n)