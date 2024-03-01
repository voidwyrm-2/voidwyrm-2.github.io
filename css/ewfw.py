step = 1


out = ''


for i in range(100):
    if bool(i % 2):
        out += str(i) + '''% {
    left: 350px;
}\n'''
    else:
        out += str(i) + '''% {
    left: 330px;
}\n'''


with open('hefwfwe.txt', 'xt') as f: f.write(out)