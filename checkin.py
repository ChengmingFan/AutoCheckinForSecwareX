#! /usr/bin/env python3
# ! encoding=utf-8

import requests
import time
import json
from datetime import datetime
import random

url_scan = "https://api.secwarex.io/api/v1/secwarex/riskDetection/scanAddress"


def scan(_address, _token):
    timestamp = int(time.time_ns() / 1e6)
    data = {
        "X-Address": _address,
        "X-Project": "secwarex",
        "language": "cn",
        "manageId": "100004",
        "timestamp": timestamp
    }

    resp = requests.post(url=url_scan, data=json.dumps(data), headers={
        "X-Project": "secwarex",
        "Token": _token
    })
    if (resp.status_code == 200):
        print(f"- {_address}: Success")
    else:
        print(f"- {_address}: Failed")
    return resp.json()


if __name__ == "__main__":
    print("================================================")
    print(f"{datetime.now().date()}'s secwarex checkin start at {datetime.now()}")
    addresses = []
    tokens = []
    with open('addresses.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            addresses.append(line)
    with open('tokens.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            tokens.append(line)
    for (address, token) in zip(addresses, tokens):
        scan(address, token)
        # 生成随机的暂停时间，范围为 10 到 60 秒
        random_sleep_time = random.randint(10, 60)

        # 暂停一段随机时间
        print(f"Waiting for {random_sleep_time} seconds...")
        time.sleep(random_sleep_time)

    print(f"{datetime.now().date()}'s secwarex checkin end at {datetime.now()}")