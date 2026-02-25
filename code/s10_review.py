count = 0

for letter in 'mississippi':
    if letter == 's':
        count += 1
print(count)


n = 6
while n > 0:
    print(n)
    n = n - 2

n = 6
while n >= 0:
    print(n)
    n = n - 2

n = 6
while n != 0:
    print(n)
    n = n - 2

def uses_any(word, letters):
    for letter in word:
        if letter in letters:
            return True
        else:
            return False

print(uses_any('hello', 'xyz'))
print(uses_any('hello', 'aeiou'))

def version_a(word):
    for letter in word:
        if letter in 'aeiou':
            print(letter)
    print('Done')

(version_a('hello'))

def version_b(word):
    for letter in word:
        if letter in 'aeiou':
            return(letter)
    return 'None found'

(version_b('hello'))


version_a ('nbc')
print('---')
print(version_b)