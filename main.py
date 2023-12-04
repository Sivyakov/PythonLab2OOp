class MyClass:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def get_info_string(self):
        return f"Поле 1: {self.field_1} часов, Поле 2: {self.field_2} минут"

    def calculate_total_minutes(self):
        return self.field_1 * 60 + self.field_2


field_1 = int(input("Введите значение поля 1 (количество часов): "))
field_2 = int(input("Введите значение поля 2 (количество минут): "))

my_object = MyClass(field_1, field_2)

print(my_object.get_info_string())
print("Общее количество минут:", my_object.calculate_total_minutes())
