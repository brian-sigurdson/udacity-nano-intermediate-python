hello = "Hello, world!"

a = hello[0]
b = hello[-2]
c = hello[1:5]
d = hello[7:]
e = hello[1] + hello[2] # etc...
f = hello[::-1]

print(f)

def make_palindrome(s):
    # eg. s = abcd
    # eg. s = abcde

    s_rev = s[::-1]
    return s + s_rev


print(make_palindrome("abcd"))


def add_layer(triangle):


