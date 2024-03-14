data = open('data.dat', 'w')

for i in range(31):
    for j in range(51):
        data.write(str(j) + '\n')
    data.write('\n')


data.close()
