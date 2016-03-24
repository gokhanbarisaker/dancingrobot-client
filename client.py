
# idea is simple - if there is a data after last dance - Dance!

import requests
import time
from datetime import datetime

class DanceTiming(object):
    def __init__(self):
        self.refresh_dt()

    def _build_new_dt(self):
        lastdance = datetime.now()
        return lastdance.replace(microsecond=0)

    def refresh_dt(self):
        self.dt = self._build_new_dt()


class UrlBuilder(object):
    def build(dt):
        return 'https://api.github.com/repos/gokhanbarisaker/dancingrobot-client/commits?since=' + dt.isoformat() + 'Z'


class Ruler(object):
    def __init__(self, interval):
        self.timer = DanceTiming()
        self.interval = interval
        self.last_length = 0
        print("Long live the King!")

    def rule(self):
        print('Let the ruling began!')
        while 1==1:
            current_length = self.request_length()
            if self.last_length != current_length:
                self.timer.refresh_dt()
                self.dance()
                self.last_length = current_length
            time.sleep(self.interval)

    def request_length(self):
        url = UrlBuilder.build(self.timer.dt)
        headers = {'user-agent': 'Dancing robot/v0.0.0'}
        resp = requests.head(url, headers=headers)
        #print(resp.status_code, resp.text, resp.headers)
        print("Sir, treasury have " + resp.headers['X-RateLimit-Remaining'] + " requests left.")
        return resp.headers['Content-Length']

    def dance(self):
        print("Look ma, dancing without hands!")

robo_king = Ruler(60)
robo_king.rule()

timer = DanceTiming()
print(timer.dt.isoformat())
print(UrlBuilder.build(timer.dt))
exit()


# testing part of code
headers = {'user-agent': 'Dancing robot/v0.0.0'}
url = 'https://api.github.com/repos/gokhanbarisaker/dancingrobot-client/commits?since=2016-03-01T00:00:00Z'
resp = requests.head(url, headers=headers)
print(resp.status_code, resp.text, resp.headers)
if 'Content-Length' in resp.headers:
    print(resp.headers['Content-Length'])
