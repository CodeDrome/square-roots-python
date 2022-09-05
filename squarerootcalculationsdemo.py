import math

import numpy as np

import squarerootcalculations as src
import squarerootplot as srp


def main():

    print("------------------------")
    print("| codedrome.com        |")
    print("| Square Roots         |")
    print("| Part 2: Calculations |")
    print("------------------------\n")

    babylonian()

    # bakhshali()

    # exponential_identity()


def babylonian():

    min = 1
    max = 99

    plot_data = []

    radicands = np.array(range(min, max + 1))

    square_roots_babylonian = src.babylonian_array(radicands, 0)
    plot_data.append({"sqrts": square_roots_babylonian,
                      "label": "Babylonian 0 iterations",
                      "color": "#000000"})

    square_roots_babylonian = src.babylonian_array(radicands, 1)
    plot_data.append({"sqrts": square_roots_babylonian,
                      "label": "Babylonian 1 iterations",
                      "color": "#FF0000"})

    square_roots_babylonian = src.babylonian_array(radicands, 2)
    plot_data.append({"sqrts": square_roots_babylonian,
                      "label": "Babylonian 2 iterations",
                      "color": "#0000FF"})

    square_roots_babylonian = src.babylonian_array(radicands, 3)
    plot_data.append({"sqrts": square_roots_babylonian,
                      "label": "Babylonian 3 iterations",
                      "color": "#00FF00"})

    square_roots_babylonian = src.babylonian_array(radicands, 4)
    plot_data.append({"sqrts": square_roots_babylonian,
                      "label": "Babylonian 4 iterations",
                      "color": "#FF8000"})

    srp.plot((min,max), plot_data)


def bakhshali():

    min = 1
    max = 99

    plot_data = []

    radicands = np.array(range(min, max + 1))

    square_roots_bakhshali = src.bakhshali_array(radicands, 0)
    plot_data.append({"sqrts": square_roots_bakhshali,
                      "label": "Bakhshali 0 iterations",
                      "color": "#000000"})

    square_roots_bakhshali = src.bakhshali_array(radicands, 1)
    plot_data.append({"sqrts": square_roots_bakhshali,
                      "label": "Bakhshali 1 iterations",
                      "color": "#FF0000"})

    square_roots_bakhshali = src.bakhshali_array(radicands, 2)
    plot_data.append({"sqrts": square_roots_bakhshali,
                      "label": "Bakhshali 2 iterations",
                      "color": "#FF8000"})

    srp.plot((min,max), plot_data)


def exponential_identity():

    min = 1
    max = 99

    plot_data = []

    radicands = np.array(range(min, max + 1))

    square_roots_exponential_identity = src.exponential_identity_array(radicands)
    plot_data.append({"sqrts": square_roots_exponential_identity,
                      "label": "Exponential Identity",
                      "color": "#FF8000"})

    srp.plot((min,max), plot_data)


if __name__ == "__main__":

    main()
