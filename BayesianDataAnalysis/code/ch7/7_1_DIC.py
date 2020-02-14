"""Refer to ch3_11.py"""

import numpy as np
import sys

sys.path.append('../ch3')

from util import draw_sample_from_marginal, draw_2nd_var_from_joint, add_jitter
from ch3_11 import compute_log_likelihood

# data
x = np.array([-0.86, -0.30, -0.05, 0.73])  # Dose x (log g/ml)
n = np.array([5, 5, 5, 5])  # Number of animals
y = np.array([0, 1, 3, 5])  # Number of deaths

if __name__ == '__main__':

    # set up grid
    alpha = np.linspace(-6, 6, 1000)
    beta = np.linspace(-20, 40, 1200)
    alpha_grid, beta_grid = np.meshgrid(alpha, beta)

    # set up grid
    alpha = np.linspace(-6, 6, 1000)
    beta = np.linspace(-20, 40, 1200)
    alpha_grid, beta_grid = np.meshgrid(alpha, beta)

    lld = compute_log_likelihood(alpha_grid, beta_grid)
    posterior = np.exp(lld)  # uniform prior
    posterior = posterior / np.sum(posterior)

    # sampling from the posterior distribution
    alpha_marginal = posterior.sum(axis=0)
    num_samples = 1500
    samples = np.zeros(shape=(num_samples, 2))  # first column: alpha, second column: beta
    for s in range(num_samples):
        a, a_id = draw_sample_from_marginal(alpha, alpha_marginal)
        b, b_id = draw_2nd_var_from_joint(beta, posterior, a_id)
        a_, b_ = add_jitter(a, alpha[1] - alpha[0]), add_jitter(b, beta[1] - beta[0])
        samples[s, 0] = a_
        samples[s, 1] = b_

    x_ = np.concatenate((np.ones_like(x), x)).reshape((2, -1))
    Epost_y = np.sum(-n * np.log(1 + np.exp(-np.matmul(samples, x_)))
                     - np.matmul(samples, x_) * (n - y)) / num_samples

    Epost_param = np.mean(samples, axis=0)
    logp_Epost = np.sum(-n * np.log(1 + np.exp(-np.matmul(Epost_param, x_)))
                        - np.matmul(Epost_param, x_) * (n - y))

    # =============================
    # Calculating DIC
    # =============================
    print("Calculating DIC...")
    pDIC = 2 * (logp_Epost - Epost_y)
    elpdDIC = logp_Epost - pDIC
    DIC = - 2 * elpdDIC
    print("pDIC = {}, elpdDIC = {}, DIC = {}".format(pDIC, elpdDIC, DIC))

    # =============================
    # Calculating WAIC
    # =============================
    print("\n\nCalculating WAIC...")
    # llpd
    inv_logit = 1 / (1 + np.exp(-np.matmul(samples, x_)))
    llpd = np.log(np.mean(inv_logit ** y * ((1-inv_logit) ** (n - y)), axis=0)).sum()
    print("llpd = {}".format(llpd))

    # effective number of the parameters
    pwaic1 = 2 * (llpd - Epost_y)
    print("Effective number of the parameters v1 = {}".format(pwaic1))

    logp_post = -n * np.log(1 + np.exp(-np.matmul(samples, x_))) \
                - np.matmul(samples, x_) * (n - y)
    logp_post_avg = logp_post.mean(axis=0)
    pwaic2 = np.sum(np.sum((logp_post - logp_post_avg)**2, axis=0) / (num_samples - 1))
    print("Effective number of the parameters v2 = {}".format(pwaic2))

    elpdWAIC1 = llpd - pwaic1
    elpdWAIC2 = llpd - pwaic2
    WAIC1 = -2 * elpdWAIC1
    WAIC2 = -2 * elpdWAIC2

    print("elpdWAIC1 = {}, WAIC1 = -2 * elpdWAIC1 = {}".format(elpdWAIC1, WAIC1))
    print("elpdWAIC2 = {}, WAIC1 = -2 * elpdWAIC2 = {}".format(elpdWAIC2, WAIC2))