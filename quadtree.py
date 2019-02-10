from matplotlib import pyplot
from matplotlib.patches import Rectangle as rect

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self, color=None):
        pyplot.scatter(self.x, self.y, color=color)

class Square(object):
    def __init__(self, x, y, halflength):
        self.x = x
        self.y = y
        self.hl = halflength

    def containsPoint(self, point):
        return not (point.x < self.x - self.hl or point.y < self.y - self.hl or
            point.x > self.x + self.hl or point.y > self.y + self.hl)

    def intersects(self, other):
        x = self.x - self.hl
        other_x = other.x - other.hl
        y = self.y - self.hl
        other_y = other.y - other.hl

        return ((x <= other_x + other.hl*2 and x >= other_x) or
            (y <= other_y + other.hl*2 and y >= other_y) or
            (other_x <= x + self.hl*2 and other_x >= x) or
            (other_y <= y + self.hl*2 and other_y >= y))

    def show(self, edgecolor=None):
        x, y = self.x - self.hl, self.y - self.hl
        pyplot.gca().add_patch(rect((x, y), self.hl * 2, self.hl * 2, facecolor='none', edgecolor=edgecolor))

class Quadtree(object):
    def __init__(self, boundary):
        self.boundary = boundary
        self.capacity = 4
        self.points = list()
        self.divided = False

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        hl = self.boundary.hl

        nw_x = x - hl / 2
        nw_y = y + hl / 2
        self.northwest = Quadtree(Square(nw_x, nw_y, hl / 2))

        ne_x = x + hl / 2
        ne_y = y + hl / 2
        self.northeast = Quadtree(Square(ne_x, ne_y, hl / 2))

        sw_x = x - hl / 2
        sw_y = y - hl / 2
        self.southwest = Quadtree(Square(sw_x, sw_y, hl / 2))

        se_x = x + hl / 2
        se_y = y - hl / 2
        self.southeast = Quadtree(Square(se_x, se_y, hl / 2))
        self.divided = True

    def insert(self, point):
        if (not self.boundary.containsPoint(point)):
            return False

        if (len(self.points) < self.capacity and not self.divided):
            self.points.append(point)
            return True

        if (not self.divided):
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

    def query(self, range):
        points = list()
        if (not self.boundary.intersects(range)):
            return points

        for p in self.points:
            if (range.containsPoint(p)):
                points.append(p)

        if (not self.divided):
            return points

        for p in self.northwest.query(range):
            points.append(p)
        for p in self.northeast.query(range):
            points.append(p)
        for p in self.southwest.query(range):
            points.append(p)
        for p in self.southeast.query(range):
            points.append(p)

        return points



    def show(self):
        x, y = self.boundary.x - self.boundary.hl, self.boundary.y - self.boundary.hl
        pyplot.gca().add_patch(rect((x, y), self.boundary.hl * 2, self.boundary.hl * 2, facecolor='none'))

        if (self.divided):
            self.northwest.show()
            self.northeast.show()
            self.southwest.show()
            self.southeast.show()

        # for p in self.points:
        #     pyplot.scatter(p.x, p.y, color="red")