import string

def f(a, b):
    with open(a, 'r', encoding='utf-8') as x:
        l = x.readlines()

    lc = len(l)
    wc = 0
    d = {}

    for i in l:
        i = i.lower()
        i = i.translate(str.maketrans('', '', string.punctuation))
        w = i.split()
        wc += len(w)

        for j in w:
            d[j] = d.get(j, 0) + 1

    with open(b, 'w', encoding='utf-8') as y:
        y.write(f"Lines: {lc}\n")
        y.write(f"Words: {wc}\n")
        y.write("Word frequencies:\n")
        for k, v in d.items():
            y.write(f"{k}: {v}\n")

f("text.txt", "analysis.txt")
