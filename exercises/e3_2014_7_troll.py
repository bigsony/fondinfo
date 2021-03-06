def troll(text: str) -> str:
    output = ''
    trolling = False
    for c in text:
        if c == '*':
            trolling = not trolling
        elif 'a' <= c <= 'z' and trolling:
            output += c.upper()
        else:
            output += c
    return output

with open('troll.out.txt', 'w') as out:
    with open('troll.txt', 'r') as f:
        for line in f:
            res = troll(line)
            print(res, file=out, end='')
