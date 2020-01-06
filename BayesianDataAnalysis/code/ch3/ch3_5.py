import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def incorrect_posterior(mu_grid, sigma_grid, data):
    n = len(data)
    s = (1 / (n - 1)) * np.sum((data - data.mean()) ** 2)
    return sigma_grid ** (-n - 2) * np.exp(
        -(1 / (2 * sigma_grid ** 2)) * ((n - 1) * s ** 2 + n * (data.mean() - mu_grid) ** 2))


def correct_posterior(mu_grid, sigma_grid, data):
    grid_m = mu.shape[0]
    extend_data = np.repeat(data[:, np.newaxis], grid_m, axis=1)
    extend_data = np.repeat(extend_data[:, :, np.newaxis], grid_m, axis=2)
    return sigma_grid ** (-2) * np.prod(norm.cdf((extend_data + 0.5 - mu_grid) / sigma_grid) -
                                        norm.cdf((extend_data - 0.5 - mu_grid) / sigma_grid), axis=0)


def get_statistics(sample, probability):
    smean = np.sum(sample * probability)
    variance = np.sum(probability * ((sample - smean) ** 2))
    return smean, variance


if __name__ == '__main__':
    # set up the grid
    mu = np.linspace(9.25, 11.5, 1000)
    log_sigma = np.linspace(-1, 1, 1000)
    sigma = np.exp(log_sigma)

    # data
    y = np.array([10, 10, 12, 11, 9])

    # posterior
    mu_v, log_sigma_v = np.meshgrid(mu, log_sigma)
    sigma_v = np.exp(log_sigma_v)
    ip = incorrect_posterior(mu_v, sigma_v, y)
    ip = ip / np.sum(ip)
    p = correct_posterior(mu_v, sigma_v, y)
    p = p / np.sum(p)

    # calculate the posterior mean and variance
    ip_mu = ip.sum(axis=0)
    incorrect_mean_mu, incorrect_variance_mu = get_statistics(mu, ip_mu)
    print('Incorrect posterior mu:\n\tmean:{} \t variance:{}\n'
          .format(incorrect_mean_mu, incorrect_variance_mu))

    ip_sigma = ip.sum(axis=1)
    incorrect_mean_sigma, incorrect_variance_sigma = get_statistics(sigma, ip_sigma)
    print('Incorrect posterior sigma:\n\tmean:{} \t variance:{}\n'
          .format(incorrect_mean_sigma, incorrect_variance_sigma))

    p_mu = p.sum(axis=0)
    correct_mean_mu, correct_variance_mu = get_statistics(mu, p_mu)
    print('Correct posterior mu:\n\tmean:{} \t variance:{}\n'
          .format(correct_mean_mu, correct_variance_mu))

    p_sigma = p.sum(axis=1)
    correct_mean_sigma, correct_variance_sigma = get_statistics(sigma, p_sigma)
    print('Correct posterior sigma:\n\tmean:{} \t variance:{}\n'
          .format(correct_mean_sigma, correct_variance_sigma))

    # plotting
    plt.rcParams.update({'font.size': 18})
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(18, 8))

    ax1.contour(mu_v, log_sigma_v, ip)
    ax1.set_xlabel('mu')
    ax1.set_ylabel('log(sigma)')
    ax1.set_title('Incorrect posterior distribution')
    ax2.contour(mu_v, log_sigma_v, p)
    ax2.set_xlabel('mu')
    ax2.set_title('Correct posterior distribution')

    plt.tight_layout()
    plt.savefig('ch3_5.png')
