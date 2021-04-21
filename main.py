from lib.cm import count_min_sketch
from lib.cs import count_sketch
from lib.mg import misra_gries
from random import sample
import pandas as pd

data = pd.read_csv('./20news-bydate-matlab/20news-bydate/matlab/train.data',
                   delim_whitespace=True,
                   header=None
                   )

freq_of = {}
for i in data.index[:1000000]:
    if data[1][i] in freq_of:
        freq_of[data[1][i]] += data[2][i]
    else:
        freq_of[data[1][i]] = data[2][i]
    if i%10000 == 0:print(i)

top_1000 = sorted(freq_of.items(), key=lambda a: a[1], reverse=True)[:1000]
rand_100 = sample(top_1000, 100)

k = 1000
obj = misra_gries(k)
for i in data.index[:1000000]:
    obj.add(data[1][i], data[2][i])
    if i%10000 == 0:print(i)



rel_error = 0
for i in rand_100:
    rel_error += abs(obj.query(i[0])-i[1])/i[1]

print("Relative error: ", rel_error/100)