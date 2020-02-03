import numpy as np
import matplotlib.pyplot as plt

fatal_accidents = np.array([24, 25, 31, 31, 22, 21, 26, 20, 16, 22])

if __name__ == '__main__':
    avg_fas = np.mean(fatal_accidents)

    num_samples = 2000
    samples = np.zeros(shape=(num_samples, len(fatal_accidents)))
    alpha_pos = np.sum(fatal_accidents)
    beta_pos = len(fatal_accidents)
    for ind in range(num_samples):
        theta_s = np.random.gamma(alpha_pos, 1/beta_pos)
        samples[ind] = np.random.poisson(theta_s, size=(len(fatal_accidents), ))

    print('Calculating Fano factor...')
    fn_data = np.var(fatal_accidents) / np.mean(fatal_accidents)
    fn_sample = np.var(samples, axis=1) / np.mean(samples, axis=1)
    # p-value
    p_value = np.mean(fn_sample > fn_data)
    print('p-value for fano factor = {}'.format(p_value))
    plt.figure(figsize=(8,6))
    plt.hist(fn_sample, bins=40, label='posterior predictive fano factor')
    plt.plot([fn_data, fn_data], [0, 160], label='data', color='red')
    plt.title('fano factor p(T(sample) > T(data)) = {}'.format(p_value))
    plt.legend()
    plt.savefig('2_fano_factor.png')

    print('Calculating autocorrelation....')
    ar_data = np.sum((fatal_accidents[:-1] - fatal_accidents.mean()) * (fatal_accidents[1:] - fatal_accidents.mean())) / np.sum((fatal_accidents - fatal_accidents.mean())**2)

    sample_mean = np.ones((num_samples, 10)) * samples.mean(axis=1, keepdims=True)
    ar_sample = np.sum((samples[:, :-1] - sample_mean[:, :-1]) \
                       * (samples[:, 1:] - sample_mean[:, 1:]), axis=1) \
                / np.sum((samples - sample_mean)**2, axis=1)

    p_value = np.mean(ar_sample > ar_data)
    print('p-value for autocorrelation = {}'.format(p_value))
    plt.figure(figsize=(8,6))
    plt.hist(ar_sample, bins=40, label='posterior predictive autocorrelation')
    plt.plot([ar_data, ar_data], [0, 160], label='data', color='red')
    plt.title('autocorrelation p(T(sample) > T(data)) = {}'.format(p_value))
    plt.legend()
    plt.savefig('2_autocorrelation.png')


