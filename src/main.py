import numpy as np
import matplotlib.pyplot as plt
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
    # repeat = 30 if len(sys.argv) == 2 else sys.argv[2]
    # costs = []
    # u_size, s_size, s, sol, seq = file.read_instance(sys.argv[1])
    # for k in range(repeat):
    #     cover_idx = algorithms.naive_approx(s, seq)
    #     costs.append(len(cover_idx))
    # confidence_at = 5.
    # average_value = np.mean(costs)
    # confidence_level = np.percentile(costs, [confidence_at/2, 100 - confidence_at/2])
    # print(f"mean in interval : {average_value} inside {confidence_level}\ncompared to exact solution: {sol}")
    instances = [
        "instance_1x",
        "instance_1y",
        "instance_2a",
        "instance_2x",
        "instance_2y",
        "instance_3.1a",
        "instance_3.3a",
        "instance_10a",
        "instance_11a",
        "instance_12a",
        "instance_13a",
        "instance_14a",
        "instance_15a",
        "instance_16a",
        "instance_16b",
        "instance_17a",
        "instance_17b",
        "instance_17c",
        "instance_19a",
        "instance_19b",
        "instance_19c"
    ]
    solutions, cmax, cmin, crandom, clognlogm = [], [], [], [], []

    for instance in instances:
        if instance == "instance_3.3a":
            solutions.append(sol)
            cmax.append(0)
            cmin.append(0)
            crandom.append(0)
            clognlogm.append(0)
            continue
        _, _, s, sol, seq = file.read_instance(instance)
        solutions.append(sol)
        naive_max, naive_min, full_random, lognlogm = [], [], [], []

        for _ in range(100):
            naive_max.append(len(algorithms.naive_approx(s, seq)))
            naive_min.append(len(algorithms.naive_approx(s, seq, min=True)))
            full_random.append(len(algorithms.full_random_approx(s, seq)))
            lognlogm.append(len(algorithms.lognlogm(s, seq)))
        cmax.append(np.mean(naive_max))
        cmin.append(np.mean(naive_min))
        crandom.append(np.mean(full_random))
        clognlogm.append(np.mean(lognlogm))
        print(f"{instance} done")
    fig, ax = plt.subplots()
    instances_name = [instance[9:] for instance in instances]
    ax.plot(instances_name, solutions, label="sol")
    ax.plot(instances_name, cmax, label="max")
    ax.plot(instances_name, cmin, label="min")
    ax.plot(instances_name, crandom, label="random")
    ax.plot(instances_name, clognlogm, label="lognlogm")

    ax.legend()
    plt.show()

main()