# -*- coding: utf-8 -*-
"""
@Project ：BJUT_login 
@File    ：world.py
@Author  ：Knkiss
@Date    ：2023/3/28 21:41 
"""
import ssl

LGN_LOGIN_URL = 'https://lgn.bjut.edu.cn/'
LGN_LOGOUT_URL = 'https://lgn.bjut.edu.cn/F.htm'
SIMULATED_UA = 'Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# 校园网账号密码
# account_number = "S2022_____"
# account_password = "__________"
