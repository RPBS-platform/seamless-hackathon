def scramble(seq):
    seq = "".join([l for l in seq.split() if not l.startswith(">")])
    from random import shuffle
    l = list(seq)
    rs =[]
    for x in range(0,50):
        shuffle(l)
        rs.append("".join(l))
    return "\n".join(rs)

#result = scramble(seq)
