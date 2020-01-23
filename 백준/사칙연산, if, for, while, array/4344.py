R = int(input())
for i in range(R):
    test = list(map(int, input().split()))
    avg = (sum(test) - test[0]) / test[0]
    count = 0
    for j in range(test[0]):
        if test[j + 1] > avg:
            count += 1
    print(str("%.3f" % round(count / test[0] * 100, 3)) + "%")
