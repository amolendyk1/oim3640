for i in range(1, 4):
    print("Iteration:", i)
    print("Square:", i * i)
    print()

a = 5
b = a 
a = 10
print(b)


x = 10

def f():
    message = "Hello"
    x =
    return x

print(f())
print(x)

# Draw a square 
def draw_square(size):
    for i in range(size):
        # print('🧱' * size)
        for j in range(size):
            print('🧱', end='')
        print()

draw_square(4)
# print('Hi', end = "")
# print('Hello')

# draw a triangle 
create a function to draw a triangle 
🧱           1
🧱🧱         2
🧱🧱🧱      3
🧱🧱🧱🧱   4

I nrow i, how many bricks are there? i + 1
"""
def draw_triangle(rows):
    for i in range(rows):
        print("🧱" * (i + 1))
        
    draw_triangle(4)"""


Draw a triangle like this (size = 5)
    # 4 spaces + 1 # = 5 5 - 0 - 1 = 4
   ## 3 spaces + 2 # = 5 5 - 1- 1 = 3
  ### 2 spaces + 3 # = 5 5 - 2 - 1 = 2
 #### 1 space + 4 # = 5 5 - 3 - 1 = 1 
 
in row i how many spaces are there? size - i - 1
how many #s are there? i + 1
# create a function to draw a pyramid   