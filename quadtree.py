import matplotlib.pyplot as pyplot
from matplotlib.patches import Rectangle as rect

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        pyplot.scatter(self.x, self.y)

class Square(object):
    def __init__(self, x, y, halflength):
        self.x = x
        self.y = y
        self.hl = halflength

    def containsPoint(self, point):
        if (point.x < self.x - self.hl or point.y < self.y - self.hl or
            point.x > self.x + self.hl or point.y > self.y + self.hl):
            return False
        return True

    def show(self):
        x, y = self.x - self.hl, self.y - self.hl
        pyplot.gca().add_patch(rect((x, y), self.hl * 2, self.hl * 2, facecolor='none'))

        

class QuadTree(object):
    def __init__(self, boundary):
        self.boundary = boundary
        self.capacity = 2
        self.points = list()
        self.northwest = None
        self.northeast = None
        self.southwest = None
        self.southeast = None


    def subdivide(self):
        nw_x = self.boundary.x - self.boundary.hl / 2
        nw_y = self.boundary.y + self.boundary.hl / 2
        self.northwest = QuadTree(Square(nw_x, nw_y, self.boundary.hl / 2))

        ne_x = self.boundary.x + self.boundary.hl / 2
        ne_y = self.boundary.y + self.boundary.hl / 2
        self.northeast = QuadTree(Square(ne_x, ne_y, self.boundary.hl / 2))

        sw_x = self.boundary.x - self.boundary.hl / 2
        sw_y = self.boundary.y - self.boundary.hl / 2
        self.southwest = QuadTree(Square(sw_x, sw_y, self.boundary.hl / 2))

        se_x = self.boundary.x + self.boundary.hl / 2
        se_y = self.boundary.y - self.boundary.hl / 2
        self.southeast = QuadTree(Square(se_x, se_y, self.boundary.hl / 2))

    def insert(self, point):
        if (not self.boundary.containsPoint(point)):
            return False

        if (len(self.points) < self.capacity and self.northwest == None):
            self.points.append(point)
            return True

        if (self.northwest == None):
            self.subdivide()

        if (self.northwest.insert(point)):
            return True
        if (self.northeast.insert(point)):
            return True
        if (self.southwest.insert(point)):
            return True
        if (self.southeast.insert(point)):
            return True

        return False

    def show(self):
        self.boundary.show()
        self.northwest.boundary.show()
        self.northeast.boundary.show()
        self.southwest.boundary.show()
        self.southeast.boundary.show()