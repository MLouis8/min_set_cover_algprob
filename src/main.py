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

def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1):
    """Draws a bar plot with multiple bars per data point.

    Parameters
    ----------
    ax : matplotlib.pyplot.axis
        The axis we want to draw our plot on.

    data: dictionary
        A dictionary containing the data we want to plot. Keys are the names of the
        data, the items is a list of the values.

        Example:
        data = {
            "x":[1,2,3],
            "y":[1,2,3],
            "z":[1,2,3],
        }

    colors : array-like, optional
        A list of colors which are used for the bars. If None, the colors
        will be the standard matplotlib color cyle. (default: None)

    total_width : float, optional, default: 0.8
        The width of a bar group. 0.8 means that 80% of the x-axis is covered
        by bars and 20% will be spaces between the bars.

    single_width: float, optional, default: 1
        The relative width of a single bar within a group. 1 means the bars
        will touch eachother within a group, values less than 1 will make
        these bars thinner.
    """

    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # Iterate over all data
    for i, (_, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])

    ax.legend(bars, data.keys())
    ax.set_ylabel("competitivity ratio")
    ax.set_xlabel("instances")

def main():
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
    solutions = np.array(solutions)
    rmax = np.array(cmax) / solutions
    rmin = np.array(cmin) / solutions
    rrandom = np.array(crandom) / solutions
    rlognlogm = np.array(clognlogm) / solutions
    data = {
        "max": rmax,
        "min": rmin,
        "random": rrandom,
        "lognlogm": rlognlogm
    }

    _, ax = plt.subplots()
    bar_plot(ax, data, total_width=.8, single_width=1)
    plt.show()

main()