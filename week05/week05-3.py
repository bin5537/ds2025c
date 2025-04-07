def is_vaild_brackets(expression: str) -> bool:
    stack = []

    brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for letter in expression:
        if letter in brackets.values():
            stack.append(letter)
        elif letter in brackets.keys():
            if not stack or brackets[letter] != stack.pop():
                return False
    return not stack

print(is_vaild_brackets("(2+3)"))
print(is_vaild_brackets("(2+(3*9))"))
print(is_vaild_brackets("(2+{4/5])"))
print(is_vaild_brackets("[2 + {3 * 5(5+5)}]"))
