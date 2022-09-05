import numpy as np


def _nparray_to_sci_not(radicands):

    exponents = np.log10(radicands).astype(int)

    significands = radicands / 10**exponents

    return {"significands": significands, "exponents": exponents}


def decimal_1(radicands):

    sci_not = _nparray_to_sci_not(radicands)

    estimates = 5.5 * 10**sci_not["exponents"]

    return estimates


def decimal_2(radicands):

    sci_not = _nparray_to_sci_not(radicands)

    estimates = 3.16 * 10**sci_not["exponents"]

    return estimates


def decimal_3(radicands):

    sci_not = _nparray_to_sci_not(radicands)

    filter_low = sci_not["significands"] < 10
    exponents_low = sci_not["exponents"][filter_low]

    filter_high = sci_not["significands"] >= 10
    exponents_high = sci_not["exponents"][filter_high]

    estimates_low = 2 * 10**exponents_low
    estimates_high = 6 * 10**exponents_high

    return np.concatenate((estimates_low, estimates_high))


def linear_1(radicands):

    sci_not = _nparray_to_sci_not(radicands)

    estimates = (sci_not["significands"] - 1 + 1.2) * 10**sci_not["exponents"]

    return estimates


def linear_2(radicands):

    sci_not = _nparray_to_sci_not(radicands)

    filter_low = sci_not["significands"] < 10
    significands_low = sci_not["significands"][filter_low]
    exponents_low = sci_not["exponents"][filter_low]
    estimates_low = (significands_low * 0.28 + 0.89) * 10**exponents_low

    filter_high = sci_not["significands"] >= 10
    significands_high = sci_not["significands"][filter_high]
    exponents_high = sci_not["exponents"][filter_high]
    estimates_high = (significands_high * 0.89 + 2.8) * 10**exponents_high

    return np.concatenate((estimates_low, estimates_high))
