import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    mu_c, s_c, n_c = 1.013, 0.24, 32
    mu_t, s_t, n_t = 1.173, 0.20, 36

    N = 10000
    normalized_pc = np.random.standard_t(n_c-1, size=(N,))
    normalized_pt = np.random.standard_t(n_t-1, size=(N,))

    pc = normalized_pc * (s_c / np.sqrt(n_c)) + mu_c
    pt = normalized_pt * (s_t / np.sqrt(n_t)) + mu_t

    # calculate 95% posterior interval
    low, high = np.quantile(pt-pc, [0.025, 0.975])

    plt.rcParams.update({'font.size': 12})
    plt.hist(pt-pc, bins=50, density=True)
    plt.title('95% posterior interval: [{0:.3f}, {1:.3f}]'.format(low, high))
    plt.xlabel('mu_t - mu_c')
    plt.ylabel('density')
    plt.savefig('ch3_3.png')

