### PART 1
# read the input
f = open('input/day16.txt', 'r')
input = [x.strip() for x in f]
f.close()
# collect the ticket field data from input
unsure_ticket_fields = {}
my_ticket = []
other_tickets = []
section_i = 0 # ['fields', 'myticket', 'othertickets']
for line in input:
    if line=='':
        section_i += 1
    elif section_i==0:
        fields = line.split(': ')
        valid_values = [e for e in fields[1].split(' or ')]
        valid_values = [e.split('-') for e in valid_values]
        valid_values = [(int(e[0]), int(e[1])) for e in valid_values]
        unsure_ticket_fields[fields[0]] = valid_values
    elif section_i==1:
        if line!='your ticket:':
            my_ticket = [int(e) for e in line.split(',')]
    else:
        if line!='nearby tickets:':
            other_tickets.append([int(e) for e in line.split(',')])
# return the sum of invalid values for a ticket
def ticketScanErrorRateAnyField(rules, ticket):
    scan_error_rate = 0
    invalid = False
    for i in range(len(ticket)):
        # compare against ANY field
        rules_invalid = 0
        for ruleranges in rules.values():
            if not any([(ticket[i]>=e[0] and ticket[i]<=e[1]) for e in ruleranges]):
                rules_invalid += 1
        if rules_invalid == len(rules):
            scan_error_rate += ticket[i]
            invalid = True
    return invalid, scan_error_rate
print(sum([ticketScanErrorRateAnyField(unsure_ticket_fields, e)[1] for e in other_tickets]))

### PART 2
# discard the tickets that are invalid entirely
other_tickets = [e for e in other_tickets if not ticketScanErrorRateAnyField(unsure_ticket_fields, e)[0]]
# assign all the preliminary columns
potential_ticket_fields = {}
for fname in unsure_ticket_fields:
    assignees = []
    for i in range(len(my_ticket)):
        values = [f[i] for f in other_tickets]
        if all([any([(v>=r[0] and v<=r[1]) for r in unsure_ticket_fields[fname]]) for v in values]):
            # this column could fit
            assignees.append(i)
    potential_ticket_fields[fname] = assignees
# eliminate the preliminary columns
ticket_fields = {}
while len(potential_ticket_fields)>0:
    # find one that is unique
    assigned = None
    for fname in potential_ticket_fields:
        if len(potential_ticket_fields[fname])==1:
            assigned = fname
    if assigned==None:
        raise ValueError('impossible')
    else:
        # assign it
        assigned_col = potential_ticket_fields[assigned][0]
        ticket_fields[assigned] = assigned_col
        potential_ticket_fields.pop(assigned)
        # and remove it from all competitors
        for fname in potential_ticket_fields:
            potential_ticket_fields[fname] = [e for e in potential_ticket_fields[fname] if e!=assigned_col]
# FINALLY, find the six fields that start with 'departure' and multiply them together
fields_to_multiply = [ticket_fields[f] for f in ticket_fields if f.startswith('departure')]
product_parts = [my_ticket[f] for f in fields_to_multiply]
product = 1
for v in product_parts:
    product *= v
print(product)
