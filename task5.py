class Stationary:
    title = None

    def __init__(self, title=None):
        Stationary.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationary):
    def draw(self):
        print(self.title)


class Pencil(Stationary):
    def draw(self):
        print(self.title)


class Marker(Stationary):
    def draw(self):
        print(self.title)


stationary = Stationary()
stationary.draw()

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

marker = Marker('Маркер')
marker.draw()


