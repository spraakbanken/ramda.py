from ramda.curry import curry


@curry
def split_every(length, collection):
    return [
        collection[length * i:length * (i + 1)]
        for i in range(0, round(len(collection) / length + 1))
        if collection[length * i:length * (i + 1)]
    ]
