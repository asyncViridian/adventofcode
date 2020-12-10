### PART 1
# read the input
f = open('input/day04.txt', 'r')
input = [x.strip() for x in f]
f.close()
# process it into a dict format
passports = ' '.join([(x if (x != '') else '\t') for x in input]).split('\t')
passports = [x.strip().split() for x in passports]
passports = [[e.split(':') for e in p] for p in passports]
passports = [dict(zip([e[0] for e in p], [e[1] for e in p])) for p in passports]
# check validity of a passport
def passportIsValid(p):
    # 'cid' not required
    required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    return all([(field in p) for field in required_fields])
print(sum([(1 if passportIsValid(p) else 0) for p in passports]))

### PART 2
# stricter check for validity of a passport
def passportIsValidStricter(p):
    # 'cid' not required
    required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    if not all([(field in p) for field in required_fields]):
        return False
    # do byr check: >= 1920, <= 2002
    if (int(p['byr']) < 1920) or (int(p['byr']) > 2002):
        return False
    # do iyr check: >= 2010, <= 2020
    if (int(p['iyr']) < 2010) or (int(p['iyr']) > 2020):
        return False
    # do eyr check: >= 2020, <= 2030
    if (int(p['eyr']) < 2020) or (int(p['eyr']) > 2030):
        return False
    # do hgt check: if cm 150->193; if in 59->76
    if p['hgt'][-2:] not in ['cm', 'in']:
        return False
    if (p['hgt'][-2:] == 'cm') and ((int(p['hgt'][:-2]) < 150) or (int(p['hgt'][:-2]) > 193)):
        return False
    if (p['hgt'][-2:] == 'in') and ((int(p['hgt'][:-2]) < 59) or (int(p['hgt'][:-2]) > 76)):
        return False
    # do hcl check: a # followed by lowercase hexadecimal
    if (p['hcl'][0] != '#'):
        return False
    if (len(p['hcl'][1:]) != 6) or any([(c not in list('abcdef0123456789')) for c in p['hcl'][1:]]):
        return False
    # do ecl check: must be in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    # do pid check: nine digit number including leading zeroes
    if len(p['pid']) != 9:
        return False
    if any([(c not in list('0123456789')) for c in p['pid']]):
        return False
    return True
print(sum([(1 if passportIsValidStricter(p) else 0) for p in passports]))
