import requests 

APP_ID = 'cc6fc36a309d4ff8a7a37a0b34f6c265'
ENDPOINT = 'https://openexchangerates.org/api/latest.json'

response = requests.get(f'{ENDPOINT}?app_id={APP_ID}')
exchange_rates = response.json()['rates']

usd_amount = 1000
gbp_aount = usd_amount * exchange_rates['GBP']
