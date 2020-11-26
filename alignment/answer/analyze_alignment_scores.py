import numpy as np
import scipy.stats as st

for line in alignment.splitlines():
    l = line.split()
    if len(l) < 3:
        continue
    if l[1] == "Score:":
        score = float(l[2])
        break
else:
    raise Exception("Malformed alignment")

scrambled_scores = [float(sc) for sc in scrambled_scores.splitlines()]
scrambled_scores = np.array(scrambled_scores)

z = (score - scrambled_scores.mean()) / scrambled_scores.std(ddof=1)
p = 1 - st.norm.cdf(z)
result = {
    "z": z,
    "p": p,
}
