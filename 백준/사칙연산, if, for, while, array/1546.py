count = int(input())
test = list(map(int, input().split()))
max_value = max(test)

for i in range(count):
    test[i] = int(test[i] / max_value * 100)
print("%.2f" %(sum(test) / count))
