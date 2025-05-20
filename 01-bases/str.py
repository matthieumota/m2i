text = 'Bonjour    '
print(text.upper())
print(len(text))
print(text.strip())
text = text.strip()
print(len(text))
print(text.replace('jour', 'soir'))

print(any(c.isupper() for c in text)) # [True, False, False]
print(all([True, False, True]))

print([c.isupper() for c in text])

for c in text:
    if c.isupper():
        print(True)
        break
    print(False)

import random
print(random.randint(1, 10))
