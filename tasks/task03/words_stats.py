"""
You are given a list of sentences. Find all unique words along with:
Number of word occurrences
Number of the sentence where the word appeared for the first time

Note: ignore word case during comparison, i.e. treat “Home”, “home” and “HOME” as the same words.
"""
from re import sub

texts = [
    "Hello, World!",
    "The world is mine",
    "Hello, how are you?"
]

ci_texts = list(map(lambda text: sub('([^A-z^\s])+', '', text).lower().split(), texts))
accumulator = {}

for words in ci_texts:
    index = ci_texts.index(words)
    for word in words:
        d = accumulator.get(word, {})
        line = d.get('line', index)
        count = d.get('count', 0)
        accumulator[word] = {'line': line, 'count': count + 1}

print("{:<5} {:<5} {:<5}".format('word', 'count', 'first line'))
for word in accumulator:
    d = accumulator[word]
    print("{:<5} {:<5} {:<5}".format(word, d['count'], d['line']))
