import requests
from IPython import embed
from datetime import datetime, timedelta

# FIRST_DATE_FILL_API = "2013/06/12"
# END_DATE_FILL_API = datetime.now().strftime("%Y/%m/%d")




# Como usar o requests

COIN = "BTC"
year, month, day = 2013, 1, 1
datetime_object = datetime.strptime(f"{year}/{month}/{day}", "%Y/%m/%d")  # %Yyyy-%mm-%dd
datetime_str = str(datetime_object).split()[0].replace("-", "/")# %Yyyy/%mm/%dd  , segundos deixados de lado
status_code = 404   # 404 = Not Found, 200 = OK, enquanto 404 requisição não feita

while status_code != 200:
    print(datetime_str)


    endpoint = f"https://www.mercadobitcoin.net/api/{COIN}/day-summary/{datetime_str}/"
    response = requests.get(endpoint)

    status_code = response.status_code

    datetime_object += timedelta(days=1)
    datetime_str = str(datetime_object).split()[0].replace("-", "/")
    

first_day_api = response.json()
