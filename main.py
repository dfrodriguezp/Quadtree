from quadtree import Point, Square, Quadtree
from numpy import random
from matplotlib import pyplot

l = 10
sq = Square(l/2, l/2, l/2)
qtree = Quadtree(sq)

points = list()
for i in range(100):
    p = Point(random.uniform(0, l), random.uniform(0, l))
    points.append(p)
    qtree.insert(p)

area = Square(random.uniform(0, l), random.uniform(0, l), random.uniform(3))
points_in_area = qtree.query(area)

pyplot.figure()
for p in points:
    p.show()
for p in points_in_area:
    p.show("red")
qtree.show()
area.show("red")
pyplot.xlim(-0.5, l + 0.5)
pyplot.ylim(-0.5, l + 0.5)
pyplot.gca().set_aspect('equal')
pyplot.savefig("img.png")
pyplot.show()
pyplot.close()

