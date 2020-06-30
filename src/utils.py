#!/usr/bin/env python
import requests
from collections import OrderedDict, Counter
import json
import config
import os


# uuid取得用
uuid_url = "https://api.mojang.com/user/profiles/"
# mcid取得用
name_url = "https://api.mojang.com/users/profiles/minecraft/"


def min30_rank() -> dict:
    """
    :return: 日間整地量ランキング
    """
    return read_file(config.min30_path) if os.path.exists(config.min30_path) else {}


def daily_rank() -> dict:
    """
    :return: 日間整地量ランキング
    """
    return read_file(config.daily_path) if os.path.exists(config.daily_path) else {}


def weekly_rank() -> dict:
    """
    :return: 週間整地量ランキング
    """
    return read_file(config.weekly_path) if os.path.exists(config.weekly_path) else {}


def monthly_rank() -> dict:
    """
    :return: 月間整地量ランキング
    """
    return read_file(config.monthly_path) if os.path.exists(config.monthly_path) else {}


def daily_reply(uuid: str) -> str:
    """
    :param uuid: 日間整地量を表示させたいuuid
    :return: 指定uuidの日間整地量
    """
    return ("daily: " + str(daily_rank()[uuid]) + "\n") if uuid in daily_rank() else "daily: 0\n"


def weekly_reply(uuid: str) -> str:
    """
    :param uuid: 週間整地量を表示させたいuuid
    :return: 指定uuidの週間整地量
    """
    return ("weekly: " + str(weekly_rank()[uuid]) + "\n") if uuid in weekly_rank() else "weekly: 0\n"


def monthly_reply(uuid: str) -> str:
    """
    :param uuid: 月間整地量を表示させたいuuid
    :return: 指定uuidの月間整地量
    """
    return ("monthly: " + str(monthly_rank()[uuid]) + "\n") if uuid in monthly_rank() else "monthly: 0\n"


def sort_dict(d: dict) -> dict:
    """
    :param d: ソート元
    :return: ソート結果
    """
    return OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))


def add_dict(d1: dict, d2: dict) -> dict:
    """
    d1とd2の中身を加算する．
    :param d1:
    :param d2:
    :return: 加算結果
    """
    return dict(Counter(d1) + Counter(d2))


def sub_dict(d1: dict, d2: dict) -> dict:
    """
    d1とd2の中身を減算する．0以下の要素は消される．
    :param d1:
    :param d2:
    :return: 減算結果
    """
    return dict(Counter(d1) - Counter(d2))


def uuid_to_name(uuid: str) -> str:
    """
    uuidから最新のmcidを取得
    :param uuid: mcidを取得したいuuid
    :return: uuidに対応したmcid
    """
    r_get = requests.get(uuid_url + uuid + "/names")
    return r_get.json()[len(r_get.json()) - 1]["name"]


def name_to_uuid(name: str) -> str:
    """
    mcidからuuidを取得
    :param name: uuidを取得したいmcid
    :return: mcidに対応したuuid
    """
    r_get = requests.get(name_url + name)
    print(r_get.status_code)
    if r_get.status_code != requests.codes.ok:
        return "#null"
    return r_get.json()["id"]


def read_file(path: str) -> dict:
    """
    jsonファイルを安全に読み込む
    :param path: 読み込むjsonファイルの位置
    :return: jsonファイルの中身
    """
    with open(path, "r") as f:
        return json.load(f)


def write_file(path: str, d: dict):
    """
    jsonファイルに安全に書き込む
    :param path: 書き込むjsonファイルの位置
    :param d: 書き込む内容
    """
    with open(path, "w") as f:
        json.dump(d, f, indent=4)

