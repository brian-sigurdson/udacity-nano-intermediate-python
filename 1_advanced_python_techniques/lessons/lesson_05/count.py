import collections


def count_unique_words(the_filename):

    with open(the_filename, 'r') as infile:
        hamlet_text = infile.read()

    hamlet_list = hamlet_text.split()
    return collections.Counter(hamlet_list)


filename = "hamlet.txt"
hamlet_collection = count_unique_words(filename)
print(hamlet_collection.most_common(10))
