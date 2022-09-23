n = int(input())
word = {}
k = []
for i in range(n):
    k.append(input())

k.sort()
for i in range(n):
    word[k[i]] = len(k[i])


p = [x[0] for x in sorted(word.items(), key=lambda x: x[1])]

for i in range(len(p)):
    print(p[i])


# num2 = list(word.values())
# num2.sort()

# print(num2)

# for i in range(len[num]):
#     if num[i] == 0:
#         continue
#     while num[i] != 0:
#         print(word.values(i+1))
#         del word.va[]
