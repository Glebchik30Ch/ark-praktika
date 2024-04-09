class Country:
    def __init__(self, name, xl, yl, xh, yh):
        # Инициализация атрибутов объекта страны
        self.name = name  # Название страны
        self.xl = xl  # Нижняя граница координаты x
        self.yl = yl  # Нижняя граница координаты y
        self.xh = xh  # Верхняя граница координаты x
        self.yh = yh  # Верхняя граница координаты y
        self.days_to_finish = 0  # Инициализация количества дней, необходимых для завершения обращения монет в стране

def calculate_days_to_finish(countries):
    # Рассчет количества дней, необходимых для завершения обращения монет для каждой страны
    for country in countries:
        # Общее количество монет в стране
        total_coins = (country.xh - country.xl + 1) * (country.yh - country.yl + 1) * 1000000
        # Рассчет дней на основе представительной части: 1 монета на каждые 1000 монет
        country.days_to_finish = total_coins // 1000  

def simulate_coin_distribution(countries, case_number):
    # Сортировка стран по количеству дней до завершения обращения монет и их названиям
    calculate_days_to_finish(countries)
    sorted_countries = sorted(countries, key=lambda country: (country.days_to_finish, country.name))
    # Вывод номера случая
    print(f"Case Number {case_number}")
    # Вывод названий стран и соответствующего количества дней до завершения обращения монет
    for country in sorted_countries:
        print(f"{country.name} {country.days_to_finish}")

def main():
    input_data = [
        # Пример входных данных, содержащих названия стран и их координаты
        (3, ["France", 1, 4, 4, 6], ["Spain", 3, 1, 6, 3], ["Portugal", 1, 1, 2, 2]),
        (1, ["Luxembourg", 1, 1, 1, 1]),
        (2, ["Netherlands", 1, 3, 2, 4], ["Belgium", 1, 1, 2, 2])
    ]

    case_number = 1
    # Перебор входных данных и симуляция распределения монет для каждого случая
    for data in input_data:
        c = data[0]  # Количество стран в случае
        countries = []
        # Извлечение данных о стране и создание объектов страны
        for country_data in data[1:]:
            name = country_data[0]
            xl, yl, xh, yh = country_data[1:]
            country = Country(name, xl, yl, xh, yh)
            countries.append(country)
        # Симуляция распределения монет и вывод результатов
        simulate_coin_distribution(countries, case_number)
        case_number += 1  # Увеличение номера случая для следующей итерации

if __name__ == "__main__":
    main()  # Выполнение основной функции, если скрипт запущен как основная программа
