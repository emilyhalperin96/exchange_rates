#import requests 
from openexchange import OpenExchangeClient

APP_ID = 'cc6fc36a309d4ff8a7a37a0b34f6c265'

#ENDPOINT = 'https://openexchangerates.org/api/latest.json'

#response = requests.get(f'{ENDPOINT}?app_id={APP_ID}')
#exchange_rates = response.json()['rates']

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
#gbp_amount = usd_amount * exchange_rates['GBP']

gbp_amount = client.convert(usd_amount, 'USD', 'GBP')

print(f'USD{usd_amount} is GBP{gbp_amount}')
