generator = (i ** 2 for i in range(10) if i % 2 == 0)

for n in generator:
    print(n)
