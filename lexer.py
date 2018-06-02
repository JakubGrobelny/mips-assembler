def split_line(line: str):
    token = ""
    tokens = []
    for c in line:
        if c.isspace() or c == ',':
            if token != "":
                tokens.append(token)
                token = ""
        else:
            token += c
    if token != "":
        tokens.append(token)
    return tokens


def tokenize(lines: list):
    # Removing comments
    lines = map(lambda line: line.split('#')[0], lines)
    # Splitting by whitespace and commas
    lines = map(split_line, lines)
    # Removing empty lines
    lines = list(filter(None, lines))

    return lines
