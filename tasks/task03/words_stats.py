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

for line_number, line in enumerate(ci_texts):
    for word in line:
        d = accumulator.get(word, {})
        line_index = d.get('line', line_number)
        count = d.get('count', 0)
        accumulator[word] = {'line': line_index, 'count': count + 1}

print(f"{'word':<6} {'count':<5} {'first line':<5}")

sorted_accumulator = sorted(accumulator.items(), key=lambda x: x[1]['count'], reverse=True)

for word, d in sorted_accumulator:
    print(f"{word:<6} {d['count']:<5} {d['line']:<5}")
