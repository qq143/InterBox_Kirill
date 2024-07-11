# в терминале -> 'pip install requests'
import requests


def countries_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    return response.json()


def filter(name):
    # меняем для сортировки Å на A, иначе Åland Islands будет в самом низу
    return name.replace("Å", "A")


def print_table(countries):

    for country in countries:
        country['normalized_name'] = filter(country['name']['common'])

    countries_sorted = sorted(countries, key=lambda x: x['normalized_name'].lower())

    max_country_len = max(len(country['name']['common']) for country in countries_sorted)
    max_capital_len = max(
        len(country.get('capital', [''])[0]) if 'capital' in country else 0 for country in countries_sorted)
    max_flag_len = 60

    print(f"{'Country Name':<{max_country_len}} {'Capital':<{max_capital_len}} {'Flag Image URL':<{max_flag_len}}")
    print('-' * (max_country_len + max_capital_len + max_flag_len))

    for country in countries_sorted:
        name = country['name']['common']
        capital = country.get('capital', ['N/A'])[0] if 'capital' in country else 'N/A'
        flag_url = country.get('flags', {}).get('png', 'N/A')
        print(f"{name:<{max_country_len}} {capital:<{max_capital_len}} {flag_url:<{max_flag_len}}")


if __name__ == "__main__":
    countries = countries_data()
    print_table(countries)
