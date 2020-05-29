# 5

f = open('C:/Users/Dell/Desktop/lab11/f.txt','r')
f_s = f.read()
c = 0
for i in f_s:
    if i.isalpha():
            c += 1
g = open('C:/Users/Dell/Desktop/lab11/g.txt', 'w')
g.write(f"{c}")