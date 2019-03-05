dict1 = {1: 'one', 2: 'two', 3: 'three'}
# dict1={v:k for k,v in dict1.items()}
# print(dict1)

# res=dict()
# for k,v in dict1.items():
#     res.update({v:k})
#
# print(res)

from itertools import chain

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = dic3
dic5 = dic2.copy()
# dic = dict(chain(dic1.items(), dic2.items(), dic3.items()))
dic = dict()
dic.update(dic1)
dic.update(dic2)
dic.update(dic4)
print(dic)
# dic.update({1: 'bingoo'})
dic3.update({5: 'five'})
dic2.update({4: 'four'})
dic5[7] = 'seven'
dic6 = {**dic1, **dic5, **dic4}

print(dic6)
