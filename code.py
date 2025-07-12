import numpy as np
import matplotlib.pyplot as plt

# We should select N random numbers uniformly distributed between 0 and 1.
def select_a_number(N):
    return np.random.uniform(0, 1, N)

# we should write a function to check weather the median of the selected random numbers is greater than m
def does_median_greater_than_m(random_numbers, m):
    median = np.median(random_numbers)
    return median > m

# we should estimate the probability that the median of N random numbers is greater than m
def estimate_probability(N, m, num_experiments=10000):
    count = 0
    for _ in range(num_experiments):
        random_numbers = select_a_number(N)
        if does_median_greater_than_m(random_numbers, m):
            count += 1
    return count / num_experiments

# for plotting the probabilities of the median to be greater than m for various values of N and m
def plot_the_probabilities(N_values, m_values):
    for m in m_values:
        probabilities = []
        for N in N_values:
            prob = estimate_probability(N, m)
            probabilities.append(prob)
        plt.plot(N_values, probabilities, label=f'm={m}')
    plt.xlabel('N')
    plt.ylabel('Probability')
    plt.legend()
    plt.title('Probability of Median being Greater than m')
    plt.show()

# we should give the range of N values and m values for testing
N_values = list(range(3, 26, 2))
m_values = [0.4, 0.6, 0.8]

# finally this is function for plotting the probabilities for specified range of N and m values
plot_the_probabilities(N_values, m_values)