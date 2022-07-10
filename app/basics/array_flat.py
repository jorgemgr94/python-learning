import itertools

words = [
    ['jorge', 'jorge1', 'jorge2'],
    ['jorge3', 'jorge4', 'jorge5'],
    ['test'],
    ['tes1', 'test3']
]

# flat array
words = list(itertools.chain(*words))

print(words)
