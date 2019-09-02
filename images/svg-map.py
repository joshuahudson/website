from sys import argv

width = 1828.8
height = 1219.2

a = argv[1]

a = a.split(' ') ; 
b = [k.split(',') for k in a]; 

trans = argv[2]
trans = trans.split(',')
trans = [float(trans[0]), float(trans[1])]

conv = lambda b,i: ((float(b[i][0]) + trans[0]) / width * width, (float(b[i][1]) + trans[1]) / height * height)

x, y = conv(b,0); #y = height - y; 
c = [str(int(x)) + ',' + str(int(y))]
for i in range(1,len(b)):
    dx, dy = conv(b,i)
    x = x + dx; y = y + dy
    c.append(str(int(x)) + ',' + str(int(y)))
print(",".join(c))
