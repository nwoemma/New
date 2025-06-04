# def do_not_repeat(word):
#     seen = {}
#     for i in word:
#         if i in seen:
#             seen[i] += 1
#         else:
#             seen[i] = 1
#     for k,l in seen.items():
#         if l == 1:
#             return k
# print(do_not_repeat("swiss"))
# Set = {10,20,[30,40]}
# result = Set[2][1]
# print(result)
x = 0
while x < 20:
    x = x +3
print(x)

num = 11
if num & 1==1:
    print('odd')
x = []
y = [[0,1,2],[3,4,5],[6,7,8]]
x.append([row[i] for row in y for i in range(3)])
print(x)
