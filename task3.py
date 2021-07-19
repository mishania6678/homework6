class Worker:
    name = None
    surname = None
    position = None
    _income = None

    def __init__(self, name: str, surname: str, position: str, income: dict):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position
        Worker._income = income


class Position(Worker):
    def get_full_name(self):
        return Worker.surname + ' ' + Worker.name

    def get_total_income(self):
        return Worker._income['salary'] + Worker._income['bonus']


worker1 = Position('Иван', 'Иванов', 'плотник', {'salary': 15000, 'bonus': 4000})
print(worker1.get_full_name())
print(worker1.get_total_income())

print()

worker2 = Position('Петр', 'Петров', 'дровосек', {'salary': 14000, 'bonus': 5000})
print(worker2.get_full_name())
print(worker2.get_total_income())
