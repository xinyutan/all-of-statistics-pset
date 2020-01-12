"""Bayesian Data Analysis

1. Contour plot for (N, theta)
2. Posterior scatter plot for (N, theta)
3. Calculate the posterior probability that N > 100
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom

from util import draw_sample_from_marginal, draw_2nd_var_from_joint, add_jitter


def calculate_posterior(N_grid, theta_grid, data):
    m, n = N_grid.shape
    extend_data = np.repeat(data[:, np.newaxis], m, axis=1)
    extend_data = np.repeat(extend_data[:, :, np.newaxis], n, axis=2)

    return 1 / N_grid * np.prod(binom(N_grid, extend_data) * (theta_grid ** extend_data) \
                                * (1-theta_grid) ** (N_grid - extend_data), axis=0) \
        * (N_grid > data.max())


if __name__ == '__main__':
    # calculate the posterior distribution
    data = np.array([53, 57, 66, 67, 72])

    Ns = np.arange(72, 1000)
    thetas = np.linspace(0, 1, 2000)

    N_grid, theta_grid = np.meshgrid(Ns, thetas)
    posterior = calculate_posterior(N_grid, theta_grid, data)
    posterior = posterior / posterior.sum()

    # sample 1000 points from the posterior distribution using
    # procedure on page 76
    N_marginal = posterior.sum(axis=0)
    samples = {'N': [], 'theta': []}
    for s in range(1000):
        n, n_id = draw_sample_from_marginal(Ns, N_marginal)
        t, t_id = draw_2nd_var_from_joint(thetas, posterior, n_id)
        n_, t_ = add_jitter(n, 1), add_jitter(t, thetas[1] - thetas[0])
        samples['N'].append(n_)
        samples['theta'].append(t_)

    # plot the scatter plot
    plt.rcParams.update({'font.size': 18})
    fig, (ax1, ax2) = plt.subplots(2, 1, sharey=True, figsize=(10, 16))
    ax1.contour(N_grid, theta_grid, posterior)
    ax1.set_xlabel('N')
    ax1.set_ylabel('theta')
    ax1.set_title('Contour plot of posterior distribution')

    ax2.scatter(samples['N'], samples['theta'], s=1, alpha=0.5, marker='o')
    ax2.set_xlabel('N')
    ax2.set_ylabel('theta')
    ax2.set_title('Scatter plot from samples of the posterior distribution')

    plt.tight_layout()
    plt.savefig('ch3_6.png')

    # probability that N > 100
    id_100 = np.where(Ns==100)[0][0]
    print("probability that N > 100 = {}".format(np.sum(N_marginal[id_100+1:])))
