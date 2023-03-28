# -*- coding: utf-8 -*-
"""
@Project ：BJUT_login 
@File    ：log_out.py
@Author  ：Knkiss
@Date    ：2023/3/28 21:32 
"""
from urllib import request

import world


def gateway_logout():
    req = request.Request(world.LGN_LOGOUT_URL)
    req.add_header('User-Agent', world.SIMULATED_UA)
    f = request.urlopen(req, context=world.context)
    data = f.read().decode('gb2312')
    if data.find('Msg=14') != -1:
        print('Logout succeed')
    else:
        print('Logout failed, have you already logged out?')


if __name__ == '__main__':
    gateway_logout()
