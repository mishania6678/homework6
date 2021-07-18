from time import sleep


class TrafficLight:
    __color = None

    def running(self):
        while True:
            self.switch('Красный', 7)
            self.switch('Желтый', 2)
            self.switch('Зеленый', 5)

    @staticmethod
    def switch(color, sleep_time):
        TrafficLight.__color = color
        print(TrafficLight.__color)
        sleep(sleep_time)


traffic_light = TrafficLight()
traffic_light.running()
