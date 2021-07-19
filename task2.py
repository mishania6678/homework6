class Road:
    _length, _width = 0, 0

    def __init__(self, length, width):
        Road._length, Road._width = length, width

    def density_calc(self, m, n):
        return Road._length * Road._width * m * n


road = Road(20, 5000)
print(road.density_calc(25, 5))
