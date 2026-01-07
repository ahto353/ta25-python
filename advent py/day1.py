f = open('example.txt', 'r')
'''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''
start = 50
password = 0
for line in f.readlines():
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])
    if direction == 'L':
        start = (start - distance) % 100
    else:
        start = (start + distance) % 100

    print(line + ':', start)
              