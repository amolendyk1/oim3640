# fixed conversion rates
- USD_to_EUR = 0.848 
- USD_to_GBP = 0.739
- USD_to_INR = 90.902
- USD_to_AUD = 1.409
- USD_to_CAD = 1.369
- USD_to_SGD = 1.265
- USD_to_CHF = 0.773
- USD_to_MYR = 3.891
- USD_to_JPY = 156.492
- USD_to_CNY = 6.869

# conversion rate equation from USD
def currency_conversion_from_USD(amount, conversion_rate):
    currency = amount * conversion_rate
    return currency

# Test 
print(currency_conversion_from_USD(100, USD_to_EUR)) # should return 84.8

