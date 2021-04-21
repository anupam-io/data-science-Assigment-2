from lib.cm import count_min_sketch
from random import sample
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./20news-bydate-matlab/20news-bydate/matlab/train.data',
                   delim_whitespace=True,
                   header=None
                   )

freq_of = {}
for i in data.index[:]:
    if data[1][i] in freq_of:
        freq_of[data[1][i]] += data[2][i]
    else:
        freq_of[data[1][i]] = data[2][i]
    if i%10000 == 0:print(i)

top_1000 = sorted(freq_of.items(), key=lambda a: a[1], reverse=True)[:1000]
rand_100 = sample(top_1000, 100)

error = []
k_val = []
for k in [100, 200, 500, 1000, 2000]:
    d = 5
    obj = count_min_sketch(d, k//d)
    for i in data.index[:]:
        obj.add(data[1][i], data[2][i])
        if i%10000 == 0:print(i)

    rel_error = 0
    for i in rand_100:
        rel_error += abs(obj.query(i[0])-i[1])/i[1]

    print("Relative error: ", rel_error/100)
    k_val.append(k)
    error.append(rel_error/100)

plt.plot(k_val, error, linewidth=2)
plt.title("Count-min sketch: k vs. relative error")
plt.xlabel("k")
plt.ylabel("Relative error")
# plt.show()
plt.savefig("./plots/cm.png", dpi=300)