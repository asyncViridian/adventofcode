### PART 1
# read the input
f = open('input/day19.txt', 'r')
input = [x.strip() for x in f]
f.close()
input_rules = input[:input.index('')]
input_strings = input[input.index('')+1:]
# parse the list of rules
rules = {}
for r in input_rules:
    rs = r.split(': ')
    rules[rs[0]] = [e.strip('"').split(' ') for e in rs[1].split(' | ')]
# build the list of all strings that each rule can produce
# (since we are guaranteed a finite potential string count :) )
rule_strings = {}
while len(rules) > 0:
    rules_update = {}
    for r in rules:
        if len(rules[r])==1 and len(rules[r][0])==1 and (not rules[r][0][0].isdecimal()):
            # check if the rule matches a single character
            rule_strings[r] = [rules[r][0][0]]
        elif all([all([(e in rule_strings) for e in c]) for c in rules[r]]):
            # the rule can be compressed into a set of potential literal strings
            compressions = []
            for breakdown in rules[r]:
                b_compressions = rule_strings[breakdown[0]]
                for ref in breakdown[1:]:
                    b_compressions_update = []
                    for s in rule_strings[ref]:
                        b_compressions_update += [e+s for e in b_compressions]
                    b_compressions = b_compressions_update
                compressions += b_compressions
            rule_strings[r] = compressions
        else:
            rules_update[r] = rules[r]
    rules = rules_update
# compress the list of strings in the rule_strings
for r in rule_strings:
    rule_strings[r] = list(set(rule_strings[r]))
# finally, count how many messages completely match rule 0
print(sum([1 if (s in rule_strings['0']) else 0 for s in input_strings]))

### PART 2
# the puzzle input that I have DEFINITELY has the line '0: 8 11' and so does the sample input
# the problem statement itself states a constant and defined overwriting to the rule set...
#   8: 42 | 42 8
#   11: 42 31 | 42 11 31
def is_valid_8(s):
    for rs in rule_strings['42']:
        if s==rs:
            return True
        if len(s)>len(rs) and s[:len(rs)]==rs and is_valid_8(s[len(rs):]):
            return True
    return False
def is_valid_11(s):
    for rs1 in rule_strings['42']:
        for rs2 in rule_strings['31']:
            if s==rs1+rs2:
                return True
            if len(s)>len(rs1)+len(rs2) and s[:len(rs1)]==rs1 and s[-len(rs2):]==rs2 and is_valid_11(s[len(rs1):][:-len(rs2)]):
                return True
    return False
# count up how many are valid :)
results_match = []
for s in input_strings:
    for i in range(len(s)):
        if is_valid_8(s[:i]) and is_valid_11(s[i:]):
            results_match.append(s)
print(len(set(results_match)))
