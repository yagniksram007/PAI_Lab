#pip install fuzzywuzzy

from fuzzywuzzy import fuzz

def fuzzy_union(set1, set2):
    union_result = max(set1, set2)
    return union_result

def fuzzy_intersection(set1, set2):
    intersection_result = min(set1, set2)
    return intersection_result

# Example fuzzy sets
set_a = fuzz.token_set_ratio("apple", "pineapple") / 100.0
set_b = fuzz.token_set_ratio("banana", "orange") / 100.0

# Demonstrate union and intersection
union_result = fuzzy_union(set_a, set_b)
intersection_result = fuzzy_intersection(set_a, set_b)

print(f"Fuzzy Set A: {set_a}")
print(f"Fuzzy Set B: {set_b}")
print(f"Union: {union_result}")
print(f"Intersection: {intersection_result}")