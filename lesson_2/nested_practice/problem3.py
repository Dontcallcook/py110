munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for i, member in enumerate(munsters):
    print(f"{list(munsters.keys())[i]} "
    f"is a {munsters[member]['age']}-year-old "
    f"{munsters[member]['gender']}.")