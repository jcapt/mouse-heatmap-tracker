import pyautogui
from db import save_motion
from time import sleep

class Tracker:
	def __init__(self):
		self.last_x = 0
		self.last_y = 0
		self.data = []

	def track(self):
		while True:
			x, y = pyautogui.position()
			if x != self.last_x and y != self.last_y:
				save_motion(self.data, x, y)
				self.last_x = x
				self.last_y = y
				yield x, y

			sleep(0.005)


if __name__ == "__main__":
	tracker = Tracker()

	for pos in tracker.track():
		print(pos)
