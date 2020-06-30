import requests
from utils import *

url = "https://w4.minecraftserver.jp/api/ranking"
payload = {"type": "break", "duration": "daily"}    # 日間整地ランキング

daily_path = ".json/daily.json"
weekly_path = ".json/weekly.json"
monthly_path = ".json/monthly.json"
min30_path = ".json/min30.json"


def update_ranking():
    b_daily_rank = daily_rank()

    r_get = requests.get(url, params=payload)
    if r_get.status_code != requests.codes.ok:
        return
    r_json = r_get.json()
    ranks = r_json["ranks"].copy()
    while len(r_json["ranks"]) > 99:
        next_p = {"type": "break", "offset": str(len(ranks) - 1), "duration": "daily"}
        r_get = requests.get(url, params=next_p)
        r_json = r_get.json()
        ranks.extend(r_json["ranks"].copy())

    result = {}
    for rank in ranks:
        result[rank["player"]["uuid"].replace("-", "")] = int(rank["data"]["raw_data"])

    diff_daily = sort_dict(sub_dict(result, b_daily_rank))  # 更新前との差分

    # 各ランキング更新
    write_file(daily_path, sort_dict(result))
    write_file(weekly_path, sort_dict(add_dict(weekly_rank(), diff_daily)))
    write_file(monthly_path, sort_dict(add_dict(monthly_rank(), diff_daily)))
    write_file(min30_path, diff_daily)
    
update_ranking()
