import requests
import json
import time
# 定义要发送的参数
params = {
    "username": "change to your phone number",
    "password": "change to your corresponded agent passward",
    "domain": "telecom"
}

# 定义请求的URL
url = "http://10.10.16.12/api/portal/v1/login"

# 发送POST请求

response = requests.post(url, data=json.dumps(params), headers={"Content-Type": "application/json"})
time.sleep(5)

