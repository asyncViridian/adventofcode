### PART 1
# read the input
f = open('input/day18.txt', 'r')
input = [x.strip() for x in f]
f.close()
def parseParentheses(s):
    output = []
    levels = 0
    i = 0
    while i<len(s):
        if s[i]=='(':
            levels += 1
            if levels==1:
                output.append(s[:i])
                s = s[i:]
                i = 0
        elif s[i]==')':
            levels -= 1
            if levels==0:
                output.append(s[:i+1])
                s = s[i+1:]
                i = 0
        i += 1
    if s!='':
        output.append(s)
    return output
def evaluate(expression):
    # parse out parentheses
    expression = parseParentheses(expression)
    if len(expression)!=1:
        expression = [(evaluate(e[1:-1]) if e[0]=='(' else e) for e in expression if len(e)!=0]
    expression = ''.join(expression)
    expression = expression.split(' ')
    # evaluate from left to right
    value = int(expression[0])
    operation_i = None # [+, *]
    for i in range(1, len(expression)):
        if expression[i]=='+':
            operation_i=0
        elif expression[i]=='*':
            operation_i=1
        else:
            # perform the operation on the value
            if operation_i==0:
                value += int(expression[i])
            elif operation_i==1:
                value *= int(expression[i])
            else:
                raise ValueError('something is wrong')
            operation_i = None
    return str(value)
print(sum([int(evaluate(l)) for l in input]))

### PART 2
def evaluate(expression):
    # parse out parentheses
    expression = parseParentheses(expression)
    if len(expression)!=1:
        expression = [(evaluate(e[1:-1]) if e[0]=='(' else e) for e in expression if len(e)!=0]
    expression = ''.join(expression)
    expression = expression.split(' ')
    # compute addition first
    while len([e for e in expression if e=='+']):
        i = expression.index('+')
        expression = expression[:i-1] + [str(int(expression[i-1]) + int(expression[i+1]))] + expression[i+2:]
    # evaluate from left to right
    value = int(expression[0])
    operation_i = None # [*]
    for i in range(1, len(expression)):
        if expression[i]=='*':
            operation_i=0
        else:
            # perform the operation on the value
            if operation_i==0:
                value *= int(expression[i])
            else:
                raise ValueError('something is wrong')
            operation_i = None
    return str(value)
print(sum([int(evaluate(l)) for l in input]))
