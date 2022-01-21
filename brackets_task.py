def brackets_task_stack(brackets):
    stack = []
    good_sequence = True
    brackets_compliance = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    for bracket in brackets:
        if bracket in '([{':
            stack.append(bracket)

        if bracket in ')]}' and stack:
            prev = stack.pop()
            if prev == brackets_compliance[bracket]:
                continue
            else:
                good_sequence = False
                break
        if bracket in ')]}' and not stack:
            good_sequence = False
            break
    if good_sequence and len(stack) == 0:
        return 'Good Sequence'
    else:
        return 'Bad Sequence'


def brackets_recursion(brackets):
    pairs = ['()', '{}', '[]']
    if any(pair in brackets for pair in pairs):
        for br in pairs:
            brackets = brackets.replace(br, '')
        if brackets:
            return brackets_recursion(brackets)
        else:
            return "Good"
    return "Bad"


brackets_lists = [
    "{{([([])])}}(){[]}",
    "{{([])}}",
    "{}",
    "(())",
    "}{",
    "{[}]",
    ")("
]


for brackets in brackets_lists:
    print(f'{brackets}: {brackets_task_stack(brackets)}')
    print(f'{brackets}:{brackets_recursion(brackets)}')
