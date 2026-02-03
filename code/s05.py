# a product would cost $100, how much tax do we pay?


product = 100 # in dollars
tax_rate = 0.0625
tax = product * tax_rate
print(f'The tax for the product which costs ${product} is ${tax}.') # f-string


def calc_tax():
    product = 100 
    tax_rate = 0.0625
    tax = product * tax_rate
    print(f'The tax for the product which costs ${product} is ${tax}.')