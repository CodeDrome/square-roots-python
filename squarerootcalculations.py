import math

import numpy as np

import squarerootestimates as sre


def babylonian_array(radicands, iterations):

    estimates = sre.linear_2(radicands)

    vfunc = np.vectorize(babylonian)
    square_roots = vfunc(radicands, estimates, iterations)

    return square_roots


def bakhshali_array(radicands, iterations):

    estimates = sre.linear_2(radicands)

    vfunc = np.vectorize(bakhshali)
    square_roots = vfunc(radicands, estimates, iterations)

    return square_roots


def exponential_identity_array(radicands):

    vfunc = np.vectorize(exponential_identity)
    square_roots = vfunc(radicands)

    return square_roots


def babylonian(s, estimate, iterations):

    sqrt = estimate

    for i in range(0, iterations):

        sqrt = (sqrt + s / sqrt) / 2

    return sqrt


def bakhshali(s, estimate, iterations):

    sqrt = estimate

    a = 0
    b = 0

    for i in range(0, iterations):

        a = (s - sqrt**2) / (2 * sqrt)

        b = sqrt + a

        sqrt = b - (a**2 / (2 * b))

    return sqrt


def exponential_identity(n):

    return math.e ** (0.5 * math.log(n))
