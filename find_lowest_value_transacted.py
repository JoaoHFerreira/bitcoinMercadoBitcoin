import requests
from datetime import datetime, timedelta

END_DATE_FILL_API = (datetime.now() + timedelta(days=1)).strftime("%Y/%m/%d")
COIN = "BTC"
year, month, day = 2013, 6, 12
datetime_object = datetime.strptime(f"{year}/{month}/{day}", "%Y/%m/%d")  # %Yyyy-%mm-%dd
datetime_str = str(datetime_object).split()[0].replace("-", "/")# %Yyyy/%mm/%dd  , segundos deixados de lado


lowest_value_transacted = 1000000000
while datetime_str != END_DATE_FILL_API:
    print (datetime_str)
    endpoint = f"https://www.mercadobitcoin.net/api/{COIN}/day-summary/{datetime_str}/"
    response_json = requests.get(endpoint).json()

    response_json_lowest_field = response_json.get("lowest")
    if response_json_lowest_field < lowest_value_transacted:
        lowest_value_transacted = response_json_lowest_field
        print(f"The lowest value until now is: {lowest_value_transacted}")

    datetime_object += timedelta(days=1)
    datetime_str = str(datetime_object).split()[0].replace("-", "/")
    

print(f"The lowest value transacted was: {lowest_value_transacted}")