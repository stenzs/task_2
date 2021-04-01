s = input('введите текст: ')
text = input('Введите скобки для проверки: ')
inp = str()
inp2 = str()
for i in text:
    if i in '()':
        inp += '('
        inp2 += ')'
for i in text:
    if i in '[]':
        inp += '['
        inp2 += ']'
for i in text:
    if i in '{}':
        inp += '{'
        inp2 += '}'
for i in text:
    if i in '<>':
        inp += '<'
        inp2 += '>'
stack = []
stack1 = []
check = True
error = 'None'
bracket = 'None'
num = 0
open_bracket = ()
for i in s:
    if i in inp:
        stack.append(i)
        stack1.append(num)
        num += 1
    elif i in inp2:
        if not stack:
            check = False
            error = i, num
            break
        open_bracket = stack.pop()
        if open_bracket == '(' and i == ')':
            stack1.pop()
            num += 1
            continue
        if open_bracket == '[' and i == ']':
            stack1.pop()
            num += 1
            continue
        if open_bracket == '{' and i == '}':
            stack1.pop()
            num += 1
            continue
        if open_bracket == '<' and i == '>':
            stack1.pop()
            num += 1
            continue
        check = False
        error = i, num
        bracket = open_bracket, stack1[-1]
        print(f"{'False'}, {error}, {bracket}")
        raise SystemExit
    else:
        num += 1
if len(stack) != 0:
    bracket = stack[0], stack1[0]
if check and len(stack) == 0:
    print(f"{'True'}, {error}, {bracket}")
else:
    print(f"{'False'}, {error}, {bracket}")