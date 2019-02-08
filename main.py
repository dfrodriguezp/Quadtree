import quadtree
import numpy
from matplotlib import pyplot
from matplotlib.patches import Rectangle

l = 10
sq = quadtree.Square(l/2, l/2, l/2)
qt = quadtree.QuadTree(sq)

points = list()
for i in range(10):
    p = quadtree.Point(numpy.random.uniform(l), numpy.random.uniform(l))
    points.append(p)
    qt.insert(p)

pyplot.figure()
qt.show()
for p in points:
    p.show()
pyplot.xlim(-0.5, l + 0.5)
pyplot.ylim(-0.5, l + 0.5)
pyplot.gca().set_aspect('equal')
pyplot.show()

