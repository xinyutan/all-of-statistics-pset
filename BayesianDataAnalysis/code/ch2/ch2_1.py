import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

if __name__ == '__main__':
    theta = np.linspace(0, 1, 1000)
    prior = beta.pdf(theta, 4, 4)
    posterior = prior * ( (1-theta)**2 + 10 * theta * (1-theta) + 45 * theta ** 2) * (1-theta)**8
    plt.plot(theta, posterior)
    plt.xlabel('theta')
    plt.ylabel('posterior density')
    plt.savefig('ch2_1.png')