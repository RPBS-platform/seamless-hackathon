def parse_water(alignment,scrambled_scores):
    import scipy
    from scipy.stats import norm
    for l in alignment.splitlines():
        if l.count("Score:"):
            rs = float(l.split()[2])
    import numpy as np
    scr = [float(x) for x in scrambled_scores.splitlines()]
    zscore = (rs-np.mean(scr))/np.std(scr)
    p_value = norm.sf(abs(zscore)) #one-sided
    return {"z":zscore, "p":p_value}
