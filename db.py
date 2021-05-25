import time, csv


def save_motion(data, x, y):
	data.append([x, y])
	if len(data) > 1000:
		print("write event")
		with open("chunk.csv", "a") as f:
			writer = csv.writer(f)
			for row in data:
				writer.writerow(row)

		data.clear()
