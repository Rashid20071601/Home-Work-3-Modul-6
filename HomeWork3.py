class Horse:
    # Инициализация класса Horse
    def __init__(self):
        # x_distance - расстояние, которое прошла лошадь
        self.x_distance = 0
        # sound - звук, издаваемый лошадью
        self.sound = 'Frrr'

    # Метод для перемещения лошади
    def run(self, dx):
        # Увеличиваем пройденное расстояние на значение dx
        self.x_distance += dx


class Eagle:
    # Инициализация класса Eagle
    def __init__(self):
        # y_distance - высота полета орла
        self.y_distance = 0
        # sound - звук, издаваемый орлом
        self.sound = 'I train, eat, sleep, and repeat'

    # Метод для изменения высоты полета орла
    def fly(self, dy):
        # Увеличиваем высоту полета на значение dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    # Инициализация класса Pegasus
    def __init__(self):
        # Инициализируем атрибуты от Horse и Eagle
        Horse.__init__(self)
        Eagle.__init__(self)

    # Метод для одновременного передвижения по горизонтали и высоте
    def move(self, dx, dy):
        # Используем метод run из Horse для перемещения по горизонтали
        self.run(dx)
        # Используем метод fly из Eagle для изменения высоты
        self.fly(dy)

    # Метод для получения текущего положения (x, y)
    def get_pos(self):
        # Возвращаем кортеж с текущим значением x_distance и y_distance
        return (self.x_distance, self.y_distance)

    # Метод для издания звука
    def voice(self):
        # Выводим значение атрибута sound (будет использоваться значение из первого родительского класса)
        print(self.sound)


# Проверяем порядок разрешения методов (Method Resolution Order)
print(Pegasus.mro())  # Выведет порядок поиска методов и атрибутов в иерархии наследования

# Создаем объект класса Pegasus
p1 = Pegasus()

# Выводим начальную позицию (0, 0)
print(p1.get_pos())
# Перемещаем пегаса на 10 единиц по горизонтали и на 15 по вертикали
p1.move(10, 15)
print(p1.get_pos())  # (10, 15)
# Перемещаем пегаса на -5 единиц по горизонтали и на 20 по вертикали
p1.move(-5, 20)
print(p1.get_pos())  # (5, 35)

# Пегас издает звук
p1.voice()  # I train, eat, sleep, and repeat
