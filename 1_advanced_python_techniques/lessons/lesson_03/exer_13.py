# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)

map_list = ["apple", "orange", "pear"]


def to_upper(word):
    return word.upper()


def first_two(word):
    return word[:2]


def my_reversed(word):
    return word[::-1]


a = map(len, map_list)
b = map(str.upper, map_list)
c = map(my_reversed, map_list)
d = map(first_two, map_list)

print(list(a))
print(list(b))
print(list(c))
print(list(d))


# Practice with filter
# Fill out the rest of the filter functions.
# You can define additional functions if you need to.
# (a) range(100) => (0, 3, 6, 9, ...)  (div by 3)
# (b) range(100) => (0, 5, 10, 15, ...)  (div by 5)
# (c) range(100) => (0, 15, 30, 45, ...)  (div by 15)
# (d) range(100) => (1, 2, 4, 7, 8, 11, 13, 14, 16, 17, ...)  (not div by 3 and not div by 5)

def num_div_by_x(num, x):
    if num < x:
        return False
    else:
        return num % x == 0


def div_by_3(num):
    return num_div_by_x(num, 3)


def div_by_5(num):
    return num_div_by_x(num, 5)


def div_by_15(num):
    return num_div_by_x(num, 15)


def not_div_3_not_div_5(num):
    return not div_by_3(num) and not div_by_5(num)


a = filter(div_by_3, range(100))
b = filter(div_by_5, range(100))
c = filter(div_by_15, range(100))
d = filter(not_div_3_not_div_5, range(100))

print(list(a))
print(list(b))
print(list(c))
print(list(d))


# use lambdas
a = filter(lambda x: x % 3 == 0, range(100))
b = filter(lambda x: x % 5 == 0, range(100))
c = filter(lambda x: x % 15 == 0, range(100))
d = filter(lambda x: x % 3 != 0 and x % 5 != 0, range(100))
