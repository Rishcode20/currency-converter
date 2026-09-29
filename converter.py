import requests

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"API request failed with status {response.status_code}")

    data = response.json()

    if 'rates' not in data or to_currency not in data['rates']:
        raise ValueError(f"Currency code '{to_currency}' not found")

    return data['rates'][to_currency]


def convert(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * rate
    return converted_amount

if __name__ == "__main__":
    result = convert(100, "USD", "CAD")
    print(f"100 USD = {result} CAD")