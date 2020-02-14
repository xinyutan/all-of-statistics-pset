import numpy as np
import matplotlib.pyplot as plt

from util import draw_sample_from_marginal, draw_2nd_var_from_joint, add_jitter

# data
x = np.array([-0.86, -0.30, -0.05, 0.73])  # Dose x (log g/ml)
n = np.array([5, 5, 5, 5])  # Number of animals
y = np.array([0, 1, 3, 5])  # Number of deaths


def compute_prior(alpha_grid, beta_grid, parameters):
    mu_alpha, sigma_alpha = parameters['mu_alpha'], parameters['sigma_alpha']
    mu_beta, sigma_beta = parameters['mu_beta'], parameters['sigma_beta']
    rho = parameters['rho']
    exp_part = (alpha_grid - mu_alpha) ** 2 / sigma_alpha ** 2 + \
               (beta_grid - mu_beta) ** 2 / sigma_beta ** 2 - \
               2 * rho * (alpha_grid - mu_alpha) * (beta_grid - mu_beta) / (sigma_alpha * sigma_beta)
    return 1 / (2 * np.pi * sigma_alpha * sigma_beta * np.sqrt(1 - rho ** 2)) * \
           np.exp(-1 / (1 - rho ** 2) * exp_part)


def compute_log_likelihood(alpha_grid, beta_grid):
    """
    log p(y|alpha, beta, x, n) = -n log (1 + exp(-(alpha + beta x))) - x (n - y)
    """
    m1, m2 = alpha_grid.shape

    def grid_data(a):
        extend_a = np.repeat(a[:, np.newaxis], m1, axis=1)
        extend_a = np.repeat(extend_a[:, :, np.newaxis], m2, axis=2)
        return extend_a

    x_grid = grid_data(x)
    y_grid = grid_data(y)
    n_grid = grid_data(n)

    return np.sum(-n_grid * np.log(1 + np.exp(-alpha_grid - beta_grid * x_grid))
                  - (alpha_grid + beta_grid * x_grid) * (n_grid - y_grid), axis=0)


if __name__ == '__main__':
    # parameters
    parameters = {'mu_alpha': 0, 'sigma_alpha': 2,
                  'mu_beta': 10, 'sigma_beta': 10,
                  'rho': 0.5}

    # set up grid
    alpha = np.linspace(-6, 6, 1000)
    beta = np.linspace(-20, 40, 1200)
    alpha_grid, beta_grid = np.meshgrid(alpha, beta)

    prior = compute_prior(alpha_grid, beta_grid, parameters)
    lld = compute_log_likelihood(alpha_grid, beta_grid)
    log_posterior = np.log(prior) + lld
    posterior = np.exp(log_posterior)
    posterior = posterior / np.sum(posterior)

    # sampling from the posterior distribution
    samples = {'alpha': [], 'beta': []}
    alpha_marginal = posterior.sum(axis=0)
    num_samples = 1500
    for s in range(num_samples):
        a, a_id = draw_sample_from_marginal(alpha, alpha_marginal)
        b, b_id = draw_2nd_var_from_joint(beta, posterior, a_id)
        a_, b_ = add_jitter(a, alpha[1] - alpha[0]), add_jitter(b, beta[1] - beta[0])
        samples['alpha'].append(a_)
        samples['beta'].append(b_)

    # plot the scatter plot
    plt.rcParams.update({'font.size': 18})
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(6, 16))
    ax1.contour(alpha_grid, beta_grid, posterior)
    ax1.set_ylabel('beta')
    ax1.set_title('Contour plot of posterior \ndistribution')

    ax2.scatter(samples['alpha'], samples['beta'], s=1, alpha=0.5, marker='o')
    ax2.set_xlabel('alpha')
    ax2.set_ylabel('beta')
    ax2.set_title('Scatter plot from samples of \nthe posterior distribution')
    plt.tight_layout()
    plt.savefig('ch3_11_1.png')

    # calculate and plot LD50
    # x = - alpha / beta
    px = -np.array(samples['alpha']) / np.array(samples['beta'])
    plt.figure()
    plt.hist(px, bins=50)
    plt.xlabel('LD50')
    plt.tight_layout()
    plt.savefig('ch3_11_2.png')
