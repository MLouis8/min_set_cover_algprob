import numpy as np
import file
import algorithms
import sys

def some_code():
    # find a 95 percet confidence interval for the mean of data
    mu, sigma = 0, 1 # mean and std
    data = np.random.normal(mu, sigma, 10000)

    confidence_at = 5.
    average_value = np.mean(data)
    confidence_level = np.percentile(data, [confidence_at/2, 100 - confidence_at/2])
    print("mean in interval : " + str(average_value) + " inside " + str(confidence_level))

def verify_sol(sol, seq):
    for x in seq:
        present = False
        for s in sol:
            if x in s:
                present = True
        if not present:
            return False
    return True

def main():
    repeat = 30 if len(sys.argv) == 2 else sys.argv[2]
    costs = []
    u_size, s_size, s, sol, seq = file.read_instance(sys.argv[1])
    for k in range(repeat):
        cover_idx = algorithms.naive_approx(s, seq)
        costs.append(len(cover_idx))
    confidence_at = 5.
    average_value = np.mean(costs)
    confidence_level = np.percentile(costs, [confidence_at/2, 100 - confidence_at/2])
    print(f"mean in interval : {average_value} inside {confidence_level}\ncompared to exact solution: {sol}")
main()