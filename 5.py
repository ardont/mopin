'''
result = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s += s[-3:]
    else:
        s += bin(n%3 * 3)[2:]
    if int(s, 2) > 151:
        result.append(int(s,2))
print(min(result))
'''

a = []
for x in range(10, 1001):
    i = int(bin(x)[3:], 2)
    if x - i not in a:
        a.append(x-i)
print(len(a))