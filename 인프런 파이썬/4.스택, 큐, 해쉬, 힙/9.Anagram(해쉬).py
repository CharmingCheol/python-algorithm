import sys

# 개선 1
str1 = str(sys.stdin.readline().strip())
str2 = str(sys.stdin.readline().strip())
dict1 = dict()
dict2 = dict()

for item in str1:
    dict1[item] = dict1.get(item, 0) + 1
for item in str2:
    dict2[item] = dict2.get(item, 0) + 1
for item in dict1.keys():
    if item in dict2.keys():
        if dict1[item] != dict2[item]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

# 개선 2
"""
1.dict를 2개 만들었는데 1개로만 값을 비교
2.아나그램인지 판별하는 코드를 단순화 
"""
str1 = str(sys.stdin.readline().strip())
str2 = str(sys.stdin.readline().strip())
stringHash = dict()

for item in str1:
    stringHash[item] = stringHash.get(item, 0) + 1
for item in str2:
    stringHash[item] = stringHash.get(item, 0) - 1
for item in str1:
    if stringHash.get(item) > 0:
        print("NO")
        break
else:
    print("YES")
