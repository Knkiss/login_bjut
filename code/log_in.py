# -*- coding: utf-8 -*-
"""
@Project ：BJUT_login 
@File    ：log_in.py
@Author  ：Knkiss
@Date    ：2023/3/28 21:21 
"""
import re
import sys
import urllib
from urllib import request

import world
from log_state import gateway_account_status


def gateway_login():
    # Get lgn login page's content
    req = request.Request(world.LGN_LOGIN_URL)
    req.add_header('User-Agent', world.SIMULATED_UA)
    f = request.urlopen(req, context=world.context)
    data = f.read().decode('gb2312')

    # Get ipv4_server_ip from login page
    result = re.match(r'.*v4serip=\'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\'', data, re.DOTALL)
    if not result:
        if data.find('DispTFM') != -1:
            print('Error: re.match get ipv4_server_ip failed, have you already logged in?\n'
                  'Please use the following command to logout if you want:\n'
                  '\t', sys.argv[0], '--logout\n')
            print('Trying to get current logged in account status ...')
            gateway_account_status()
        else:
            print('Error: re.match get ipv4_server_ip failed')
        return -1

    ipv4_server_ip = result.groups()[0]
    print('ipv4_server_ip =', ipv4_server_ip)
    '''
    # POST data to lgn6 jumping page
    req = request.Request(LGN6_JUMPING_URL)
    req.add_header('User-Agent', SIMULATED_UA)
    post_data = {'DDDDD': username, 'upass': password, 'v46s': '0', 'v6ip': '', 'f4serip': ipv4_server_ip, '0MKKey': ''}
    post_data = urllib.parse.urlencode(post_data).encode()
    f = request.urlopen(req, post_data,context=context)
    data = f.read().decode('gb2312')

    # Get ipv6_server_ip from lgn6 jumping page
    result = re.match(r'.*name=\'v6ip\' value=\'(.+?)\'', data, re.DOTALL)
    if not result:
        print('Error: re.match get ipv6_server_ip failed, abort')
        sys.exit(1)

    ipv6_server_ip = result.groups()[0]
    print('ipv6_server_ip =', ipv6_server_ip)
    '''
    # POST data to final lgn login page
    req = request.Request(world.LGN_LOGIN_URL)
    req.add_header('User-Agent', world.SIMULATED_UA)
    post_data = {'DDDDD': world.account_number, 'upass': world.account_password, '0MKKey': 'Login', 'v6ip': ''}
    post_data = urllib.parse.urlencode(post_data).encode()
    f = request.urlopen(req, post_data, context=world.context)
    data = f.read().decode('gb2312')
    if data.find('successfully logged') != -1:
        print('Login succeed, Welcome to the Internet!\n')
        gateway_account_status()
    elif data.find('Msg=01') != -1:
        print('Error: wrong password')
        return 1
    elif data.find('Msg=04') != -1:
        print('Error: server says: Insufficient account balance')
        return 4
    else:
        print('--- final LGN login page content dump - START')
        print(data)
        print('--- final LGN login page content dump - END')
        print('\nError: unknown error, page content dumped')
        return -2


if __name__ == '__main__':
    gateway_login()
