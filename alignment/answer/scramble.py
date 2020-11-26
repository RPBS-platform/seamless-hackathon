import random
random.seed(0)
result = ""
for n in range(50):
    seqlist = list(seq)
    random.shuffle(seqlist)
    result += ''.join(seqlist) + "\n"
