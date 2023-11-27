import assignment5
import matplotlib.pyplot as plt

normal_frequencies = {
    'A': 8.2,
    'B': 1.5,
    'C': 2.8,
    'D': 4.3,
    'E': 12.7,
    'F': 2.2,
    'G': 2.0,
    'H': 6.1,
    'I': 7.0,
    'J': 0.15,
    'K': 0.77,
    'L': 4.0,
    'M': 2.4,
    'N': 6.7,
    'O': 7.5,
    'P': 1.9,
    'Q': 0.095,
    'R': 6.0,
    'S': 6.3,
    'T': 9.1,
    'U': 2.8,
    'V': 0.98,
    'W': 2.4,
    'X': 0.15,
    'Y': 2.0,
    'Z': 0.074,
}


def manual_analysis(text: str):
    frequencies = dict()
    for c in text:
        c = c.upper()
        if c.isupper():
            if c in frequencies:
                frequencies[c] += 1
            else:
                frequencies[c] = 1
    m = max(frequencies, key=frequencies.get)
    key = (ord(m) - ord('E') + 26) % 26
    decrypted = assignment5.decrypt(text, key)
    return decrypted


def automatic_cracking(text: str):
    print(text)
    frequencies = dict()
    for c in text:
        c = c.upper()
        if c.isupper():
            if c in frequencies:
                frequencies[c] += 1
            else:
                frequencies[c] = 1
    frequencies_sort = sorted(frequencies, key=frequencies.get, reverse=True)
    plt.bar(frequencies.keys(), frequencies.values(), 1.0, color='g')
    plt.show()
    for c in normal_frequencies:
        if c not in frequencies_sort:
            frequencies_sort.append(c)
    min_difference = 100
    cracked_key = 0
    for c in frequencies_sort:
        key = (ord(c) - ord('E') + 26) % 26
        decrypted = assignment5.decrypt(text, key)
        difference = analyze_decrypted(decrypted)
        if difference < min_difference:
            min_difference = difference
            cracked_key = key
    return assignment5.decrypt(text, cracked_key)


def analyze_decrypted(text: str):
    frequencies = dict()
    for c in text:
        c = c.upper()
        if c.isupper():
            if c in frequencies:
                frequencies[c] += 1
            else:
                frequencies[c] = 1
    frequencies_percent = dict()
    total = sum(frequencies.values())
    for c in frequencies:
        frequencies_percent[c] = frequencies[c] / total * 100
    difference = 0
    for c in normal_frequencies:
        if c in frequencies_percent:
            difference += abs(normal_frequencies[c] - frequencies_percent[c])
        else:
            difference += normal_frequencies[c]
    difference /= 26
    return difference
