#import requests 
from openexchange import OpenExchangeClient
import time

APP_ID = 'cc6fc36a309d4ff8a7a37a0b34f6c265'

#ENDPOINT = 'https://openexchangerates.org/api/latest.json'

#response = requests.get(f'{ENDPOINT}?app_id={APP_ID}')
#exchange_rates = response.json()['rates']

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
#gbp_amount = usd_amount * exchange_rates['GBP']
start_time = time.time()

gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
end_time = time.time()

print(end_time-start_time)
print(f'USD{usd_amount} is GBP{gbp_amount}')
