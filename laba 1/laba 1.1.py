j = str("ab")
s = str("aabbccd")
count = 0
for wor in s:
    if wor in j:
        count += 1
print(count)
