#!/usr/bin/env python
from collections import OrderedDict
import json
import config
import os
import copy


def min30_rank() -> dict:
    """
    :return: 30分整地量ランキング
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


def sort_dict(d: dict) -> dict:
    """
    :param d: ソート元
    :return: ソート結果
    """
    return OrderedDict(sorted(d.items(), key=lambda x: x[1]["data"], reverse=True))


def add_dict(d1: dict, d2: dict) -> dict:
    """
    d1とd2の中身を加算する．
    :param d1:
    :param d2:
    :return: 加算結果
    """
    add_d = copy.deepcopy(d1)
    for uuid, v in d2.items():
        if uuid not in d1:
            add_d[uuid] = v
        else:
            add_d[uuid]["data"] = d1[uuid]["data"] + d2[uuid]["data"]

    return add_d


def sub_dict(d1: dict, d2: dict) -> dict:
    """
    d1とd2の中身を減算する．0以下の要素は消される．
    :param d1:
    :param d2:
    :return: 減算結果
    """
    sub_d = copy.deepcopy(d1)
    for uuid, v in d2.items():
        if uuid not in d1:
            continue
        else:
            sub_d[uuid]["data"] = d1[uuid]["data"] - d2[uuid]["data"]
            if sub_d[uuid]["data"] <= 0:
                sub_d.pop(uuid, 'no key')
    return sub_d


def update_mcid(d1: dict, d2: dict) -> dict:
    new_d = copy.deepcopy(d1)
    print(new_d)

    for uuid, v in d2.items():
        if uuid not in d1:
            continue
        new_d[uuid]["name"] = d2[uuid]["name"]

    print(new_d)
    return new_d


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
