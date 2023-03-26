import matplotlib.pyplot as plt
import numpy as np
import math

color = "GREEN"
v_line_min = -100
v_line_max = 100
h_line_min = -100
h_line_max = 100


def genCoordinates (sigma):
	return sigma * np.random.randn(), sigma * np.random.randn()

def getLengthBetweenCenterAndPoint (point):
	return math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))

def minimum(points):
	min = 0
	minPoint = ()
	for point in points:
		length = getLengthBetweenCenterAndPoint(point)
		if (min == 0):
			min = length
			minPoint = point
		else:
			if (length < min):
				min = length
				minPoint = point
	return min, minPoint

def maximum(points):
	max = 0
	maxPoint = ()
	for point in points:
		length = getLengthBetweenCenterAndPoint(point)
		if (max == 0):
			max = length
			maxPoint = point
		else:
			if (length > max):
				max = length
				maxPoint = point
	return max, maxPoint
	
def getInfoAboutPoints(ruleNumber, points):
	min, minPoint = minimum(points) 
	max, maxPoint = maximum(points)
	print("------------------------------------------------------------------")
	print(ruleNumber, " правило")
	print("Минимальная длина: ", min, 'Мин. точка: ', minPoint)
	print("Максимальная длина: ", max, 'Макс. точка: ', maxPoint)
	print("------------------------------------------------------------------")

#n - count of points
def buildFirstRule(n):
	points = []
	fig, ax = plt.subplots()
	ax.vlines(0, v_line_min, v_line_max)
	ax.hlines(0, h_line_min, h_line_max)
	plt.grid()
	for i in range(0, n):
		coordinatesPair = genCoordinates(6)
		points.append((coordinatesPair[0], coordinatesPair[1]))
		plt.scatter(coordinatesPair[0], coordinatesPair[1], c = color)

	plt.show()
	return points

def buildSecondRule (points):
	newPoints = []
	fig, ax = plt.subplots()
	ax.vlines(0, v_line_min, v_line_max)
	ax.hlines(0, h_line_min, h_line_max)
	funnel_x, funnel_y = 0, 0
	for i in range (0, len(points)):
		if (i == 0):
			x, y = points[0]
			funnel_x = -x
			funnel_y = -y
			plt.scatter(x, y, c = color)
			newPoints.append((x, y))
		else:
			x, y = points[i]
			new_x = x + funnel_x
			new_y = y + funnel_y
			funnel_x += (-new_x)
			funnel_y += (-new_y)
			plt.scatter(new_x, new_y, c = color)
			newPoints.append((new_x, new_y))
	plt.show()
	return newPoints		
	

def buildThirdAndFourthRule(points, isThird = True):
	newPoints = []
	fig, ax = plt.subplots()
	ax.vlines(0, v_line_min, v_line_max)
	ax.hlines(0, h_line_min, h_line_max)
	old_x, old_y = 0, 0

	for i in range (0, len(points)):
		curr_x, curr_y = points[i]
		if i == 0:
			plt.scatter(curr_x, curr_y, c = color)
			old_x, old_y = curr_x, curr_y
			newPoints.append((curr_x, curr_y))
		else:
			if (isThird): 
				new_x = curr_x + (-old_x)
				new_y = curr_y + (-old_y)
			else:
				new_x = curr_x + old_x
				new_y = curr_y + old_y
			plt.scatter(new_x, new_y, c = color)
			old_x, old_y = new_x, new_y
			newPoints.append((new_x, new_y))
	plt.show()
	return newPoints


def main():
	points = buildFirstRule(100)
	getInfoAboutPoints('1е', points)
	points2 = buildSecondRule(points)
	getInfoAboutPoints('2е',points2)
	points3 = buildThirdAndFourthRule(points)
	getInfoAboutPoints('3е',points3)
	points4 = buildThirdAndFourthRule(points, False)
	getInfoAboutPoints('4е',points4)

main()
	
