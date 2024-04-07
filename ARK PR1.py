class Country:
    def __init__(self, name, xl, yl, xh, yh):
        self.name = name
        self.xl = xl
        self.yl = yl
        self.xh = xh
        self.yh = yh
        self.days_to_finish = 0

def calculate_days_to_finish(countries):
    for country in countries:
        total_coins = (country.xh - country.xl + 1) * (country.yh - country.yl + 1) * 1000000
        # Розрахунок кількості днів для завершення обігу монет у країні
        country.days_to_finish = total_coins // 1000  # Репрезентативна частина: 1 монета на кожні 1000 монет

def simulate_coin_distribution(countries, case_number):
    calculate_days_to_finish(countries)
    sorted_countries = sorted(countries, key=lambda country: (country.days_to_finish, country.name))
    print(f"Case Number {case_number}")
    for country in sorted_countries:
        print(f"{country.name} {country.days_to_finish}")

def main():
    input_data = [
        (3, ["France", 1, 4, 4, 6], ["Spain", 3, 1, 6, 3], ["Portugal", 1, 1, 2, 2]),
        (1, ["Luxembourg", 1, 1, 1, 1]),
        (2, ["Netherlands", 1, 3, 2, 4], ["Belgium", 1, 1, 2, 2])
    ]

    case_number = 1
    for data in input_data:
        c = data[0]
        countries = []
        for country_data in data[1:]:
            name = country_data[0]
            xl, yl, xh, yh = country_data[1:]
            country = Country(name, xl, yl, xh, yh)
            countries.append(country)
        simulate_coin_distribution(countries, case_number)
        case_number += 1

if __name__ == "__main__":
    main()
