import numpy as np


def draw_sample_from_marginal(vars, prob):
    cdf = np.array(prob)
    for i in range(1, prob.shape[0]):
        cdf[i] += cdf[i-1]
    u = np.random.uniform()
    ind = np.where(cdf == u)[0]
    if len(ind) > 0:
        return vars[ind], ind
    ind_l, ind_r = np.where(cdf < u)[0][-1], np.where(cdf > u)[0][0]
    return vars[(ind_l + ind_r) // 2], (ind_l + ind_r) // 2


def draw_2nd_var_from_joint(vars, joint, id):
    marginal = joint[:, id]
    marginal = marginal / marginal.sum()
    return draw_sample_from_marginal(vars, marginal)


def add_jitter(x, width):
    return np.random.uniform(x - width / 2, x + width / 2)