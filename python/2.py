# prints sum of all even-valued fibonacci numbers up to 4000000

s, a, b = (0, 1, 2)

while a <= 4000000:
    if a % 2 == 0:
        s += a
    a, b = b, a + b

print s
