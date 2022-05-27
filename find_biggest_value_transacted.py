import requests
from IPython import embed
from datetime import datetime, timedelta


END_DATE_FILL_API = (datetime.now() + timedelta(days=1)).strftime("%Y/%m/%d")
COIN = "BTC"
year, month, day = 2013, 6, 12
datetime_object = datetime.strptime(f"{year}/{month}/{day}", "%Y/%m/%d")  # %Yyyy-%mm-%dd
datetime_str = str(datetime_object).split()[0].replace("-", "/")# %Yyyy/%mm/%dd  , segundos deixados de lado


biggest_value_transacted = 0
while datetime_str != END_DATE_FILL_API:
    endpoint = f"https://www.mercadobitcoin.net/api/{COIN}/day-summary/{datetime_str}/"
    response_json = requests.get(endpoint).json()

    response_json_highest_field = response_json.get("highest")
    if response_json_highest_field > biggest_value_transacted:
        biggest_value_transacted = response_json_highest_field
        print(f"The hightest value until now is: {biggest_value_transacted}")

    datetime_object += timedelta(days=1)
    datetime_str = str(datetime_object).split()[0].replace("-", "/")
    

print(f"The hightest value transacted was: {biggest_value_transacted}")
