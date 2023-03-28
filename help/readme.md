# 北工大校园网有线自动登录
### linux服务器脚本

---
## 简介
由于4090服务器不需要使用向日葵进行连接  
仅需要将其连接到校园内网即可进行访问  
所以4090仅在下载环境时候需要连接网络

## 使用
1. 修改`/code/world.py`的校园网账号密码
2. 运行`/code/log_in.py`即登录
3. 运行`/code/log_out.py`即注销
4. 运行`/code/log_state.py`即查询当前服务器网络连接状态

注释：如果报错无法登陆，请先尝试注销一遍。