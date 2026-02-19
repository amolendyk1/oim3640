score = int(input("Enter your score: "))

if score >= 90:
    print("A")
elif score >= 60:
    print('Pass')
else:
    print("Fail")

def mystery(x):
    if x > 0:
        return "positive"
    print("done")

result = mystery(5)
print(result)

x = 15
y = x > 10 and x < 20
print(type(y))



def check(n):
    if n % 2 == 0 and n % 3 == 0:
        print(f"{n} is divisible by 2 and 3")
    elif n % 2 == 0:
        print(f"{n} is divisible by 2")
    else:
        print(f"{n} is not divisible by 2 or 3")

check(8)
check(6)