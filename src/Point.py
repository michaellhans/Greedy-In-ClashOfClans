# Point.py
# Merepresentasikan titik dalam peta

class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x, y):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance(self, P):
        """ Compute my distance from the point P """
        return (((self.x - P.x) ** 2) + ((self.y - P.y) ** 2)) ** 0.5
