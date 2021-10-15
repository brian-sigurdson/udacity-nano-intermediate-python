"""Write a function that prints a profile, given values."""


def create_profile(given_name, *surnames, **details):
    print(given_name, *surnames)
    # print(given_name, " ".join(surnames))
    for key, value in details.items():
        print(key, value, sep=": ")


if __name__ == '__main__':
    create_profile("Sam")
    create_profile("Martin", "Luther", "King", "Jr.", born=1929, died=1968)
    create_profile("Sebastian", "Thrun", cofounded="Udacity",
                   experience="Stanford Professor")

# mylist = ["first", "second", "third", "forth"]
# result = map(len, mylist)
# # print(tuple(result))
#
# for elem in result:
#     print(elem)


# rolodex = ["amy", "brian"]
# def is_member(name):
#     return name in rolodex
#
# names = ["amy", "brian", "bob", "sue"]
# result = filter(is_member, names)
# print(list(result))