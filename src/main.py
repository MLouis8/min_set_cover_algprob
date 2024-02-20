import numpy as np
import file
import algorithms
import sys

# find a 95 percet confidence interval for the mean of data
mu, sigma = 0, 1 # mean and std
data = np.random.normal(mu, sigma, 10000)

confidence_at = 5.
average_value = np.mean(data)
confidence_level = np.percentile(data, [confidence_at/2, 100 - confidence_at/2])
print("mean in interval : " + str(average_value) + " inside " + str(confidence_level))

def main():
    args = sys.argv
    if not (len(args) == 2):
        raise ValueError("only the name of the instance should be given as parameter")
    u_size, s_size, s, sol, seq = file.read_instance(sys.argv[1])

    print(algorithms.naive_approx(s, seq))


main()