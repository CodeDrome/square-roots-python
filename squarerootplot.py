import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def plot(valuerange, sqrts=None):

    matplotlib.pyplot.figure(figsize=(10,8), facecolor="#FFFFFF")

    plt.title('Square Roots in Python ')

    values = np.array(range(valuerange[0], valuerange[1]+1))
    npsqrts = np.sqrt(values)

    plt.plot(values,
             npsqrts,
             label='NumPy sqrt',
             color='#0000FF',
             alpha=0.25,
             linewidth=4)

    if sqrts != None:
        for sqrt in sqrts:
            plt.plot(values,
                     sqrt["sqrts"],
                     label=sqrt["label"],
                     color=sqrt["color"],
                     linewidth=1.0)

    plt.legend()
    plt.show()
