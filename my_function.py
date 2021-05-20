def yoda():
    print("You must unlearn what you have learned")


def mini(a, b, c):              # mini
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


def box(h, w):                  # box
    for i in range(h):
        print("o"*w)


def find(list1, key):                # find
    for i in range(len(list1)):
        if list1[i] == key:
            print(f"Found{key} at position {i+1}")


def fizzbuzz(endpoint):                 # fizzbuzz
    for num in range(1, endpoint+1):
        if num % 15 == 0:
            print("fizzbuzz")
        elif num % 5 == 0:
            print("buzz")
        elif num % 3 == 0:
            print("fizz")
        else:
            print(num)


def fibonacci(num):                 # fibonacci
    x, y = -1, 1
    for i in range(num):
        z = x+y
        x = y
        y = z
        print(f"{z:>30,}")
