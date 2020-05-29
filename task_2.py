# 5

f1 = open('C:/Users/Dell/Desktop/lab11/f1.txt', 'r')
f1_s = f1.read()
h = open('C:/Users/Dell/Desktop/lab11/h.txt', 'w')
for i in range(0, len(f1_s) - 1, 2):
        h.write(f1_s[i])
f2 = open('C:/Users/Dell/Desktop/lab11/f2.txt', 'r')
f2_s = f2.read()
f1 = open('C:/Users/Dell/Desktop/lab11/f1.txt', 'w')
for i in range(0, len(f2_s) - 1, 2):
            f1.write(f2_s[i])
h = open('C:/Users/Dell/Desktop/lab11/h.txt', 'r')
h_s = h.read()
f2 = open('C:/Users/Dell/Desktop/lab11/f2.txt', 'w')
f2.write(h_s)