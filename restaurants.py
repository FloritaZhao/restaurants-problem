from collections import defaultdict

def most_varied_visitor(visits):
    # Write your solution here!
    # import defaultdict(set)
    most_visitor = defaultdict(set)

    for restaurant, people in visits.items():
        for person in people:
            most_visitor[person].add(restaurant)

    print(type(most_visitor))

    max_count = 0
    most_person = None
    for person, restaurant in most_visitor.items():
        if len(restaurant) > max_count:
            max_count = len(restaurant)
            most_person = person
    
    return most_person




visits_1 = {
    "Spicy City" : ["Eliza"],
    "La Especial Norte" : ["Eliza"],
    "Sushi Kashiba": ["Xinting"],
}

most_varied_visitor(visits_1)
print(most_varied_visitor(visits_1))

assert most_varied_visitor(visits_1) == "Eliza"

visits_2 = {
    "Spicy City" : ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}


assert most_varied_visitor(visits_2) == "Auberon"

visits_3 = {
    "Spicy City" : ["Elora", "Elora", "Elora"],
}
assert most_varied_visitor(visits_3) == "Elora"
print("All tests passed! If time remains, discuss time/space complexity")