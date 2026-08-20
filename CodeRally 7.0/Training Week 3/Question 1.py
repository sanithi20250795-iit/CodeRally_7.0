"""You are a cryptanalyst working for a deep space monitoring agency. You've intercepted a stream of coded signals from an unknown source. Your team's initial analysis suggests a peculiar pattern: signals that use the exact same set of characters, just in a different order, are related messages (i.e., they are anagrams).

To decipher their meaning, your first task is to group these related signals. Furthermore, intelligence suggests that shorter signals are likely high-priority tactical messages, while longer ones are less urgent strategic reports.

Your mission is to write a program that takes a list of intercepted signals (strings), groups them by anagram equivalence, and then organizes these groups for priority analysis.

The Sorting Mandate The final report must be structured according to two strict rules:

Primary Sort (By Length): The groups of signals must be ordered by the length of the signals they contain, from shortest to longest. If two groups have strings of the same length, they should be sorted alphabetically based on the first string in each group.
Secondary Sort (Lexicographical): Within each group, the individual signals must be sorted alphabetically.
Input Format

The first line contains an integer T, the number of test cases.
For each test case: The first line contains an integer n (1 ≤ n ≤ 1000), the number of intercepted signals. The next n lines each contain a lowercase string (1 to 50 characters long), representing a single signal.
Constraints

1 ≤ n ≤ 1000

Output Format

For each test case, output the anagram groups, one group per line. Each group should contain its signals sorted lexicographically and separated by spaces. The groups themselves should be ordered according to the "Sorting Mandate."

Sample Input 0

1
8
cat
listen
dog
act
silent
race
solo
care
Sample Output 0

act cat
dog
care race
solo
listen silent
Language
Python 3
More
1
# Enter your code here. Read input from STDIN. Print output to STDOUT
Line: 1 Col: 70

Test against custom input
BlogScoring"""


import sys
from collections import defaultdict


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1

        groups = defaultdict(list)

        for _ in range(n):
            word = data[idx]
            idx += 1

     
            freq = [0] * 26
            for c in word:
                freq[c - 97] += 1

            groups[tuple(freq)].append(word)

        result = []

        for words in groups.values():
            words.sort()
            result.append(words)

        result.sort(key=lambda g: (len(g[0]), g[0]))

        for group in result:
            out.append(b' '.join(group))

    sys.stdout.buffer.write(b'\n'.join(out) + b'\n')


if __name__ == "__main__":
    main()
