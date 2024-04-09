class Country:
    def __init__(self, name, xl, yl, xh, yh):
        # Ініціалізація атрибутів об'єкта страна
        self.name = name  # Назва країни
        self.xl = xl  # Нижня границя координати x
        self.yl = yl  # Нижня границя координати y
        self.xh = xh  # Верхня границя координати x
        self.yh = yh  # Верхня границя координати y
        self.days_to_finish = 0  # Кількість днів для завершення обігу монет в країні

class CoinSimulator:
    @staticmethod
    def calculate_days_to_finish(countries):
        # Розрахунок кількості днів для завершення обігу монет для кожної країни
        for country in countries:
            # Перевірка наявності всіх координат
            if None in [country.xl, country.yl, country.xh, country.yh]:
                print(f"Помилка: Не всі координати визначені для країни {country.name}")
                continue
            # Розрахунок кількості монет
            total_coins = (country.xh - country.xl + 1) * (country.yh - country.yl + 1) * 1000000
            # Розрахунок днів на основі 1000 монет на 1 день
            country.days_to_finish = total_coins // 1000  

    @staticmethod
    def sort_countries(countries):
        # Сортування країн за кількістю днів для завершення обігу монет та їх назвами
        return sorted(countries, key=lambda country: (country.days_to_finish, country.name))

    @staticmethod
    def simulate_coin_distribution(countries, case_number):
        # Розрахунок кількості днів для завершення обігу монет
        CoinSimulator.calculate_days_to_finish(countries)
        # Сортування країн
        sorted_countries = CoinSimulator.sort_countries(countries)
        # Вивід результатів
        print(f"Номер випадку {case_number}")
        for country in sorted_countries:
            print(f"{country.name} {country.days_to_finish}")

def main():
    input_data = [
        # Приклади вхідних даних, які містять назви країн та їх координати
        (3, ["France", 1, 4, 4, 6], ["Spain", 3, 1, 6, 3], ["Portugal", 1, 1, 2, 2]),
        (1, ["Luxembourg", None, 1, 1, 1]),  # Помилка: Не всі координати визначені
        (2, ["Netherlands", 1, 3, 2, 4], ["Belgium", 1, 1, 2, 2])
    ]

    # Перебір вхідних даних та симуляція розподілу монет для кожного випадку
    for case_number, data in enumerate(input_data, start=1):
        countries = []
        # Отримання даних про країну та створення об'єктів країн
        for country_data in data[1:]:
            name = country_data[0]
            xl, yl, xh, yh = country_data[1:]
            country = Country(name, xl, yl, xh, yh)
            countries.append(country)
        # Симуляція розподілу монет та вивід результатів
        CoinSimulator.simulate_coin_distribution(countries, case_number)

if __name__ == "__main__":
    main()  # Виконання основної функції, якщо скрипт запущено як головна програма