import math

import numpy as np

import squarerootestimates as sre
import squarerootplot as srp


def main():

    print("----------------------")
    print("| codedrome.com      |")
    print("| Square Roots       |")
    print("| Part  1: Estimates |")
    print("----------------------\n")

    min = 1
    max = 99

    estimates = []

    radicands = np.array(range(min, max + 1))

    estimates_decimal_1 = sre.decimal_1(radicands)
    estimates.append({"sqrts": estimates_decimal_1,
                      "label": "decimal_1",
                      "color": "#FF0000"})

    estimates_decimal_2 = sre.decimal_2(radicands)
    estimates.append({"sqrts": estimates_decimal_2,
                      "label": "decimal_2",
                      "color": "#FF8000"})

    estimates_decimal_3 = sre.decimal_3(radicands)
    estimates.append({"sqrts": estimates_decimal_3,
                      "label": "decimal_3",
                      "color": "#FF00FF"})

    estimates_linear_1 = sre.linear_1(radicands)
    estimates.append({"sqrts": estimates_linear_1,
                      "label": "linear_1",
                      "color": "#00FFFF"})

    estimates_linear_2 = sre.linear_2(radicands)
    estimates.append({"sqrts": estimates_linear_2,
                      "label": "linear_2",
                      "color": "#000080"})

    srp.plot((min,max), estimates)


if __name__ == "__main__":

    main()
