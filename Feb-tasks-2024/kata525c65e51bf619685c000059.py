def cakes(recipe, ingredients):
    min_ = float('inf')
    for ingredient in recipe:
        try:
            min_ = min(min_, ingredients[ingredient] // recipe[ingredient])
        except:
            return 0
    return min_

print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))