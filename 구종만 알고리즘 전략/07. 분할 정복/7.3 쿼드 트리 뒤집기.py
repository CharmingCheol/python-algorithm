import sys

for i in range(int(sys.stdin.readline())):
    index = 0


    def reverse(word):
        global index
        if word[index] != "x":
            index += 1
            return word[index - 1]
        else:
            index += 1
            ul = reverse(word)
            ur = reverse(word)
            dl = reverse(word)
            dr = reverse(word)
        return "x" + dl + dr + ul + ur


    word = sys.stdin.readline().strip()
    print(reverse(word))
    index = 0

"""
w
xbwwb
xbwxwbbwb
xxwwwbxwxwbbbwwxxxwwbbbwwwwbb
"""