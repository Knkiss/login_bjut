# -*- coding: utf-8 -*-
"""
@Project ：BJUT_login 
@File    ：log_state.py
@Author  ：Knkiss
@Date    ：2023/3/28 21:34 
"""
import re
import sys
from urllib import request

import world


def gateway_account_status():
    req = request.Request(world.LGN_LOGIN_URL)
    req.add_header('User-Agent', world.SIMULATED_UA)
    f = request.urlopen(req, context=world.context)
    data = f.read().decode('gb2312')
    # print(data)
    result = re.match(r'.*time=\'(.+?)\s*\';', data, re.DOTALL)
    if not result:
        print('Error: re.match get account info failed, abort')
        sys.exit(1)
    used_time = int(result.groups()[0])
    used_traffic = int(re.match(r'.*flow=\'(.+?)\s*\';', data, re.DOTALL).groups()[0]) / 1024
    account_balance = int(re.match(r'.*fee=\'(.+?)\s*\';', data, re.DOTALL).groups()[0]) / 10000

    print("=== Account status =========================================")
    print(" Connected time:       %d mins (%d hours and %d mins)" % (used_time, used_time // 60, used_time % 60))
    print(" Traffic used:          %.2f GiB (%d GiB and %d MiB)" % (
        used_traffic / 1024, used_traffic // 1024, used_traffic % 1024))
    print(" Account balance:      %d Yuan" % account_balance)
    print("=============================================================")


if __name__ == '__main__':
    gateway_account_status()
