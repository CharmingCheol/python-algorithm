x_array = []
y_array = []
for i in range(3):
    x,y = map(int, input().split())
    x_array.append(x)
    y_array.append(y)
for j in range(3):
    if x_array.count(x_array[j]) == 1:
        x = x_array[j]
    if y_array.count(y_array[j]) == 1:
        y = y_array[j]
print(x, y)