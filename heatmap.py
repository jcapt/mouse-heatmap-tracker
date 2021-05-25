import matplotlib.pyplot as plt
import numpy as np
import csv

def gen_heatmap():
	xs = []
	ys = []
	arr = []

	with open("chunk.csv", "r") as f:
		reader = csv.reader(f)
		for row in reader:
			x = int(row[0])
			xs.append(x)
			y = int(row[1])
			ys.append(y)
			arr.append([x, y])

	nxs = np.array(xs)
	print(np.matrix(nxs))
	nys = np.array(ys)

	print(nxs.shape)

	plt.hist2d(nxs, nys, bins=40)

	plt.show()

if __name__ == "__main__":
	gen_heatmap()
