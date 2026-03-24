# -----------------------------
# Ally's Top 10 Currency Converter
# -----------------------------

# Conversion rates from USD
rates = { 
    "japan": 156.492,
    "london": 0.739,
    "france": 0.848,
    "netherlands": 0.848,
    "china": 6.849,
    "costa rica": 520.0,
    "greece": 0.848,
    "germany": 0.848,
    "united states": 1.0,
    "italy": 0.848
    }

# Tax Rates
tax = { 
    "japan": 0.10,
    "london": 0.20,
    "france": 0.20,
    "netherlands": 0.21,
    "china": 0.13,
    "costa rica": 0.13,
    "greece": 0.24,
    "germany": 0.19,
    "united states": 0.07,
    "italy": 0.22
}

# Functions
def convert(amount, country):
    """Return USD converted to the target country's currency."""
    return amount * rates[country]

def add_tax(amount, country):
    """Return amount after applying that country's tax rate."""
    return amount * (1 + tax[country])

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def get_country():
    """Return a valid country using a loop + conditionals."""
    while True:
        c = input("Country: ").lower()
        if c in rates:
            return c
        print("Not in Ally's Top 10. Try again.")


# -----------------------------
# Menu
# -----------------------------

def convert_only():
    amount = get_number("USD amount: ")
    country = get_country()
    result = convert(amount, country)
    print(f"{amount} USD → {result:.2f} ({country})")

def convert_with_tax():
    amount = get_number("USD amount (already including US tax): ")
    country = get_country()

    # Step 1: amount is already with US tax, so don't add US tax again
    usd_with_tax = amount

    # Step 2: convert that taxed USD amount to target currency
    converted = convert(usd_with_tax, country)

    # Step 3: apply target country's tax
    final = add_tax(converted, country)

    print(f"Final price in {country}: {final:.2f}")


def list_countries():
    print("\nSupported countries:")
    for c in rates:
        print("-", c.title())

# -----------------------------
# Loop
# -----------------------------

def menu():
    print("\n--- Ally's Currency Converter ---")
    print("1) Convert USD → currency")
    print("2) Convert USD → currency (with tax)")
    print("3) List countries")
    print("4) Quit")

def main():
    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            convert_only()
        elif choice == "2":
            convert_with_tax()
        elif choice == "3":
            list_countries()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

main()
