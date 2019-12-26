import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    N = 5000    # number of samples
    pre_debate = np.random.beta(294, 307, (N,))
    post_debate = np.random.beta(288, 332, (N,))

    alpha_diff = post_debate - pre_debate
    print("The posterior probability that there was a shift toward Bush: {}".format(np.mean(alpha_diff > 0)))
    plt.hist(alpha_diff, bins=40)
    plt.xlabel('alpha_2 - alpha_1')
    plt.ylabel('number of samples')
    plt.savefig('ch3_2.png')
