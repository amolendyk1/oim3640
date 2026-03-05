stocks = 'AAPL,MSFT,GOOG,AMZN'
print(stocks[0])

print(stocks[-1])

print(len(stocks))


print(stocks.islower())
print(stocks.isupper())
print(stocks.find('MSFT'))
print(stocks.strip('A'))

def count_vowels(s):
    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
    return count

print(count_vowels('apple'))

print(count_vowels('sky'))
print(count_vowels('ski'))

print('A' in stocks[0])

for stock in stocks:
    if 'A' in stock:
        print(stock)