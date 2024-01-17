import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit()


try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


o = response.json()
rate = o["bpi"]["USD"]["rate"]
amount = float(rate.replace(",", "")) * number
print(f"${amount:,.4f}")