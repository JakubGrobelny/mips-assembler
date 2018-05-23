def tokenize(lines : list):
    # Removing comments
    lines = map(lambda line : line.split('#')[0], lines)

    for line in lines:
        print(line)
        
    return lines