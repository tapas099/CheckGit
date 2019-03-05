# l1 = [1, 2, 3, 4]
# l2 = l1
# l3 = l2
# print(f'l1: {l1}')
# l1.pop()
# print(l1)
# l1.append(8)
# print(l2)
# l2.append(5)
# print(l3)

#
d1=[1,2,3,4]
d2=d1.copy()
d3=d2.copy()

print(f'd1: {d1}')
d1.pop()
print(f'd2: {d2}')
d2.append(7)
print(f'd3: {d3}')
d3.remove(2)
d3.append(9)
print(f'd1: {d1}')
print(f'd2: {d2}')
print(f'd3: {d3}')