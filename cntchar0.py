from collections import defaultdict
from collections import Counter

def count_characters(string):
    count_dict = defaultdict(int)
    for c in string:
        count_dict[c] += 1

    print(count_dict)

count_characters("Dynasty")

print(Counter("Dynasty"))
