from ramda.curry import curry


@curry
def take(n, xs):
    """Returns the first n elements of the given list, string, or
transducer/transformer (or object with a take method).
Dispatches to the take method of the second argument, if present"""
    return xs[:n]
