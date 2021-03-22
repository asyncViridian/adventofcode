import math

### PART 1
# read the input
f = open('input/day21.txt', 'r')
input = [x.strip() for x in f]
f.close()
# parse input into foods, allergens listings
input = [i.split(' (contains ') for i in input]
input = [(e[0].strip().split(), [a.strip() for a in e[1][:-1].split(',')]) for e in input]
# get all of the raw foods and allergens
foods = list(set([a for b in input for a in b[0]]))
allergens = list(set([a for b in input for a in b[1]]))
# filter down which foods each allergen could be!
# initialize the set of foods per allergen
allergen_map = dict([(a, foods) for a in allergens])
# now filter them down
for i in input:
    for i_food in i[1]:
        allergen_map[i_food] = [e for e in allergen_map[i_food] if e in i[0]]
# figure out which foods could not possibly be an allergen
nonallergen_foods = [e for e in foods if all([(e not in a) for a in allergen_map.values()])]
# figure out how many times the nonallergens show up, total
print(len([a for b in input for a in b[0] if a in nonallergen_foods]))

### PART 2
# canonical-ify the list of allergens
canonical_allergens = {}
while len(canonical_allergens) != len(allergens):
    updated_allergen_map = {}
    for a in allergen_map:
        if len(allergen_map[a])==1:
            canonical_allergens[a] = allergen_map[a][0]
        else:
            updated_allergen_map[a] = [e for e in allergen_map[a] if e not in canonical_allergens.values()]
    allergen_map = updated_allergen_map
# print out the canonical list, sorted by english name alphabetically
print(','.join([canonical_allergens[a] for a in sorted(canonical_allergens)]))
