import numpy as np
import matplotlib.pyplot as plt

fatal_accidents = np.array([24, 25, 31, 31, 22, 21, 26, 20, 16, 22])
passenger_death = np.array([734, 516, 754, 877, 814, 362, 764, 809, 223, 1066])
death_rate = np.array([0.19, 0.12, 0.15, 0.16, 0.14, 0.06, 0.13, 0.13, 0.03, 0.15])


def sample_from_model1(alpha, beta, num_sample, num_batch):
    samples = np.zeros(shape=(num_sample, num_batch))
    for ind in range(num_sample):
        theta_s = np.random.gamma(alpha, 1 / beta)
        samples[ind] = np.random.poisson(theta_s, size=(num_batch,))
    return samples


def sample_from_model2(alpha, beta, x, num_sample, num_batch, scale = 1e8):
    samples = np.zeros(shape=(num_sample, num_batch))
    beta_ = beta / scale
    for ind in range(num_sample):
        theta_s = np.random.gamma(alpha, 1 / beta_) / scale
        samples[ind] = np.random.poisson(theta_s * x, size=(num_batch,))
    return samples


def calculate_fano_factor(samples, data, file_name='fig.png'):
    print('Calculating Fano factor...')
    fn_data = np.var(data) / np.mean(data)
    fn_sample = np.var(samples, axis=1) / np.mean(samples, axis=1)
    # p-value
    p_value = np.mean(fn_sample > fn_data)
    print('p-value for fano factor = {}'.format(p_value))
    plt.figure(figsize=(8, 6))
    height = plt.hist(fn_sample, bins=40, label='posterior predictive fano factor')
    plt.plot([fn_data, fn_data], [0, max(height[0])], label='data', color='red')
    plt.title('fano factor p(T(sample) > T(data)) = {}'.format(p_value))
    plt.legend()
    plt.savefig(file_name)


def calculate_autocorrelation(samples, data, file_name='autocorrelation.png'):
    print('Calculating autocorrelation....')
    ar_data = np.sum((data[:-1] - data.mean()) * (data[1:] - data.mean())) / np.sum((data - data.mean()) ** 2)

    num_samples = samples.shape[0]
    sample_mean = np.ones((num_samples, 10)) * samples.mean(axis=1, keepdims=True)
    ar_sample = np.sum((samples[:, :-1] - sample_mean[:, :-1]) \
                       * (samples[:, 1:] - sample_mean[:, 1:]), axis=1) \
                / np.sum((samples - sample_mean) ** 2, axis=1)

    p_value = np.mean(ar_sample > ar_data)
    print('p-value for autocorrelation = {}'.format(p_value))
    plt.figure(figsize=(8, 6))
    height = plt.hist(ar_sample, bins=40, label='posterior predictive autocorrelation')
    plt.plot([ar_data, ar_data], [0, max(height[0])], label='data', color='red')
    plt.title('autocorrelation p(T(sample) > T(data)) = {}'.format(p_value))
    plt.legend()
    plt.savefig(file_name)


if __name__ == '__main__':
    # ====================================
    # Model 1: fatal_accidents | theta
    # ====================================
    num_samples = 5000
    alpha_pos = np.sum(fatal_accidents)
    beta_pos = len(fatal_accidents)
    samples_model1 = sample_from_model1(alpha_pos, beta_pos, num_samples, len(fatal_accidents))

    calculate_fano_factor(samples_model1, fatal_accidents, '2_fano_factor_model1.png')
    calculate_autocorrelation(samples_model1, fatal_accidents, '2_autocorrelation_model1.png')

    # =================================================================
    # Model 2: fatal_accidents | theta, number_of_passenger_miles_flown
    # =================================================================
    pass_miles_flown = passenger_death / death_rate * 1e8
    alpha_pos_2 = np.sum(fatal_accidents)
    beta_pos_2 = np.sum(pass_miles_flown)
    samples_model2 = sample_from_model2(alpha_pos_2, beta_pos_2, pass_miles_flown,
                                        2000, len(fatal_accidents), scale=1e10)

    calculate_fano_factor(samples_model2, fatal_accidents, '2_fano_factor_model2.png')
    calculate_autocorrelation(samples_model2, fatal_accidents, '2_autocorrelation_model2.png')
