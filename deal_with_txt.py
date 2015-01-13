
from glob import glob

file_names = glob('score*')
#file_names = glob('industry*')
file_names.sort()

length = 3
pro = {}
stock = {}
date = {}

for i in range(len(file_names)):

	fname = file_names[i]

	date[fname[5:-4]] = -1

	f = open(fname, 'r')
	print fname
	stock_t = {}
	summ = 0
	while 1:
		line = f.readline()
		#print line
		if not line:
			break
		array = line[:-1].split('%')
		a = array[0].decode('utf-8')


		stock_t[a] = int(array[2])

		#print line
		summ += int(array[2])

	f = open('temp' + fname[5:-4] + '.txt', 'w')
	for key in stock_t:

		f.write(key.encode('utf-8') + '%' + str(stock_t[key]/float(summ)) + '\n')
